# -*- coding: utf-8 -*-

from com.sun.star.awt.WindowClass import TOP
from com.sun.star.awt.WindowAttribute import (BORDER, CLOSEABLE, MOVEABLE,
                                              SIZEABLE)
from com.sun.star.awt.PosSize import SIZE
from com.sun.star.awt.KeyModifier import MOD1, SHIFT
from com.sun.star.awt import (FontDescriptor, Rectangle, Selection,
                              WindowDescriptor, XKeyHandler, XTextListener,
                              XTopWindowListener, XWindowListener)
import theconsole
import pythonscript
import traceback
import threading
import sys
import pdb
import code
from com.sun.star.awt.MessageBoxType import (ERRORBOX, INFOBOX, MESSAGEBOX,
                                             QUERYBOX, WARNINGBOX)
from com.sun.star.uno import RuntimeException
from com.sun.star.script.provider import ScriptFrameworkErrorException
import uno
import unohelper
from com.sun.star.beans import PropertyValue


# ------------HELPERS----------------
def createUnoService(service, ctx=None, args=None):
    '''
    Instanciate a Uno service.

    @service: name of the service to be instanciated.
    @ctx: the context if required.
    @args: the arguments when needed.
    '''
    if not ctx:
        ctx = uno.getComponentContext()
    smgr = ctx.getServiceManager()
    if ctx and args:
        return smgr.createInstanceWithArgumentsAndContext(service, args, ctx)
    elif args:
        return smgr.createInstanceWithArguments(service, args)
    elif ctx:
        return smgr.createInstanceWithContext(service, ctx)
    else:
        return smgr.createInstance(service)


def getConfigurationAccess(nodevalue, updatable=False):
    '''
    Access configuration value.

    @nodevalue: the configuration key node as a string.
    @updatable: set True when accessor needs to modify the key value.
    '''
    cp = createUnoService("com.sun.star.configuration.ConfigurationProvider")
    node = PropertyValue("nodepath", 0, nodevalue, 0)
    if updatable:
        return cp.createInstanceWithArguments("com.sun.star.configuration.ConfigurationUpdateAccess", (node,))
    else:
        return cp.createInstanceWithArguments("com.sun.star.configuration.ConfigurationAccess", (node,))


def getProductName():
    '''
    Return the program name.
    '''
    key = "/org.openoffice.Setup/Product"
    reader = getConfigurationAccess(key)
    return reader.ooName


# ------------XRAY----------------


def xray(obj):
    '''
    Uno objects introspection tool.

    Xray is an Uno introspection tool created in basic by Bernard Marcelly.
    This function allows to call it from inside a python script.
    The tool must be installed first. Last version is available at
    http://www.openoffice.org/fr/Documentation/Basic.
    '''
    ctx = uno.getComponentContext()
    url = ("vnd.sun.star.script:XRayTool._Main.Xray?language=Basic&location=application")
    mspf = createUnoService(
        "com.sun.star.script.provider.MasterScriptProviderFactory", ctx)
    try:
        print('Loading Xray...')
        script = mspf.createScriptProvider('').getScript(url)
        script.invoke((obj,), (), ())
    except ScriptFrameworkErrorException:
        print('Fail loading Xray')
        msgbox('Xray is not installed.\nPlease visit:\n'
               'http://www.openoffice.org/fr/Documentation/Basic',
               'Error', 'error')


# ------------MRI----------------


def mri(target):
    '''
    Uno objects introspection tool.

    Mri is an Uno introspection tool created in python by Hanya.
    This function allows to call it from inside a python script.
    The tool must be installed first. Last version is available at
    https://github.com/hanya/MRI or at
    https://extensions.libreoffice.org/en/extensions/show/mri-uno-object-inspection-tool.
    '''
    try:
        print('Loading MRIself...')
        mri = createUnoService("mytools.Mri")
        mri.inspect(target)
    except (RuntimeException, AttributeError):
        print('Fail loading MRI')
        msgbox('MRI is not installed.\nPlease visit:\n'
               'http://extensions.services.openoffice.org',
               'Error', 'error')


# ------------MSGBOX----------------


def msgbox(message, title="Message", boxtype='message', buttons=1, win=None):
    '''
    Simple message box.

    Like the oobasic build-in function msgbox,
    but simplified as only intended for quick debugging.
    Signature: msgbox(message, title='Message', boxtype='message', buttons=1, win=None).
    '''
    types = {'message': MESSAGEBOX, 'info': INFOBOX, 'error': ERRORBOX,
             'warning': WARNINGBOX, 'query': QUERYBOX}
    tk = createUnoService("com.sun.star.awt.Toolkit")
    if not win:
        desktop = createUnoService("com.sun.star.frame.Desktop")
        frame = desktop.ActiveFrame
        if frame.ActiveFrame:
            # top window is a subdocument
            frame = frame.ActiveFrame
        win = frame.ComponentWindow
    box = tk.createMessageBox(win, types[boxtype], buttons, title, message)
    return box.execute()


# ------------CONSOLE----------------


try:
    import queue
except ImportError:
    import Queue as queue


if sys.version_info < (3, ):
    reload(sys)
    sys.setdefaultencoding(sys.getfilesystemencoding())

EOT = b'\x04'


class UnoScriptImporter(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.providers = self._load_providers()
        self.nodes = {}

    def _load_providers(self):
        p = {}
        locations = [u'user', u'user:uno_packages',
                     u'share', u'share:uno_packages']
        for location in locations:
            ext = ""
            if location.endswith('uno_packages'):
                ext = ".oxt"
            p[location] = (pythonscript.PythonScriptProvider(
                self.ctx, location), ext)
        # FIXME: check if fonctional from base subdocuments
        try:
            doc = XSCRIPTCONTEXT.getDocument()
            if doc.ScriptContainer:
                p['document'] = (
                    pythonscript.PythonScriptProvider(self.ctx, doc), "")
        except (AttributeError, NameError):
            pass
        return p

    def _find_module(self, name, path):
        # print('---_find_module---')
        if path:
            node = path[0]
            if node in self.nodes:
                return self._search_node(self.nodes[node], name)
            else:
                return False
        else:
            for prov in self.providers:
                sp, ext = self.providers[prov]
                if self._search_node(sp, name, ext):
                    self.location = prov
                    return True
        return False

    def _search_node(self, node, name, ext=''):
        # print('---_search_node---')
        for child in node.getChildNodes():
            if child.name == uno.systemPathToFileUrl(name+ext):
                self.nodes[self.fullname] = child
                return True
        return False

    def find_module(self, fullname, path=None):
        # print('_____FIND_MODULE_____')
        # print('fullname: ' + fullname)
        if fullname in ('com',):
            return None
        self.fullname = fullname
        name = fullname.rsplit('.', 1)[-1]
        if self._find_module(name, path):
            return self
        return None

    def _module_from_node(self, node):
        import imp
        mod = imp.new_module(node.name)
        for child in node.getChildNodes():
            try:
                if isinstance(child, pythonscript.FileBrowseNode):
                    setattr(mod, child.name,
                            node.provCtx.getModuleByUrl(child.uri))
                else:
                    setattr(mod, child.name, self._module_from_node(child))
            # import machinery could find a submodule that is
            # not visible from the PythonScriptProvider
            except ImportError:
                print('unexpected error while loading module <{}>'.format(child.name))
                # traceback.print_exc()
        return mod

    def load_module(self, fullname):
        # print('_____LOAD_MODULE_____')
        # print('fullname: ' + fullname)
        # print('self.nodes: ' + str(self.nodes))
        node = self.nodes[fullname]
        if isinstance(node, pythonscript.DirBrowseNode):
            mod = self._module_from_node(node)
            mod.__file__ = '<{}>'.format(self.location)
            mod.__path__ = [fullname]
            mod.__package__ = fullname
        else:
            mod = node.provCtx.getModuleByUrl(node.uri)
        try:
            parent = fullname.rsplit('.', 1)[-2]
            mod.__package__ = parent
        except IndexError:
            pass
        # name = fullname.rsplit('.', 1)[-1]
        mod.__name__ = fullname
        mod.__loader__ = self
        sys.modules[fullname] = mod
        return mod


class ConsoleWindow(object):
    """Interactive console dialog.

    Instantiate with corresponding keyword parameters to override
    default values: ConsoleWindow(BACKGROUND=0x0, FOREGROUND=0xFFFFFF)>
    """

    FONT = "DejaVu Sans Mono"
    BACKGROUND = 0xFDF6E3
    FOREGROUND = 0x657B83
    MARGIN = 3
    BUTTON_WIDTH = 80
    BUTTON_HEIGHT = 26
    EDIT_HEIGHT = 300
    WIDTH = 600
    PS1 = '>>> '
    PS2 = '... '
    NBTAB = 4
    HEIGHT = EDIT_HEIGHT + MARGIN * 3

    def __init__(self, **kwargs):
        self.banner = None
        for key in kwargs:
            setattr(self, key, kwargs[key])
        if 'ctx' not in kwargs:
            self.ctx = uno.getComponentContext()
        self.smgr = self.ctx.getServiceManager()
        self.setparent = True
        if kwargs.get('parent') is None:
            self.parent = self.getparent()
            self.setparent = False
        self.loc.update(xray=xray, mri=mri, msgbox=msgbox)
        self.title = "APSO console"
        self.edit_name = "console"
        self.product = getProductName()
        self.dialog = None
        self.tk = self.create("com.sun.star.awt.Toolkit")
        self.end = 0
        self.more = 0
        self.history = theconsole.history
        self.historycursor = len(self.history)

        # create import hook for macros in AOO/LO containers
        self.importer = UnoScriptImporter(self.ctx)
        sys.meta_path.append(self.importer)
        # redirect output to self
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def create(self, name, arguments=None):
        """ Create service instance. """
        if arguments:
            return self.smgr.createInstanceWithArgumentsAndContext(name, arguments, self.ctx)
        else:
            return self.smgr.createInstanceWithContext(name, self.ctx)

    def execute(self):
        '''Create dialog and manage context'''
        try:
            self._init()
            self.dialog.setVisible(True)
            proc = threading.Thread(target=_interact,
                                    args=(self.inqueue, self.exitevent, self.PS1, self.PS2, self.product, self.loc))
            proc.start()
            # self.dialog.execute()
            # self.dialog.dispose()
        except Exception:
            msgbox(traceback.format_exc())

    def enddialog(self):
        """Terminate dialog"""
        self.dialog.setVisible(False)
        self.dialog.dispose()
        # clean up everything
        theconsole.console = None
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        self.inqueue.put(EOT)
        self.tk.removeKeyHandler(self.keyhandler)
        sys.meta_path.remove(self.importer)
        print('console closed')

    def create_control(self, win, name, type_, pos, size, prop_names, prop_values):
        """ Create and insert control. """
        model = self.create("com.sun.star.awt.UnoControl{}Model".format(type_))
        if prop_names and prop_values:
            model.setPropertyValues(prop_names, prop_values)
        ctrl = self.create(model.DefaultControl)
        ctrl.setModel(model)
        ctrl.createPeer(win.Toolkit, win)
        ctrl.setPosSize(pos[0], pos[1], size[0], size[1], 15)
        return ctrl

    def create_dialog(self, title, size=None, parent=None):
        """ Create modeless dialog. """
        rect = Rectangle()
        rect.Width, rect.Height = size
        ps = self.parent.getPosSize()
        rect.X, rect.Y = (ps.X + ps.Width - self.WIDTH), ps.Y

        desc = WindowDescriptor()
        desc.Type = TOP
        desc.WindowServiceName = "dialog"
        if self.setparent:
            desc.Parent = self.parent
        desc.ParentIndex = -1
        desc.Bounds = rect
        desc.WindowAttributes = MOVEABLE | SIZEABLE | CLOSEABLE | BORDER

        dialog = self.tk.createWindow(desc)
        dialog.setTitle(title)

        self.dialog = dialog

    def create_edit(self, name, pos, size, prop_names=None, prop_values=None):
        """ Create and add new edit control. """
        self.edit = self.create_control(
            self.dialog, name, "Edit", pos, size, prop_names, prop_values)

    def getparent(self):
        '''Returns parent frame'''
        desktop = self.create("com.sun.star.frame.Desktop")
        return desktop.CurrentFrame.ContainerWindow

    class ListenerBase(unohelper.Base):
        def __init__(self, act):
            self.act = act

        def disposing(self, source):
            self.act = None

    class WindowListener(ListenerBase, XWindowListener):
        def windowResized(self, e):
            size = e.Source.Size
            margin = self.act.MARGIN
            self.act.edit.setPosSize(
                0, 0, size.Width - margin*2, size.Height - margin*3, SIZE)

        # unused events
        def windowMoved(self, e):
            pass

        def windowShown(self, e):
            pass

        def windowHidden(self, e):
            pass

    class TopWindowListener(ListenerBase, XTopWindowListener):
        def windowClosing(self, e):
            self.act.enddialog()

        def windowDeactivated(self, e):
            self.act.tk.removeKeyHandler(self.act.keyhandler)

        def windowActivated(self, e):
            self.act.tk.addKeyHandler(self.act.keyhandler)

        # unused events
        def windowOpened(self, e):
            pass

        def windowClosed(self, e):
            pass

        def windowMinimized(self, e):
            pass

        def windowNormalized(self, e):
            pass

    class TextListener(ListenerBase, XTextListener):
        def textChanged(self, ev):
            self.act.end = len(ev.Source.Text)

    class KeyHandler(ListenerBase, XKeyHandler):
        def keyPressed(self, ev):
            try:
                return getattr(self.act, "onkey_"+str(ev.KeyCode))(ev.Modifiers)
            except AttributeError:
                return 0

        def keyReleased(self, ev):
            return 0

    def onkey_514(self, modifiers):
        '''Catch ctrl+C keyboard entry'''
        if (modifiers & MOD1):
            sel = self.edit.Selection
            if sel.Min == sel.Max:
                self._keyboardinterrupt()
                return 1
        return 0

    def onkey_515(self, modifiers):
        '''Catch ctrl+D keyboard entry'''
        if (modifiers & MOD1):
            try:
                self.enddialog()
                return 1
            except Exception:
                traceback.print_exc()
                self._write(self.PS1)
                return 1
        return 0

    def onkey_537(self, modifiers):
        '''Catch ctrl+Z keyboard entry'''
        if (modifiers & MOD1):
            try:
                self.enddialog()
                return 1
            except Exception:
                traceback.print_exc()
                self._write(self.PS1)
                return 1
        return 0

    def onkey_1024(self, modifiers):
        '''Catch DOWN keyboard entry'''
        try:
            line = self._readline()
            if self.historycursor < len(self.history)-1:
                self.historycursor += 1
                self._write(self.history[self.historycursor],
                            (self.end-len(line)+1, self.end))
            else:
                self.historycursor = len(self.history)
                self._write("", (self.end-len(line)+1, self.end))
            self.gotoendofinput()
            return 1
        except Exception:
            self.inqueue.put(traceback.format_exc())

    def onkey_1025(self, modifiers):
        '''Catch UP keyboard entry'''
        try:
            line = self._readline()
            if self.historycursor > 0:
                self.historycursor -= 1
                self._write(self.history[self.historycursor],
                            (self.end-len(line)+1, self.end))
            self.gotoendofinput()
            return 1
        except Exception:
            self.inqueue.put(traceback.format_exc())

    def onkey_1028(self, modifiers):
        '''Catch HOME keyboard entry'''
        if not (modifiers & SHIFT):
            self.gotostartofinput()
            return 1
        return 0

    def onkey_1029(self, modifiers):
        '''Catch END keyboard entry'''
        if not (modifiers & SHIFT):
            self.gotoendofinput()
            return 1
        return 0

    def onkey_1280(self, modifiers):
        '''Catch RETURN keyboard entry'''
        try:
            line = self._readline()
            cmd = line.rstrip('\n')
            if cmd:
                if not self.history or cmd != self.history[-1]:
                    self.history.append(cmd)
                self.historycursor = len(self.history)
            if self.edit.Selection.Max >= (self.end-len(self.prompt+line)):
                if cmd in ("clear", "clear()"):
                    self.clear()
                else:
                    self._write("\n")
                    self.prompt = ""
                    self.inqueue.put(line)
            self.gotoendofinput()
            return 1
        except Exception:
            self.inqueue.put(traceback.format_exc())

    def onkey_1281(self, modifiers):  # ESCAPE
        '''Catch ESCAPE keyboard entry'''
        return 1

    def onkey_1282(self, modifiers):  # TAB
        '''Catch TAB keyboard entry'''
        if not modifiers:
            self._write(' ' * self.NBTAB)
            return 1
        return 0

    def _keyboardinterrupt(self):
        '''Send KeyboardInterror exception.
        This exception will not allways work as expected'''
        self.inqueue.put(KeyboardInterrupt)

    def gotoendofinput(self):
        '''Send visible cursor to end of input line'''
        self.edit.setSelection(Selection(self.end, self.end))

    def gotostartofinput(self):
        '''Send visible cursor to start of input line'''
        line = self._readline()
        pos = self.end - len(line) + 1
        self.edit.setSelection(Selection(pos, pos))

    def clear(self):
        '''Clear edit area'''
        self.edit.Text = self.prompt

    def _init(self):
        margin = self.MARGIN
        font = FontDescriptor()
        font.Name = self.FONT
        self.create_dialog(self.title, size=(self.WIDTH, self.HEIGHT))
        self.dialog.addWindowListener(self.WindowListener(self))
        self.dialog.addTopWindowListener(self.TopWindowListener(self))
        self.create_edit(self.edit_name,
                         pos=(margin, margin * 2),
                         size=(self.WIDTH - margin * 2, self.EDIT_HEIGHT),
                         prop_names=("AutoVScroll", "BackgroundColor", "FontDescriptor", "HideInactiveSelection",
                                     "MultiLine", "TextColor"),
                         prop_values=(True, self.BACKGROUND, font, True, True, self.FOREGROUND))

        self.keyhandler = self.KeyHandler(self)
        self.edit.addTextListener(self.TextListener(self))
        self.edit.setFocus()

    def flush(self):
        '''Does it need to be implemented?'''
        pass

    def write(self, data):
        '''Implements sys.stdout/stderr write method'''
        try:
            if self.exitevent.is_set():
                self.enddialog()
                return
            self.prompt = data.split("\n")[-1]
            self._write(data)
        except Exception:
            msgbox("Error on ConsoleWindow.write:\n" + traceback.format_exc())

    def _write(self, data, sel=None):
        '''Append data to edit control text'''
        if not sel:
            sel = (self.end, self.end)
        self.edit.insertText(Selection(*sel), data)

    def _readline(self):
        '''Returns input text'''
        lines = self.edit.Text.rsplit("\n", 1)
        line = lines[-1] + '\n'
        return line[len(self.prompt):]


class Interact(code.InteractiveConsole):
    def __init__(self, inqueue, exitevent, ps1, ps2, product, loc=None):
        code.InteractiveConsole.__init__(self, loc)
        self.inqueue = inqueue
        self.exitevent = exitevent
        self.ps1, self.ps2 = ps1, ps2
        self.product = product
        self.keep_prompting = True
        self.stdin = sys.stdin
        # sys.stdin = self

    def readline(self):
        '''Implements sys.stdin readline method'''
        rl = self.inqueue.get()
        if rl == KeyboardInterrupt:
            raise KeyboardInterrupt()
        if rl == EOT:
            self.keep_prompting = False
        return rl

    def interact(self, banner=None):
        '''Overwrite default interact method'''
        cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
        if banner is None:
            self.write("APSO python console [{}]\n{}\n{}\n".format(
                self.product, sys.version, cprt))
        elif banner:
            self.write("%s\n" % str(banner))
        more = 0
        try:
            while self.keep_prompting:
                # sys.stdin is sometime lost in OpenOffice and must be repeted
                sys.stdin = self
                try:
                    if more:
                        prompt = self.ps2
                    else:
                        prompt = self.ps1
                    line = self.raw_input(prompt)
                    more = self.push(str(line))
                except KeyboardInterrupt:
                    self.write("\nKeyboardInterrupt\n")
                    self.resetbuffer()
                    more = 0
                except SystemExit:
                    self.exitevent.set()
                except Exception:
                    print('INTERACT\n')
                    traceback.print_exc()
                    self.resetbuffer()
                    more = 0
        finally:
            sys.stdin = self.stdin


def _interact(*args):
    iconsole = Interact(*args)
    iconsole.interact()
    # msgbox('stop')


def console(**kwargs):
    '''
    Launch the "python interpreter" gui.

    Keyword arguments are:
    - 'loc': for passing caller's locales and/or globals to the console context
    - any constructor constant (BACKGROUND, FOREGROUND...) to tweak the console aspect.

    Examples:
    - console()  # defaut constructor)
    - console(loc=locals())
    - console(BACKGROUND=0x0, FOREGROUND=0xFFFFFF)

    More infos: https://extensions.libreoffice.org/en/extensions/show/apso-alternative-script-organizer-for-python.
    '''

    try:
        if theconsole.console:
            theconsole.tofront()
            # hack a little bug within OpenOffice
            sys.stdout = sys.stderr = theconsole.console
            return
        loc = kwargs.setdefault('loc', {})
        loc.update(pdb=pdb)
        kwargs.update(inqueue=queue.Queue(), exitevent=threading.Event())
        console_ = ConsoleWindow(**kwargs)
        theconsole.console = console_
        console_.execute()
        return console_
    except Exception:
        msgbox(traceback.format_exc())
        return None
