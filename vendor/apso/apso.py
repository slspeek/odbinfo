# coding: utf-8

from __future__ import unicode_literals

import ast
import traceback
import webbrowser
from subprocess import call as sub_call
from sys import getfilesystemencoding, version_info
from threading import Thread

import uno
import unohelper
from apso_utils import console, getConfigurationAccess, getProductName, msgbox

try:
    import pythonscript
except ImportError:
    import pythonloader
    pythonscript = None
    for url, module in pythonloader.g_loadedComponents.iteritems():
        if url.endswith("script-provider-for-python/pythonscript.py"):
            pythonscript = module
    if pythonscript is None:
        raise Exception("Impossible de trouver le module pythonscript.")

from com.sun.star.awt import (Selection, XActionListener,
                              XContainerWindowEventHandler, XKeyListener,
                              XMouseListener)
from com.sun.star.awt.MessageBoxResults import YES
from com.sun.star.awt.MessageBoxType import ERRORBOX, MESSAGEBOX, WARNINGBOX
from com.sun.star.awt.PosSize import POS, POSSIZE, SIZE
from com.sun.star.awt.tree import XTreeExpansionListener
from com.sun.star.lang import Locale
from com.sun.star.task import XJobExecutor
from com.sun.star.ui.dialogs.TemplateDescription import (
    FILEOPEN_SIMPLE, FILESAVE_AUTOEXTENSION)
from com.sun.star.uno import Exception as UNOException
from com.sun.star.view import XSelectionChangeListener

# -----------------------------------------------------------
#   GENERICS
# -----------------------------------------------------------
# Addon ID
EXTID = 'apso.python.script.organizer'

# libO or AOO ?
PRODUCT = getProductName()

# see ErrorMessage and ErrorAsMessage
ENCODING = getfilesystemencoding()

# global resource resolver
RR = None

# global temporary files
tempfiles = {}

# uno implementation
g_ImplementationHelper = unohelper.ImplementationHelper()


def getEditorKickerConfig(ctx):
    key = "/apso.EditorKicker"
    names = ("Editor", "Options")
    reader = getConfigurationAccess(key)
    values = reader.getPropertyValues(names)
    if len(values) != 2 or values[0] == "":
        return False
    elif values[1] == "":
        return values[0], "{FILENAME}"
    return values[0], values[1]


def open_script(ekconfig, url, lineno, offset):
    if ekconfig:
        cmd = '"{}" {}'.format(*ekconfig)
        cmd = cmd.replace('${', '{')   # compatibility hack with older version
        file = '"{}"'.format(uno.fileUrlToSystemPath(url))
        cmd = cmd.format(FILENAME=file, ROW=lineno, COL=offset)
        if version_info < (3,):
            cmd = cmd.encode(ENCODING)
        thread = Thread(target=sub_call, args=(cmd,), kwargs=dict(shell=True))
        thread.start()
    else:
        webbrowser.open(uno.fileUrlToSystemPath(url))


class ASTVisitFunctions(ast.NodeVisitor):
    def __init__(self, url, func):
        self.func = func
        with open(url) as f:
            self.code = ast.parse(f.read())
        self.line = 0

    def getlineno(self):
        self.visit(self.code)
        return self.line

    def visit_FunctionDef(self, node):
        if node.name == self.func:
            self.line = node.lineno
            return


class ResourceResolver(object):
    '''Resource Resolver for localized strings'''

    def __init__(self, ctx):
        self.ctx = ctx
        self.smgr = self.ctx.getServiceManager()
        self.locale = self._get_env_locale()
        self.srwl = self._get_resource_resolver()
        self.version = self._get_ext_ver()

    def _get_ext_path(self):
        '''Get addon installation path'''
        pip = self.ctx.getByName(
            "/singletons/com.sun.star.deployment.PackageInformationProvider")
        extpath = pip.getPackageLocation(EXTID)
        if extpath[-1] != "/":
            extpath += "/"
        return extpath

    def _get_ext_ver(self):
        '''Get addon version number'''
        pip = self.ctx.getByName(
            "/singletons/com.sun.star.deployment.PackageInformationProvider")
        extensions = pip.getExtensionList()
        for ext in extensions:
            if EXTID in ext:
                return ext[1]
        return ''

    def _get_env_locale(self):
        '''Get interface locale'''
        ps = self.smgr.createInstanceWithContext(
            "com.sun.star.util.PathSubstitution", self.ctx)
        vlang = ps.getSubstituteVariableValue("vlang")
        alang = vlang.split("-") + 2*[""]
        locale = Locale(*alang[:3])
        return locale

    def _get_resource_resolver(self):
        url = self._get_ext_path() + "python"
        handler = self.smgr.createInstanceWithContext(
            "com.sun.star.task.InteractionHandler", self.ctx)
        srwl = self.smgr.createInstanceWithArgumentsAndContext(
            "com.sun.star.resource.StringResourceWithLocation",
            (url, False, self.locale, "apsostrings", "", handler), self.ctx)
        return srwl

    def resolvestring(self, id):
        return self.srwl.resolveString(id)


def loadResourceResolver(ctx):
    global RR
    if not RR:
        RR = ResourceResolver(ctx)


class DialogBase(object):
    """ Base class for dialog. """

    def __init__(self, ctx):
        self.ctx = ctx
        self.smgr = ctx.getServiceManager()

    def create(self, name, arguments=None):
        """ Create service instance. """
        if arguments:
            return self.smgr.createInstanceWithArgumentsAndContext(
                name, arguments, self.ctx)
        else:
            return self.smgr.createInstanceWithContext(
                name, self.ctx)


class RuntimeDialogBase(DialogBase):
    """ Runtime dialog base. """

    def __init__(self, ctx):
        DialogBase.__init__(self, ctx)
        self.dialog = None

    def _result(self):
        """ Returns result. """
        return None

    def _init(self):
        """ Initialize, create dialog and controls. """

    def execute(self):
        """ Execute to show this dialog.
        None return value should mean canceled.
        """
        self._init()
        result = None
        if self.dialog.execute():
            result = self._result()
        self.dialog.dispose()
        return result

    def create_control(self, name, type_, pos, size, prop_names, prop_values, full_name=False):
        """ Create and insert control. """
        if not full_name:
            type_ = "com.sun.star.awt.UnoControl" + type_ + "Model"
        dialog_model = self.dialog.getModel()
        model = dialog_model.createInstance(type_)
        if prop_names and prop_values:
            model.setPropertyValues(prop_names, prop_values)
        dialog_model.insertByName(name, model)
        ctrl = self.dialog.getControl(name)
        ctrl.setPosSize(pos[0], pos[1], size[0], size[1], POSSIZE)
        return ctrl

    def create_dialog(self, title, pos=None, size=None, parent=None):
        """ Create base dialog. """
        dialog = self.create("com.sun.star.awt.UnoControlDialog")
        dialog_model = self.create("com.sun.star.awt.UnoControlDialogModel")
        dialog_model.ResourceResolver = RR.srwl
        dialog.setModel(dialog_model)
        dialog.setVisible(False)
        dialog.setTitle(title)
        if isinstance(size, tuple) and len(size) == 2:
            dialog.setPosSize(0, 0, size[0], size[1], SIZE)
        if isinstance(pos, tuple) and len(pos) == 2:
            dialog.setPosSize(pos[0], pos[1], 0, 0, POS)
        elif parent:
            pass
        self.dialog = dialog

    def create_label(self, name, command, pos, size,
                     prop_names=None, prop_values=None, action=None):
        """ Create and add new label. """
        self.create_control(name, "Label", pos, size, prop_names, prop_values)

    def create_button(self, name, command, pos, size,
                      prop_names=None, prop_values=None, action=None):
        """ Create and add new button. """
        btn = self.create_control(
            name, "Button", pos, size, prop_names, prop_values)
        btn.setActionCommand(command)
        if action:
            btn.addActionListener(action)

    def create_edit(self, name, pos, size, prop_names=None, prop_values=None):
        """ Create and add new edit control. """
        self.create_control(name, "Edit", pos, size, prop_names, prop_values)

    def create_tree(self, name, pos, size, prop_names=None, prop_values=None):
        """ Create and add new tree. """
        self.create_control(name, "com.sun.star.awt.tree.TreeControlModel",
                            pos, size, prop_names, prop_values, full_name=True)

    def get(self, name):
        """ Returns specified control by name. """
        return self.dialog.getControl(name)

    def get_text(self, name):
        """ Returns value of Text attribute specified by name. """
        return self.dialog.getControl(name).getModel().Text

    def set_focus(self, name):
        """ Set focus to the control specified by the name. """
        self.dialog.getControl(name).setFocus()


class NameInput(RuntimeDialogBase):
    """ Input dialog. """
    MARGIN = 3
    BUTTON_WIDTH = 80
    BUTTON_HEIGHT = 26
    HEIGHT = MARGIN * 3 + BUTTON_HEIGHT * 2
    WIDTH = 300
    EDIT_NAME = "edit_name"

    def __init__(self, ctx, title, default="", parent=None):
        RuntimeDialogBase.__init__(self, ctx)
        self.title = title
        self.default = default
        self.parent = parent

    def _init(self):
        margin = self.MARGIN
        self.create_dialog(self.title, size=(self.WIDTH, self.HEIGHT))
        self.create_edit(self.EDIT_NAME,
                         pos=(margin, margin),
                         size=(self.WIDTH - margin * 2, self.BUTTON_HEIGHT),
                         prop_names=("HideInactiveSelection", "Text",),
                         prop_values=(True, self.default,))
        self.create_button("btn_ok", "ok",
                           pos=(self.WIDTH - self.BUTTON_WIDTH * 2 - margin * 2,
                                self.BUTTON_HEIGHT + margin * 2),
                           size=(self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                           prop_names=("DefaultButton", "Label",
                                       "PushButtonType",),
                           prop_values=(True, "OK", 1))
        self.create_button("btn_cancel", "cancel",
                           pos=(self.WIDTH - self.BUTTON_WIDTH - margin,
                                self.BUTTON_HEIGHT + margin * 2),
                           size=(self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                           prop_names=("Label", "PushButtonType"), prop_values=("Cancel", 2))
        self.set_focus(self.EDIT_NAME)
        if self.parent:
            self.dialog.createPeer(self.parent.getToolkit(), self.parent)
        if self.default:
            self.get(self.EDIT_NAME).setSelection(
                Selection(0, len(self.default)))

    def _result(self):
        return self.get_text("edit_name")


class FileOpenDialog(DialogBase):
    """ To get file url to open. """

    def __init__(self, ctx, **kwds):
        DialogBase.__init__(self, ctx)
        self.args = kwds
        AvailableServiceNames = self.ctx.getServiceManager().getAvailableServiceNames()
        if "com.sun.star.ui.dialogs.SystemFilePicker" in AvailableServiceNames:
            self.filepickerservice = "com.sun.star.ui.dialogs.SystemFilePicker"
        elif "com.sun.star.ui.dialogs.GtkFilePicker" in AvailableServiceNames:
            self.filepickerservice = "com.sun.star.ui.dialogs.GtkFilePicker"
        else:
            self.filepickerservice = "com.sun.star.ui.dialogs.FilePicker"

    def execute(self):
        fp = self.create(self.filepickerservice)
        args = self.args
        if "template" in args:
            fp.initialize((args["template"],))
        if "title" in args:
            fp.setTitle(args["title"])
        if "default" in args:
            default = args["default"]
            fp.setDefaultName(self._substitute_variables(default))
        if "directory" in args:
            fp.setDisplayDirectory(args["directory"])
        if "filters" in args:
            for title, filter in args["filters"]:
                fp.appendFilter(title, filter)
        result = None
        if fp.execute():
            result = fp.getFiles()[0]
        return result

    def _substitute_variables(self, uri):
        return self.create("com.sun.star.util.PathSubstitution").\
            substituteVariables(uri, True)


class MessageDialog(DialogBase):
    """ Shows message in standard message box. """

    def __init__(self, ctx, parent, **kwds):
        DialogBase.__init__(self, ctx)
        self.parent = parent
        self.args = kwds

    def execute(self):
        args = self.args
        type = args.get("type", MESSAGEBOX)
        buttons = args.get("buttons", 1)
        title = args.get("title", "")
        message = args.get("message", "")
        toolkit = self.parent.getToolkit()
        dialog = toolkit.createMessageBox(
            self.parent, type, buttons, title, message)
        n = dialog.execute()
        dialog.dispose()
        return n


def join_url(base, name, name_encode=True):
    """ Join name to base URL. """
    if name_encode:
        _name = name
    else:
        _name = unohelper.systemPathToFileUrl(name)
    if base.endswith("/"):
        return base + _name
    return base + "/" + _name


def base_url(url):
    """ Returns directory of URL. """
    if url.startswith(OrganizerDialog.DOC_PROTOCOL):
        return "/".join(url.split("/")[:-1])
    if url.startswith("file:///"):
        return "/".join(url.split("/")[:-1])
    else:
        return unohelper.absolutize(url, "../")


class ErrorMessageDialog(RuntimeDialogBase):
    """ Shows error message in custom dialog with selectable text. """
    MARGIN = 3
    BUTTON_WIDTH = 80
    BUTTON_HEIGHT = 26
    EDIT_HEIGHT = 300
    HEIGHT = EDIT_HEIGHT + MARGIN * 5 + BUTTON_HEIGHT + MARGIN
    WIDTH = 420
    EDIT_NAME = "edit_name"

    ERROR_ICON = "private:standardimage/error"

    def __init__(self, ctx, **kwds):
        RuntimeDialogBase.__init__(self, ctx)
        self.args = kwds

    def _init(self):
        args = self.args
        title = args.get("title", "")
        message = args.get("message", "")

        margin = self.MARGIN
        self.create_dialog(title, size=(self.WIDTH, self.HEIGHT))

        self.create_edit("edit_message",
                         pos=(margin * 4, margin * 4),
                         size=(self.WIDTH - margin * 8, self.EDIT_HEIGHT),
                         prop_names=("Border", "MultiLine", "PaintTransparent",
                                     "ReadOnly", "VScroll"),
                         prop_values=(0, True, True, True, True))
        self.get("edit_message").getModel().Text = message
        self.create_button("btn_ok", "ok",
                           pos=((self.WIDTH - self.BUTTON_WIDTH)/2,
                                self.HEIGHT - self.BUTTON_HEIGHT - margin),
                           size=(self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                           prop_names=("DefaultButton", "Label",
                                       "PushButtonType",),
                           prop_values=(True, "OK", 1))
        frame = self.create("com.sun.star.frame.Desktop").getCurrentFrame()
        window = frame.getContainerWindow() if frame else None
        self.dialog.createPeer(self.create("com.sun.star.awt.Toolkit"), window)
        if window:
            ps = window.getPosSize()
            x = ps.Width / 2 - self.WIDTH / 2
            y = ps.Height / 2 - self.HEIGHT / 2
        self.dialog.setPosSize(x, y, 0, 0, POS)


class SyntaxErrorMessageDialog(RuntimeDialogBase):
    """ Shows syntax error message in custom dialogwith selectable text."""
    MARGIN = 3
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 26
    EDIT_HEIGHT = 300
    HEIGHT = EDIT_HEIGHT + MARGIN * 5 + BUTTON_HEIGHT + MARGIN
    WIDTH = 420
    EDIT_NAME = "edit_name"

    ERROR_ICON = "private:standardimage/error"

    def __init__(self, ctx, **kwds):
        RuntimeDialogBase.__init__(self, ctx)
        self.args = kwds

    def _init(self):
        args = self.args
        title = args.get("title", "")
        message = args.get("message", "")
        ekconfig = args.get("ekconfig", "")

        margin = self.MARGIN
        self.create_dialog(title, size=(self.WIDTH, self.HEIGHT))

        self.create_edit("edit_message",
                         pos=(margin * 4, margin * 4),
                         size=(self.WIDTH - margin * 8, self.EDIT_HEIGHT),
                         prop_names=("Border", "MultiLine", "PaintTransparent",
                                     "ReadOnly", "VScroll"),
                         prop_values=(0, True, True, True, True))
        self.get("edit_message").getModel().Text = message
        if ekconfig and ("{ROW}" in ekconfig[1]):
            self.create_button("btn_ok", "ok",
                               pos=((self.WIDTH - self.BUTTON_WIDTH*2.5 - margin*3)/2,
                                    self.HEIGHT - self.BUTTON_HEIGHT - margin),
                               size=(self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                               prop_names=("DefaultButton", "Label",
                                           "PushButtonType",),
                               prop_values=(False, RR.resolvestring("msg28").upper(), 2))
            self.create_button("btn_open_edit", "edit",
                               pos=((self.WIDTH - self.BUTTON_WIDTH*0.5 + 3*margin)/2,
                                    self.HEIGHT - self.BUTTON_HEIGHT - margin),
                               size=(self.BUTTON_WIDTH*1.5,
                                     self.BUTTON_HEIGHT),
                               prop_names=("DefaultButton", "Label",
                                           "PushButtonType",),
                               prop_values=(True, '~{}'.format(RR.resolvestring('msg19').upper()), 1))
        else:
            self.create_button("btn_ok", "ok",
                               pos=((self.WIDTH - self.BUTTON_WIDTH)/2,
                                    self.HEIGHT - self.BUTTON_HEIGHT - margin),
                               size=(self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                               prop_names=("DefaultButton", "Label",
                                           "PushButtonType",),
                               prop_values=(True, RR.resolvestring("msg28").upper(), 2))
        frame = self.create("com.sun.star.frame.Desktop").getCurrentFrame()
        window = frame.getContainerWindow() if frame else None
        self.dialog.createPeer(self.create("com.sun.star.awt.Toolkit"), window)
        if window:
            ps = window.getPosSize()
            x = ps.Width / 2 - self.WIDTH / 2
            y = ps.Height / 2 - self.HEIGHT / 2
        self.dialog.setPosSize(x, y, 0, 0, POS)

    def execute(self):
        self._init()
        result = self.dialog.execute()
        self.dialog.dispose()
        return result


if version_info < (3,):
    class ErrorMessage_(Exception):
        def __init__(self, message):
            super(ErrorMessage_, self).__init__(message.encode(ENCODING))
            self.message = message

        def __unicode__(self):
            return self.message

    class ErrorAsMessage(ErrorMessage_):
        """ Tracked error message will be shown for user. """
        pass
else:
    class ErrorAsMessage(Exception):
        """ Tracked error message will be shown for user. """
        pass


# -----------------------------------------------------------
#     APSO
# -----------------------------------------------------------

class NodeManager(object):
    """ Maps between tree node and script node. """
    LOADED = 0x100000
    SCRIPT = 0x700000
    MASK = 0xfffff
    TYPE_MASK = 0xf00000

    def __init__(self):
        self.nodes = []    # to avoid adapter creation for each node

    def _node_set(self, tree_node, node, script=False):
        """ Set script node for tree_node. """
        self.nodes.append(node)
        i = len(self.nodes) - 1
        if script:
            i |= self.SCRIPT
        tree_node.DataValue = i

    def _node_get(self, tree_node):
        """ Get script node for tree_node. """
        try:
            i = tree_node.DataValue
            if isinstance(i, int) or isinstance(i, long):
                return self.nodes[i & self.MASK]
        except Exception:
            pass

    def _node_delete(self, tree_node):
        """ Delete script node for tree_node."""
        try:
            i = tree_node.DataValue
            if isinstance(i, int):
                # TODO: check for deleting following line
                node = self.nodes[i & self.MASK]
                self.nodes[i] = None
        except Exception:
            pass

    def _node_is_script(self, tree_node):
        """ Check the node is script for tree_node. """
        return (tree_node.DataValue & self.TYPE_MASK) == self.SCRIPT

    def _node_set_loaded(self, tree_node):
        """ Set loaded flag. """
        tree_node.DataValue = tree_node.DataValue | self.LOADED

    def _node_is_loaded(self, tree_node):
        """ Check loaded flag. """
        return (tree_node.DataValue & self.TYPE_MASK) == self.LOADED


class OrganizerDialog(NodeManager, RuntimeDialogBase):
    """ Alternative organizer dialog for Python scripts. """

    TREE_NAME = "tree"
    FILE_EXT = ".py"
    DOC_PROTOCOL = "vnd.sun.star.tdoc"
    SCRIPT_PROTOCOL = "vnd.sun.star.script"

    DISK_ICON = "private:graphicrepository/res/harddisk_16.png"
    DOC_ICON = "private:graphicrepository/res/sx03150.png"
    DIR_ICON = "private:graphicrepository/res/fileopen.png"
    FILE_ICON = "private:graphicrepository/res/im30820.png"
    SCRIPT_ICON = "private:graphicrepository/res/im30821.png"

    MARGIN = 3
    BUTTON_WIDTH = 80
    BUTTON_HEIGHT = 26
    TREE_HEIGHT = 250
    HEIGHT = TREE_HEIGHT + BUTTON_HEIGHT + MARGIN * 3
    WIDTH = 300

    ENABLE_EDIT = True
    ENABLE_DEBUG = True
    ENABLE_SHELL = True

    def __init__(self, ctx,
                 user_provider, share_provider, document_provider,
                 parent, show_icon=False):
        NodeManager.__init__(self)
        RuntimeDialogBase.__init__(self, ctx)
        self.parent = parent
        self.user_provider = user_provider
        self.share_provider = share_provider
        self.document_provider = document_provider
        self.show_icon = show_icon
        self.tree = None
        self.menu = None
        self.tempdir = None
        self.ekconfig = getEditorKickerConfig(ctx)

    def execute(self, history=None):
        """ Show dialog with history represented as script in URI form."""
        self._create_ui()
        self._set_history(history)
        result = None
        n = self.dialog.execute()
        if n:
            result = self.tree_get_selected_node_uri()
        tree_node = self.tree_get_selected_node()
        node = self._node_get(tree_node)
        if hasattr(node, 'uri') and node.uri.startswith(self.DOC_PROTOCOL):
            try:
                tempfile = tempfiles[node.uri]
                sfa = node.provCtx.sfa
                if sfa.exists(tempfile):
                    sfa.copy(tempfile, node.uri)
            except KeyError:
                pass
        self.tree = None
        self.dialog.dispose()
        return result, n

    def button_pushed(self, command):
        try:
            tree_node = self.tree_get_selected_node()
            if tree_node:
                node = self._node_get(tree_node)
                getattr(self, "exec_" + command)(tree_node, node)
        except ErrorAsMessage as e:
            MessageDialog(self.ctx, self.dialog.getPeer(), type=ERRORBOX,
                          title=RR.resolvestring('msg01'), message=str(e)).execute()
        except Exception as e:
            print(e)
            traceback.print_exc()

    def exec_execute(self, tree_node, node):
        """ Execute selected macro. """
        if self._node_is_script(tree_node):
            self.dialog.endDialog(1)

    def exec_menu(self, tree_node, node):
        """ Shows dropdown menu. """
        if not self.menu:
            self._create_menu()
        menu = self.menu

        if tree_node:
            if isinstance(node, pythonscript.ScriptBrowseNode):
                states = (False, False, self.ENABLE_EDIT, False,
                          False, False, False, False, self.ENABLE_DEBUG,
                          self.ENABLE_SHELL)
            elif isinstance(node, pythonscript.FileBrowseNode):
                states = [False, False, self.ENABLE_EDIT, False,
                          True, True, False, True, False, self.ENABLE_SHELL]
                if node.uri.startswith(self.DOC_PROTOCOL):
                    states[3] = True
                    states[5] = False
                    states[6] = True
                elif not self.document_provider:
                    states[5] = False
            elif isinstance(node, pythonscript.DirBrowseNode):
                states = (True, True, False, False, True,
                          False, False, True, False, self.ENABLE_SHELL)
            else:
                states = (True, True, False, False, False,
                          False, False, False, False, self.ENABLE_SHELL)
            for i, state in enumerate(states):
                menu.enableItem(i + 1, state)

        btn = self.dialog.getControl("btn_menu")
        n = menu.execute(
            btn.getContext().getPeer(), btn.getPosSize(), 0)
        if n > 0:
            self.button_pushed(menu.getCommand(n))

    def exec_create_file(self, tree_node, node, filename=None):
        """ Create new file under selected node. """
        if isinstance(node, pythonscript.PythonScriptProvider):
            node = node.dirBrowseNode
        elif not isinstance(node, pythonscript.DirBrowseNode):
            return
        name = filename or self._input_name(RR.resolvestring('msg02'))
        if name.strip():
            uri = join_url(node.rootUrl, name)
            if not uri.endswith(self.FILE_EXT):
                uri += self.FILE_EXT
            sfa = node.provCtx.sfa
            if sfa.exists(uri):
                raise ErrorAsMessage(RR.resolvestring('msg03').format(name))
            is_doc = uri.startswith(self.DOC_PROTOCOL)
            try:
                if is_doc:
                    io = self.create("com.sun.star.io.Pipe")
                else:
                    io = sfa.openFileWrite(uri)
            except Exception as e:
                raise ErrorAsMessage(str(e))
            try:
                # Default content of any new module.
                template = getConfigurationAccess(
                    "/apso.EditorKicker").getPropertyValue("Header")
                if template or is_doc:
                    text_out = self.create(
                        "com.sun.star.io.TextOutputStream")
                    text_out.setOutputStream(io)
                    text_out.setEncoding("UTF-8")
                    text_out.writeString(template)
                    if is_doc:
                        text_out.closeOutput()
                        sfa.writeFile(uri, io)
            except Exception as e:
                raise ErrorAsMessage(str(e))
            finally:
                if is_doc:
                    io.closeInput()
                else:
                    io.closeOutput()

            child_node = pythonscript.FileBrowseNode(
                node.provCtx, uri, name)
            self._create_new_tree_node(
                tree_node, name, True, child_node)

    def exec_create_dir(self, tree_node, node):
        """ Create new directory under selected node. """
        if isinstance(node, pythonscript.PythonScriptProvider):
            node = node.dirBrowseNode
        elif not isinstance(node, pythonscript.DirBrowseNode):
            return
        name = self._input_name(RR.resolvestring('msg04'),
                                default=RR.resolvestring('msg34'))
        if name.strip():
            uri = join_url(node.rootUrl, name)
            sfa = node.provCtx.sfa
            if sfa.exists(uri):
                raise ErrorAsMessage(RR.resolvestring('msg05').format(name))
            try:
                sfa.createFolder(uri)
                child_node = pythonscript.DirBrowseNode(
                    node.provCtx, name, uri)
                self._create_new_tree_node(
                    tree_node, name, False, child_node, True)
            except Exception as e:
                raise ErrorAsMessage(str(e))

    def exec_substitute(self, tree_node, node):
        """ Substitute script file in documents. """
        if not isinstance(node, pythonscript.FileBrowseNode):
            return
        if not node.uri.startswith(self.DOC_PROTOCOL):
            return
        url = FileOpenDialog(self.ctx,
                             default="$(user)/Scripts/python",
                             filters=((RR.resolvestring('msg06'), "*.py"),
                                      (RR.resolvestring('msg07'), "*.*"),)).execute()
        if url is not None:
            sfa = node.provCtx.sfa
            if not sfa.exists(url):
                raise ErrorAsMessage(RR.resolvestring('msg08') + url)
            try:
                sfa.copy(url, node.uri)
            except Exception as e:
                raise ErrorAsMessage(str(e))

    def exec_rename(self, tree_node, node):
        """ Rename selected file. """
        if not (isinstance(node, pythonscript.FileBrowseNode) or
                isinstance(node, pythonscript.DirBrowseNode)):
            return
        current = node.getName()
        name = self._input_name(RR.resolvestring('msg09'), current)
        # if name is not None or not name == "":
        if name.strip():
            if isinstance(node, pythonscript.FileBrowseNode):
                uri = node.uri
            elif isinstance(node, pythonscript.DirBrowseNode):
                uri = node.rootUrl
            new_uri = join_url(base_url(uri), name)
            if (isinstance(node, pythonscript.FileBrowseNode) and
                    not new_uri.endswith(self.FILE_EXT)):
                new_uri += self.FILE_EXT
            sfa = node.provCtx.sfa
            if not sfa.exists(uri):
                raise ErrorAsMessage(RR.resolvestring('msg10') + current)
            if sfa.exists(new_uri):
                raise ErrorAsMessage(RR.resolvestring('msg11') + name)
            try:
                sfa.move(uri, new_uri)
                tree_node.setDisplayValue(name)
                node.name = name
                node.uri = new_uri
            except Exception as e:
                raise ErrorAsMessage(str(e))

    def exec_copytodoc(self, tree_node, node):
        """ Copy user or share script file in documents. """
        name = node.getName()
        doc_node = self.document_provider.dirBrowseNode
        doc_uri = join_url(doc_node.rootUrl, name)
        if not doc_uri.endswith(self.FILE_EXT):
            doc_uri += self.FILE_EXT
        sfa = node.provCtx.sfa
        if sfa.exists(doc_uri):
            msg = RR.resolvestring('msg12').format(name)
            n = MessageDialog(self.ctx, self.dialog.getPeer(),
                              type=WARNINGBOX,
                              buttons=3, title=RR.resolvestring('msg13'),
                              message=msg).execute()
            if n != YES:
                return
        else:
            self.exec_create_file(self._get_tree_node("document"),
                                  doc_node, node.getName())
        try:
            sfa.copy(node.uri, doc_uri)
        except Exception as e:
            raise ErrorAsMessage(str(e))

    def exec_export(self, tree_node, node):
        """ Export script file outside of document. """
        url = FileOpenDialog(self.ctx,
                             default=node.getName(),
                             template=FILESAVE_AUTOEXTENSION,
                             filters=((RR.resolvestring('msg06'), "*.py"),)).execute()
        if url:
            sfa = node.provCtx.sfa
            sfa.copy(node.uri, url)
            # self.dialog.endDialog(1)

    def exec_delete(self, tree_node, node):
        """ Delete selected node. """
        if not (isinstance(node, pythonscript.FileBrowseNode) or
                isinstance(node, pythonscript.DirBrowseNode)):
            return
        name = node.getName()
        n = MessageDialog(self.ctx, self.dialog.getPeer(), type=WARNINGBOX,
                          buttons=3, title=RR.resolvestring('msg14'),
                          message=RR.resolvestring('msg15').format(name)).execute()
        if n == YES:
            if isinstance(node, pythonscript.FileBrowseNode):
                uri = node.uri
            elif isinstance(node, pythonscript.DirBrowseNode):
                uri = node.rootUrl
            sfa = node.provCtx.sfa
            try:
                sfa.kill(uri)
                self._node_delete(tree_node)
                parent_node = tree_node.getParent()
                parent_node.removeChildByIndex(
                    parent_node.getIndex(tree_node))
            except Exception as e:
                raise ErrorAsMessage(str(e))

    def exec_edit(self, tree_node, node):
        try:
            if node.uri.startswith(self.DOC_PROTOCOL):
                try:
                    url = tempfiles[node.uri]
                    sfa = node.provCtx.sfa
                    if not sfa.exists(url):
                        url = self._create_tempfile(node)
                except KeyError:
                    url = self._create_tempfile(node)
            else:
                url = node.uri
            if self.ekconfig and self._node_is_script(tree_node):
                lineno = self.getFuncLine(url, node.funcName)
            else:
                lineno = 0
            open_script(self.ekconfig, url, lineno, 0)
        except Exception as e:
            raise ErrorAsMessage("exec_edit\n\n"+str(e))

    def exec_debug(self, tree_node, node):
        """ Debug selected macro. """
        if self._node_is_script(tree_node):
            if node.uri.startswith(self.DOC_PROTOCOL):
                try:
                    url = tempfiles[node.uri]
                    sfa = node.provCtx.sfa
                    if not sfa.exists(url):
                        self._create_tempfile(node)
                except KeyError:
                    self._create_tempfile(node)
            self.dialog.endDialog(2)

    def exec_shell(self, tree_node, node):
        try:
            provctx = node.provCtx
            # this line must come first
            loc = {'XSCRIPTCONTEXT': provctx.scriptContext}
            if isinstance(node, (pythonscript.FileBrowseNode, pythonscript.ScriptBrowseNode)):
                module = provctx.getModuleByUrl(node.uri)
                loc.update(module.__dict__)
            self.dialog.endDialog(0)
            console(loc=loc)
        except Exception:
            msgbox(traceback.format_exc())

    def _create_tempfile(self, node):
        """ Copy embedded script to temporary folder."""
        try:
            if not self.tempdir:
                TP = self.smgr.createInstanceWithContext(
                    "com.sun.star.io.TempFile", self.ctx)
                self.tempdir = base_url(TP.Uri)
            path = node.uri.replace(self.DOC_PROTOCOL + ':/', '')
            filepath = join_url(self.tempdir, path)
            dirpath = '/'.join(filepath.split('/')[:-1])
            sfa = node.provCtx.sfa
            sfa.createFolder(dirpath)
            sfa.copy(node.uri, filepath)
            tempfiles[node.uri] = filepath
            return filepath
        except Exception as e:
            raise ErrorAsMessage("_create_tempfile\n\n"+str(e))

    class ListenerBase(unohelper.Base):
        def __init__(self, act):
            self.act = act

        def disposing(self, source):
            self.act = None

    class ActionListener(ListenerBase, XActionListener):
        def actionPerformed(self, ev):
            self.act.button_pushed(ev.ActionCommand)

    class KeyListener(ListenerBase, XKeyListener):
        def keyPressed(self, ev):
            pass

        def keyReleased(self, ev):
            if ev.KeyCode == 1280:
                self.act._key_pressed()

    def _key_pressed(self):
        node = self.tree_get_selected_node()
        if node:
            if self._node_is_script(node):
                self.dialog.endDialog(1)
            else:
                self._expand_node(node)

    class MouseListener(ListenerBase, XMouseListener):
        def mouseReleased(self, ev):
            pass

        def mouseEntered(self, ev):
            pass

        def mouseExited(self, ev):
            pass

        def mousePressed(self, ev):
            if ev.ClickCount == 2 and ev.Buttons == 1:
                self.act._mouse_pressed(ev)

    def _mouse_pressed(self, ev):
        node = self.tree_get_selected_node()
        if node and self._node_is_script(node):
            self.dialog.endDialog(1)

    class TreeExpansionListener(ListenerBase, XTreeExpansionListener):
        def treeExpanding(self, ev):
            pass

        def treeCollapsing(self, ev):
            pass

        def treeExpanded(self, ev):
            pass

        def treeCollapsed(self, ev):
            pass

        def requestChildNodes(self, ev):
            try:
                node = ev.Node
                if node:
                    self.act.node_requested(node)
            except ErrorAsMessage as e:
                MessageDialog(self.act.ctx, self.act.dialog.getPeer(),
                              title=RR.resolvestring('msg01'), message=str(e)).execute()
            except Exception as e:
                print(e)
                traceback.print_exc()

    class SelectionChangeListener(ListenerBase, XSelectionChangeListener):
        def __init__(self, act):
            act.ListenerBase.__init__(self, act)
            self.btn_execute = act.get("btn_execute")

        def selectionChanged(self, ev):
            try:
                selection = ev.Source.getSelection()
                if selection:
                    is_script = self.act._node_is_script(selection)
                    self.btn_execute.setEnable(is_script)
            except ErrorAsMessage as e:
                MessageDialog(self.act.ctx, self.act.dialog.getPeer(),
                              title=RR.resolvestring('msg01'), message=str(e)).execute()
            except Exception as e:
                print(e)
                traceback.print_exc()

    def getFuncLine(self, url, funcname):
        path = uno.fileUrlToSystemPath(url)
        v = ASTVisitFunctions(path, funcname)
        return v.getlineno()

    def node_requested(self, tree_node):
        """ Add children for the tree_node at expanding. """
        data_model = self.tree.getModel().DataModel
        node = self._node_get(tree_node)
        if isinstance(node, pythonscript.FileBrowseNode):
            if node.uri.startswith(self.DOC_PROTOCOL):
                try:
                    url = tempfiles[node.uri]
                    sfa = node.provCtx.sfa
                    if sfa.exists(url):
                        sfa.copy(url, node.uri)
                except KeyError:
                    url = node.uri
                except Exception as e:
                    raise ErrorAsMessage(str(e))
            else:
                url = node.uri
        try:
            child_nodes = node.getChildNodes()
            if isinstance(node, pythonscript.PythonScriptProvider):
                if node.uno_packages_sp:
                    child_nodes += node.uno_packages_sp.getChildNodes()
        except SyntaxError as e:
            n = SyntaxErrorMessageDialog(
                self.ctx, title=RR.resolvestring('msg01'),
                message=str(e), ekconfig=self.ekconfig).execute()
            if n:
                if url.startswith(self.DOC_PROTOCOL):
                    try:
                        url = tempfiles[node.uri]
                    except KeyError:
                        url = self._create_tempfile(node)
                open_script(self.ekconfig, url, e.lineno, e.offset)
            return
        except Exception as e:
            raise ErrorAsMessage(str(e))
        if node and not tree_node.getChildCount() and child_nodes:
            show_icon = self.show_icon
            child_ondemand = True
            is_script = False
            if isinstance(node, pythonscript.ScriptBrowseNode):
                return
            elif isinstance(node, pythonscript.FileBrowseNode):
                child_ondemand = False
                is_script = True
            # child name conversation needed for name containing non ascii characters
            nodes = [(uno.fileUrlToSystemPath(child.getName()), child)
                     for child in child_nodes]
            from locale import strxfrm
            for name, child in sorted(nodes, key=lambda s: strxfrm(s[0])):
                if name == "__pycache__":
                    continue
                child.name = uno.fileUrlToSystemPath(name)
                tree_child = data_model.createNode(child.name, child_ondemand)
                if show_icon:
                    if isinstance(child, pythonscript.ScriptBrowseNode):
                        icon = self.SCRIPT_ICON
                    elif isinstance(child, pythonscript.FileBrowseNode):
                        icon = self.FILE_ICON
                    elif isinstance(child, pythonscript.DirBrowseNode):
                        icon = self.DIR_ICON
                    else:
                        icon = self.FILE_ICON
                    self._set_node_icon(tree_child, icon)
                tree_node.appendChild(tree_child)
                self._node_set(tree_child, child, is_script)
            self._node_set_loaded(tree_node)

    def _input_name(self, title="", default=None):
        if default is None:
            default = RR.resolvestring('msg33')
        """ Let user input new name. """
        return (NameInput(self.ctx, title, default, self.dialog.getPeer()).execute())

    def _set_history(self, history):
        """ Show and select node by history. """
        if history and history.startswith(self.SCRIPT_PROTOCOL):
            parts = history[len(self.SCRIPT_PROTOCOL)+1:].split("?", 1)
            if not len(parts) == 2 or parts[0].find("$") == -1:
                return
            params = parts[1].split("&")
            if "language=Python" not in params:
                return
            location = None
            for param in params:
                if param.startswith("location="):
                    location = param[9:].split(":")
                    break
            provider = None
            if hasattr(self, location[0] + "_provider"):
                provider = getattr(self, location[0] + "_provider")
            # elif len(location)>1:
            #     base_provider = getattr(self, location[0] + "_provider")
            #     provider = getattr(base_provider, location[1] + "_sp")
            if provider:
                parent_node = self._get_tree_node(location[0])
                self.node_requested(parent_node)
                self._expand_node(parent_node)

                path, func = parts[0].split("$", 1)
                paths = path.split("|")
                if paths[-1].endswith(self.FILE_EXT):
                    paths[-1] = paths[-1][:-len(self.FILE_EXT)]
                paths.append(func)
                tree_node = None
                for path in paths:
                    for i in range(parent_node.getChildCount()):
                        tree_node = parent_node.getChildAt(i)
                        if tree_node.getDisplayValue() == uno.fileUrlToSystemPath(path):
                            parent_node = tree_node
                            # self.node_requested(tree_node)
                            self._expand_node(parent_node)
                            break
                if tree_node:
                    self.tree_select_node(tree_node)

    def tree_get_selected_node(self):
        """ Returns selected tree node. """
        tree_node = self.tree.getSelection()
        if not isinstance(tree_node, tuple):
            return tree_node
        return None

    def tree_get_selected_node_uri(self):
        """ Returns script uri if selected node is script node. """
        tree_node = self.tree_get_selected_node()
        if self._node_is_script(tree_node):
            node = self._node_get(tree_node)
            if node:
                return node.getPropertyValue("URI")

    def tree_select_node(self, tree_node):
        """ Select tree node. """
        # this method ensure that the selected node will be displayed
        self.tree.startEditingAtNode(tree_node)
        self.tree.stopEditing()

    def _create_new_tree_node(self, tree_parent_node, name, ondemand, node,
                              directory=False, select=True):
        """ Create new tree node under tree_parent_node. """
        if not self._node_is_loaded(tree_parent_node):
            self.node_requested(tree_parent_node)
            return
        tree_node = self.tree.getModel().DataModel.createNode(name, ondemand)
        if self.show_icon:
            if directory:
                self._set_node_icon(tree_node, self.FILE_ICON)
            else:
                self._set_node_icon(tree_node, self.FILE_ICON)
        tree_parent_node.appendChild(tree_node)
        self._node_set(tree_node, node)
        if select:
            self.tree.select(tree_node)

    def _create_menu(self):
        """ Create popup menu. """
        menu = self.create("com.sun.star.awt.PopupMenu")
        menu.hideDisabledEntries(True)
        self.menu = menu
        items = (
            (1, 0, 0, RR.resolvestring('msg17'), "create_file"),
            (2, 1, 0, RR.resolvestring('msg18'), "create_dir"),
            (None, 2),
            (3, 3, 0, RR.resolvestring('msg19'), "edit"),
            (4, 4, 0, RR.resolvestring('msg20'), "substitute"),
            (5, 5, 0, RR.resolvestring('msg21'), "rename"),
            (None, 6),
            (6, 7, 0, RR.resolvestring('msg22'), "copytodoc"),
            (7, 8, 0, RR.resolvestring('msg23'), "export"),
            (8, 9, 0, RR.resolvestring('msg24'), "delete"),
            (None, 10),
            (9, 11, 0, RR.resolvestring('msg25'), "debug"),
            (10, 12, 0, RR.resolvestring('msg36'), "shell"),
        )
        for i in items:
            if i[0] is None or i[0] == -1:
                menu.insertSeparator(i[1])
            else:
                menu.insertItem(i[0], i[3], i[2], i[1])
                menu.setCommand(i[0], i[4])

    def _set_node_icon(self, node, icon):
        """ Set node icon. """
        node.setExpandedGraphicURL(icon)
        node.setCollapsedGraphicURL(icon)

    def _expand_node(self, tree_node):
        """ Request to expand node. """
        self.tree.expandNode(tree_node)

    def _get_tree_node(self, type):
        tree_node = None
        root_node = self.tree.getModel().DataModel.getRoot()
        n = -1
        if type == "user":
            if self.user_provider:
                n = 0
        elif type == "share":
            if self.share_provider:
                n = 0
                if self.user_provider:
                    n = 1
        elif type == "document":
            if self.document_provider:
                n = 0
                if self.user_provider:
                    n += 1
                if self.share_provider:
                    n += 1
        if n >= 0:
            tree_node = root_node.getChildAt(n)
        return tree_node

    def _create_ui(self):
        """ Create dialog ui. """
        btn_action = self.ActionListener(self)

        margin = self.MARGIN
        btn_size = self.BUTTON_WIDTH, self.BUTTON_HEIGHT
        btn_width, btn_height = btn_size
        btn_prop_names = ("Label", "PushButtonType")
        title = '{} - APSO v.{}'.format(RR.resolvestring('msg35'), RR.version)
        self.create_dialog(title, size=(self.WIDTH, self.HEIGHT))
        self.create_tree(self.TREE_NAME,
                         (margin, btn_height + margin * 2),
                         (self.WIDTH - 2 * margin, self.TREE_HEIGHT),
                         ("Tabstop",), (True,))
        self.create_button("btn_execute", "execute",
                           (margin, margin), btn_size,
                           btn_prop_names, (RR.resolvestring('msg26'), 0), btn_action)
        self.create_button("btn_menu", "menu",
                           (btn_width + margin * 2, margin), btn_size,
                           btn_prop_names, (RR.resolvestring('msg27'), 0), btn_action)
        self.create_button("btn_close", "",
                           (self.WIDTH - margin - btn_width, margin), btn_size,
                           btn_prop_names, (RR.resolvestring('msg28'), 2))

        tree = self.dialog.getControl(self.TREE_NAME)
        self.tree = tree
        tree_model = tree.getModel()
        data_model = self.create("com.sun.star.awt.tree.MutableTreeDataModel")
        tree_model.DataModel = data_model

        root = data_model.createNode("ROOT", False)
        data_model.setRoot(root)

        def add_node(name, provider, icon):
            node = data_model.createNode(name, True)
            if self.show_icon:
                self._set_node_icon(node, icon)
            root.appendChild(node)
            self._node_set(node, provider)

        if self.user_provider:
            add_node(RR.resolvestring('msg31'),
                     self.user_provider, self.DISK_ICON)
        if self.share_provider:
            add_node(RR.resolvestring('msg32').format(PRODUCT),
                     self.share_provider, self.DISK_ICON)
        if self.document_provider:
            add_node(self.document_provider.title,
                     self.document_provider, self.DOC_ICON)

        tree_model.SelectionType = 1
        tree_model.RootDisplayed = False

        tree.addTreeExpansionListener(self.TreeExpansionListener(self))
        try:
            tree.addSelectionChangeListener(self.SelectionChangeListener(self))
        except Exception as e:
            print(str(e))
        tree.addMouseListener(self.MouseListener(self))
        tree.addKeyListener(self.KeyListener(self))
        tree.setFocus()

        #frame = self.create("com.sun.star.frame.Desktop").getCurrentFrame()
        #window = frame.getContainerWindow() if frame else None
        #self.dialog.createPeer(self.create("com.sun.star.awt.Toolkit"), window)

        parent = self.parent
        ps = parent.getPosSize()
        self.dialog.setPosSize(
            (ps.Width - self.WIDTH)/2, (ps.Height - self.HEIGHT)/2, 0, 0, 3)
        self.dialog.createPeer(parent.getToolkit(), parent)


class PythonScriptOrganizer(unohelper.Base, XJobExecutor):
    """ Alternative script organizer for Python scripting. """

    History = None    # URI of previous executed script

    def __init__(self, ctx):
        self.ctx = ctx
        self.doc = None
        self.doctitle = None
        self.allowmacroexecution = False
        self.user_sp = None
        self.share_sp = None
        self.document_sp = None

    def _get_active_doc_uri(self):
        """ Returns internal uri for the current document. """
        doc = self._get_desktop().getCurrentComponent()
        try:
            # script container is another document
            # (typically for database subdocuments)
            doc = doc.ScriptContainer
        except AttributeError:
            # some subdocuments don't support XScriptInvocationContext
            try:
                if doc.Parent:
                    doc = doc.Parent
            except AttributeError:
                pass
        uri = self._get_document_uri(doc)
        if uri:
            self.doctitle = doc.Title
            self.allowmacroexecution = doc.AllowMacroExecution
            return uri.rstrip("/")

    def _get_desktop(self):
        """ Returns desktop. """
        return self.ctx.getServiceManager().createInstanceWithContext(
            "com.sun.star.frame.Desktop", self.ctx)

    def _get_active_frame(self):
        """ Returns active frame. """
        frame = self._get_desktop().ActiveFrame
        if frame.ActiveFrame:
            # top window is a subdocument
            return frame.ActiveFrame
        else:
            return frame

    def _store_history(self, result):
        """ Store history. """
        self.__class__.History = result

    def _get_document_uri(self, doc):
        """ Get document transient URI. """
        tddc = self.ctx.getServiceManager().createInstanceWithContext(
            "com.sun.star.frame.TransientDocumentsDocumentContentFactory", self.ctx)
        try:
            content = tddc.createDocumentContent(doc)
            id = content.getIdentifier()
            return id.getContentIdentifier()
        except Exception:
            pass

    def execute(self, show_user=True, show_share=True, show_doc=True, show_icon=True):
        """ Show dialog. """
        PythonScriptProvider = pythonscript.PythonScriptProvider
        if show_user:
            self.user_sp = PythonScriptProvider(self.ctx, "user")
            self.user_sp.uno_packages_sp = PythonScriptProvider(
                self.ctx, "user:uno_packages")
        if show_share:
            self.share_sp = PythonScriptProvider(self.ctx, "share")
            self.share_sp.uno_packages_sp = PythonScriptProvider(
                self.ctx, "share:uno_packages")
        if show_doc:
            self.doc = self._get_active_doc_uri()
            if self.doc:
                self.document_sp = PythonScriptProvider(self.ctx, self.doc)
                self.document_sp.uno_packages_sp = None
                self.document_sp.title = self.doctitle
        dialog = OrganizerDialog(
            self.ctx,
            self.user_sp, self.share_sp, self.document_sp,
            self._get_active_frame().getContainerWindow(),
            show_icon)
        result, mode = dialog.execute(self.__class__.History)
        if result:
            self._store_history(result)
            self.run(result, mode)

    def _get_provider(self, uri):
        """ Find specific provider. """
        for p in uri.split("&"):
            if p.startswith("location="):
                try:
                    location = p[9:].split(':')
                    if len(location) > 1:
                        base_sp = getattr(self, location[0] + "_sp")
                        return getattr(base_sp, location[1] + "_sp")
                    else:
                        return getattr(self, location[0] + "_sp")
                except Exception:
                    pass

    def run(self, uri, mode):
        """ Run script specified by script uri.
        @mode: 1 = normal, 2 = debug"""

        try:
            if not uri.endswith("document") or self.allowmacroexecution:
                sp = self._get_provider(uri)
                if sp:
                    s = sp.getScript(uri)
                    if s:
                        if mode == 2:
                            import apso_debug
                            apso_debug.tempfiles = tempfiles
                            apso_debug.RR = RR
                            apso_debug.debug(uri, s, sp)
                        else:
                            s.invoke((), (), ())
                    else:
                        raise ErrorAsMessage(RR.resolvestring('msg29') + uri)
                else:
                    raise ErrorAsMessage(RR.resolvestring('msg30') + uri)
            else:
                MessageDialog(self.ctx,
                              self._get_active_frame().getContainerWindow(), type=WARNINGBOX,
                              title=PRODUCT, message=RR.resolvestring('msg16')).execute()
        except UNOException as e:
            if "SyntaxError" in str(e):
                try:
                    err = e.__context__
                    path = err.filename
                    if uri.endswith("document"):
                        path = tempfiles[path]
                except AttributeError:
                    urihelper = sp.provCtx.uriHelper
                    path, func = urihelper.getStorageURI(uri).split('$')
                    if path.startswith('vnd.sun.star.tdoc'):
                        path = tempfiles[path]
                    try:
                        ASTVisitFunctions(uno.fileUrlToSystemPath(path), func)
                    except SyntaxError as e:
                        err = e
                ekconfig = getEditorKickerConfig(self.ctx)
                n = SyntaxErrorMessageDialog(self.ctx,
                                             title=RR.resolvestring('msg01'),
                                             message=str(e),
                                             ekconfig=ekconfig).execute()
                if n:
                    open_script(ekconfig, path, err.lineno, err.offset)
            else:
                ErrorMessageDialog(self.ctx,
                                   title=RR.resolvestring('msg01'),
                                   message=str(e)).execute()
        except ErrorAsMessage as e:
            MessageDialog(self.ctx,
                          self._get_active_frame().getContainerWindow(),
                          title=RR.resolvestring('msg01'),
                          message=str(e)).execute()

    def trigger(self, arg):
        """ All scripts are shown. """
        try:
            if arg == "execute":
                loadResourceResolver(self.ctx)
                self.execute(True, True, True, True)
            elif arg.startswith('open::'):
                _, filename, lineno, offset = arg.split('::')
                ekconfig = getEditorKickerConfig(self.ctx)
                open_script(ekconfig, filename, int(lineno), int(offset))
        except Exception:
            errmsg = traceback.format_exc()
            msgbox(errmsg)


g_ImplementationHelper.addImplementation(
    PythonScriptOrganizer, "apso.python.script.organizer.impl", ())


# -----------------------------------------------------------
# EDITOR KICKER
# -----------------------------------------------------------

ImplementationName = "apso.EditorKickerOptionsPage"


class ButtonListener(unohelper.Base, XActionListener):
    def __init__(self, cast):
        self.cast = cast

    def disposing(self, ev):
        pass

    def actionPerformed(self, ev):
        cmd = str(ev.ActionCommand)
        if cmd == "ChooseEditor":
            ret = self.cast.chooseFile()
            if ret:
                path = uno.fileUrlToSystemPath(ret)
                ev.Source.getContext().getControl("tf_Editor").setText(path)


# main class
class OptionsDialogHandler(unohelper.Base, XContainerWindowEventHandler):
    def __init__(self, ctx):
        self.ctx = ctx
        loadResourceResolver(self.ctx)
        self.CfgNode = "/apso.EditorKicker"
        self.CfgNames = ("Editor", "Header", "Options")

    # XContainerWindowEventHandler
    def callHandlerMethod(self, window, eventObject, method):
        if method == "external_event":
            try:
                self._handleExternalEvent(window, eventObject)
            except Exception as e:
                print(e)
            return True

    # XContainerWindowEventHandler
    def getSupportedMethodNames(self):
        return ("external_event",)

    def _handleExternalEvent(self, window, evName):
        if evName == "ok":
            self._saveData(window)
        elif evName == "back":
            self._loadData(window, "back")
        elif evName == "initialize":
            self._loadData(window, "initialize")
        return True

    def _saveData(self, window):
        name = window.getModel().Name
        if name != "apso_EditorKicker":
            return
        editor = window.getControl("tf_Editor")
        options = window.getControl("tf_Options")
        header = window.getControl("tf_Header")
        settings = (editor.getText(), header.getText(), options.getText())
        self._configwriter(settings)

    def _loadData(self, window, evName):
        name = window.getModel().Name
        if name != "apso_EditorKicker":
            return
        if evName == "initialize":
            listener = ButtonListener(self)
            btn_Choose = window.getControl("btn_Choose")
            btn_Choose.ActionCommand = "ChooseEditor"
            btn_Choose.addActionListener(listener)
            for control in window.Controls:
                if not control.supportsService("com.sun.star.awt.UnoControlEdit"):
                    model = control.Model
                    model.Label = RR.resolvestring(model.Label)
        settings = self._configreader()
        if settings:
            tf_Editor = window.getControl("tf_Editor")
            tf_Options = window.getControl("tf_Options")
            tf_Header = window.getControl("tf_Header")
            tf_Editor.setText(settings["Editor"])
            tf_Options.setText(settings["Options"])
            tf_Header.setText(settings["Header"])
        return

    def _configreader(self):
        settings = {}
        try:
            reader = getConfigurationAccess(self.CfgNode)
            values = reader.getPropertyValues(self.CfgNames)
            for name, value in zip(self.CfgNames, values):
                settings[name] = value
        except Exception as e:
            raise e
        return settings

    def _configwriter(self, values):
        try:
            writer = getConfigurationAccess(self.CfgNode, True)
            values = writer.setPropertyValues(self.CfgNames, values)
            writer.commitChanges()
        except Exception as e:
            raise e

    def chooseFile(self):
        ret = self._getFileUrl()
        return ret

    def _getFileUrl(self):
        url = FileOpenDialog(self.ctx,
                             template=FILEOPEN_SIMPLE,
                             filters=((RR.resolvestring('msg07'), '*.*'),
                                      (RR.resolvestring('ek10'), '*.exe;*.bin;*.sh'))).execute()
        return url or False


g_ImplementationHelper.addImplementation(
    OptionsDialogHandler, ImplementationName, (ImplementationName,),)
