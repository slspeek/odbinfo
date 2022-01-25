# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import bdb
import inspect
import linecache
import pprint
# python imports
import sys
import threading
import traceback

from pythonscript import PythonScriptProvider

try:
    # python 3
    import queue
    from reprlib import Repr

    # unicode = str
except ImportError:
    # python 2
    import Queue as queue
    from repr import Repr
    chr = unichr

import theconsole
# uno imports
import uno
import unohelper
from apso_utils import (console, getConfigurationAccess, getProductName,
                        msgbox, xray)
from com.sun.star.awt import (Rectangle, WindowDescriptor, XActionListener,
                              XMouseMotionListener, XTopWindowListener,
                              XWindowListener)
from com.sun.star.awt.ImagePosition import AboveCenter
from com.sun.star.awt.PosSize import HEIGHT as PS_HEIGHT
from com.sun.star.awt.PosSize import POSSIZE as PS_POSSIZE
from com.sun.star.awt.PosSize import WIDTH as PS_WIDTH
from com.sun.star.awt.PosSize import X as PS_X
from com.sun.star.awt.PosSize import Y as PS_Y
from com.sun.star.awt.SystemPointer import HSPLIT, VSPLIT
from com.sun.star.awt.WindowAttribute import (BORDER, CLOSEABLE, MOVEABLE,
                                              SHOW, SIZEABLE)
from com.sun.star.awt.WindowClass import SIMPLE

# custom repr() method
aRepr = Repr()
aRepr.maxother = 100
aRepr.maxstring = 100
repr = aRepr.repr

'''
TODO:
OK - open console with current locales and globals
OK - terminer test sur queue class
OK - test formatting with lambda functions
OK- show doc name instead of temp file path for embedded scripts
'''


tempfiles = {}
RR = None

MARGIN = 4
WIDTH = 1000
HEIGHT = 800
BTN_WIDTH = 80
BTN_HEIGHT = 45
LABEL_HEIGHT = 20
CODE_TOP = BTN_HEIGHT + LABEL_HEIGHT + 2*MARGIN
SPLITTER = 3
SPLITTER_Y = 620
FOOTER_HEIGHT = 150
MIN_X = MARGIN
MIN_Y = CODE_TOP
MAX_Y = LABEL_HEIGHT + MARGIN

UNKNOWN = '[unreadable]'
CODE_COLOR = 0x202020    # 0x177117
SPLITTER_COLOR = -1    # 0xc4cacd
ENCODING = sys.getfilesystemencoding()


class Restart(Exception):
    """Exception to give up completely"""


class MouseMotionListener(unohelper.Base, XMouseMotionListener):
    def __init__(self, topwindow, controls, orient):
        self.topwindow = topwindow
        self.controls = controls
        self._mouse_dragged = {'H': self._hori_dragged,
                               'V': self._vert_dragged}[orient]

    # XMouseMotionListener
    # XEventListener
    def disposing(self, source):
        pass

    def mouseDragged(self, e):
        try:
            self._mouse_dragged(e)
        except Exception:
            traceback.print_exc()

    def mouseMoved(self, e):
        pass

    # custom functions
    def _vert_dragged(self, e):
        height = self.topwindow.PosSize.Height
        e.Source.setPosSize(0, e.Source.PosSize.Y + e.Y, 0, 0, PS_Y)
        if e.Source.PosSize.Y > height - MAX_Y:
            e.Source.removeMouseMotionListener(self)
            e.Source.setPosSize(0, height - MAX_Y, 0, 0, PS_Y)
            e.Source.addMouseMotionListener(self)
        elif e.Source.PosSize.Y < MIN_Y:
            e.Source.removeMouseMotionListener(self)
            e.Source.setPosSize(0, MIN_Y, 0, 0, PS_Y)
            e.Source.addMouseMotionListener(self)
        Y = e.Source.PosSize.Y
        footer_top = Y + SPLITTER + MARGIN + LABEL_HEIGHT
        self.controls['lb_code'].setPosSize(
            0, 0, 0, Y - (CODE_TOP + SPLITTER), PS_HEIGHT)
        self.controls['ft_output'].setPosSize(
            0, Y + SPLITTER + MARGIN, 0, 0, PS_Y)
        self.controls['ft_scope'].setPosSize(
            0, Y + SPLITTER + MARGIN, 0, 0, PS_Y)
        self.controls['lb_output'].setPosSize(
            0, footer_top, 0, height - (footer_top + MARGIN), PS_Y | PS_HEIGHT)
        self.controls['lb_scope'].setPosSize(
            0, footer_top, 0,  height - (footer_top + MARGIN), PS_Y | PS_HEIGHT)
        self.controls['lb_scope'].setPosSize(
            0, footer_top, 0,  height - (footer_top + MARGIN), PS_Y | PS_HEIGHT)
        self.controls['hsplitter'].setPosSize(
            0, Y, 0, height - Y, PS_Y | PS_HEIGHT)

    def _hori_dragged(self, e):
        e.Source.setPosSize(e.Source.PosSize.X + e.X, 0, 0, 0, PS_X)
        width = self.topwindow.PosSize.Width
        max_X = width - MIN_X
        if e.Source.PosSize.X > max_X:
            e.Source.removeMouseMotionListener(self)
            e.Source.setPosSize(max_X, 0, 0, 0, PS_X)
            e.Source.addMouseMotionListener(self)
        elif e.Source.PosSize.X < MIN_X:
            e.Source.removeMouseMotionListener(self)
            e.Source.setPosSize(MIN_X, 0, 0, 0, PS_X)
            e.Source.addMouseMotionListener(self)
        X = e.Source.PosSize.X
        self.controls['ft_output'].setPosSize(
            0, 0, X - 1.5*MARGIN, 0, PS_WIDTH)
        self.controls['lb_output'].setPosSize(
            0, 0, X - 1.5*MARGIN, 0, PS_WIDTH)
        self.controls['ft_scope'].setPosSize(X + SPLITTER + MARGIN/2 + 1, 0,
                                             width - (X + SPLITTER + MARGIN*1.5), 0, PS_X | PS_WIDTH)
        self.controls['lb_scope'].setPosSize(X + SPLITTER + MARGIN/2, 0,
                                             width - (X + SPLITTER + MARGIN*1.5 - 1), 0, PS_X | PS_WIDTH)


class Debugger(unohelper.Base, XActionListener, XWindowListener, XTopWindowListener):
    def __init__(self, uri, script, scriptprovider):
        self.scriptprovider = scriptprovider
        self.scripturi = uri
        self.func = script.func
        self.topfilename = self.func.__code__.co_filename
        self.ctx = uno.getComponentContext()
        self.smgr = self.ctx.ServiceManager
        self.desktop = self.create("com.sun.star.frame.Desktop")
        self.toolkit = self.create("com.sun.star.awt.Toolkit")
        self.inqueue = queue.Queue()
        self.controls = {}
        self.currentcomponent = ''
        self.create_ui()
        self.component = None
        self.getunotype = self.create(
            "com.sun.star.reflection.CoreReflection").getType
        self.inspector = None
        try:
            # fix if mri is not installed
            mri = self.create("mytools.Mri")
            self.inspector = mri.inspect
        except Exception:
            self.inspector = xray

    def create(self, name, arguments=None):
        """ Create service instance. """
        if arguments:
            return self.smgr.createInstanceWithArgumentsAndContext(name, arguments, self.ctx)
        else:
            return self.smgr.createInstanceWithContext(name, self.ctx)

    def executedebug(self):
        if self.scripturi.endswith("document"):
            self.component = self.desktop.CurrentComponent
            if self.component.hasLocation():
                self.currentcomponent = uno.fileUrlToSystemPath(
                    self.component.Location)
            else:
                self.currentcomponent = self.component.Title
        self.topwindow.setVisible(True)
        try:
            apsodb = Apsodb(self)
            apsodb.start()
            # self.topwindow.execute()
            self.topwindow.setVisible(True)
        finally:
            # msgbox(traceback.format_exc())
            sys.settrace(None)

    def gotoline(self, no):
        self.ui_code.selectItemPos(no, True)

    def setfilename(self, name):
        self.ui_filename.setText(name)

    def writeoutput(self, output, textcolor=-1):
        self.ui_output.Model.TextColor = textcolor
        self.ui_output.Model.removeAllItems()
        if isinstance(output, (tuple, list)):
            self.ui_output.addItems(tuple(output), 0)
            self.ui_output.selectItemPos(len(output)-1, True)
        else:
            self.ui_output.addItems((output,), 0)

    def create_ui(self):
        # MAIN WINDOW
        self.topwindow = self.create_window(SIMPLE, "dialog",
                                            Rectangle(300, 50, WIDTH, HEIGHT), BORDER | MOVEABLE | SIZEABLE | CLOSEABLE)
        self.frame = self.create("com.sun.star.frame.Frame")
        self.frame.initialize(self.topwindow)
        # # do not register frame at desktop,
        # # it will interfer with the XSCRIPTCONTEXT variable
        # frames = self.desktop.getFrames()
        # frames.append(self.frame)

        fontname, fontheight = self.getfont()

        # BUTTONS
        product = getProductName()
        if product.startswith('LibreOffice'):
            imagepath = "private:graphicrepository/cmd/sc_{}.png"
        else:
            imagepath = "private:graphicrepository/res/commandimagelist/sc_{}.png"
        buttons = eval(RR.resolvestring('db_buttons'))
        for n, (name, label, icon, helptext) in enumerate(buttons):
            X = MARGIN + (MARGIN + BTN_WIDTH)*n
            imageurl = imagepath.format(icon)
            self.create_control('btn' + name, 'Button', (X, MARGIN, BTN_WIDTH, BTN_HEIGHT),
                                ('HelpText', 'ImagePosition', 'ImageURL', 'Label'),
                                (helptext, AboveCenter, imageurl, label), name)
        # CODE VIEWER
        self.create_control('ft_code', 'FixedText',
                            (MARGIN + 1, CODE_TOP - LABEL_HEIGHT,
                             WIDTH - 2*MARGIN - 1, LABEL_HEIGHT),
                            ('Label',), ('Label 1',))
        self.create_control('lb_code', 'ListBox', (MARGIN, CODE_TOP, WIDTH-2*MARGIN, SPLITTER_Y - (CODE_TOP + MARGIN)),
                            ('FontHeight', 'FontName', 'TextColor'), (fontheight, fontname, CODE_COLOR), 'generic')
        # STACK VIEWER
        footer_width = (WIDTH - 3*MARGIN - SPLITTER)/2
        footer_top = SPLITTER_Y + SPLITTER + LABEL_HEIGHT + MARGIN
        self.create_control('ft_output', 'FixedText',
                            (MARGIN + 1, SPLITTER_Y + SPLITTER +
                             MARGIN, footer_width - 1, LABEL_HEIGHT),
                            ('Label',), (RR.resolvestring('lbl01'),))
        self.create_control('lb_output', 'ListBox', (MARGIN, footer_top, footer_width, FOOTER_HEIGHT),
                            ('AutoVScroll', 'BackgroundColor', 'FontHeight',
                             'FontName', 'HScroll', 'MultiLine'),
                            (True, 0xfdf6e3, fontheight, fontname, True, True), 'generic')
        # SCOPE VIEWER
        self.create_control('ft_scope', 'FixedText',
                            (2*MARGIN + footer_width + SPLITTER + 1, SPLITTER_Y +
                             SPLITTER + MARGIN, footer_width - 1, LABEL_HEIGHT),
                            ('Label',), (RR.resolvestring('lbl02'),))
        self.create_control('lb_scope', 'ListBox',
                            (2*MARGIN + footer_width + SPLITTER,
                             footer_top, footer_width, FOOTER_HEIGHT),
                            ('BackgroundColor', 'FontHeight', 'FontName'), (0xe3e3ff, fontheight, fontname), 'generic')
        # VERTICAL SPLITTER
        self.vsplitter = self.create_window(SIMPLE, "splitter",
                                            Rectangle(0, SPLITTER_Y,
                                                      WIDTH, SPLITTER),
                                            SHOW, self.topwindow)
        self.vsplitter.setBackground(SPLITTER_COLOR)
        pointer = self.create("com.sun.star.awt.Pointer")
        pointer.setType(VSPLIT)
        self.vsplitter.setPointer(pointer)
        self.vsplitter.addMouseMotionListener(
            MouseMotionListener(self.topwindow, self.controls, 'V'))

        # HORIZONTAL SPLITTER
        self.hsplitter = self.create_window(SIMPLE, "splitter",
                                            Rectangle(
                                                (WIDTH - SPLITTER)/2, SPLITTER_Y, SPLITTER, HEIGHT - SPLITTER_Y),
                                            SHOW, self.topwindow)
        self.hsplitter.setBackground(SPLITTER_COLOR)
        pointer = self.create("com.sun.star.awt.Pointer")
        pointer.setType(HSPLIT)
        self.hsplitter.setPointer(pointer)
        self.hsplitter.addMouseMotionListener(
            MouseMotionListener(self.topwindow, self.controls, 'H'))

        # STARTING GUI
        self.controls.update(vsplitter=self.vsplitter,
                             hsplitter=self.hsplitter)
        self.topwindow.addWindowListener(self)
        self.topwindow.addTopWindowListener(self)

        self.topwindow.setTitle("APSO_DEBUG")
        self.ui_code = self.controls['lb_code']
        self.ui_output = self.controls['lb_output']
        self.ui_filename = self.controls['ft_code']
        self.ui_scope = self.controls['lb_scope']

    def getfont(self):
        key = "/org.openoffice.Office.Common/Font/SourceViewFont"
        reader = getConfigurationAccess(key)
        fontname = reader.FontName
        if not fontname:
            fontname = "DejaVu Sans Mono"
        fontheight = reader.FontHeight
        return fontname, fontheight

    def create_window(self, wtype, service, rect, attributes=SHOW | BORDER, parent=None):
        descriptor = WindowDescriptor(
            wtype, service, parent, -1, rect, attributes)
        win = self.toolkit.createWindow(descriptor)
        return win

    def create_control(self, name, type_, possize=None, prop_names=None, prop_values=None, action=''):
        type_ = "com.sun.star.awt.UnoControl{}Model".format(type_)
        model = self.create(type_)
        if prop_names and prop_values:
            model.setPropertyValues(prop_names, prop_values)
        ctrl = self.create(model.DefaultControl)
        ctrl.setModel(model)
        ctrl.createPeer(self.toolkit, self.topwindow)
        if possize:
            ctrl.setPosSize(possize[0], possize[1],
                            possize[2], possize[3], PS_POSSIZE)
        if action == 'generic':
            ctrl.addActionListener(self)
        elif action:
            ctrl.setActionCommand(action.lower())
            ctrl.addActionListener(self)
        self.controls[name] = ctrl

    # # LISTENERS
    # XEventListener
    def disposing(self, source):
        # print("disposing")
        pass

    # XActionListener
    def actionPerformed(self, event):
        action = event.ActionCommand
        source = event.Source
        if source == self.controls['lb_code']:
            lineno = source.SelectedItemPos + 1
            self.inqueue.put(('jump', lineno))
        elif source == self.controls['lb_output']:
            if self.ui_output.Model.TextColor == -1:
                lineno = source.SelectedItemPos
                self.inqueue.put(('loadframe', lineno))
        elif source == self.controls['lb_scope']:
            lineno = source.SelectedItemPos
            var, value = self.ui_scope.Items[lineno].split(' : ')
            if value == UNKNOWN:
                msgbox('unknown', win=self.topwindow)
            else:
                var = var.lstrip('*')
                varvalue = self.localscope[var]
                try:
                    # -> raise error if varvalue can be inspected
                    self.getunotype(varvalue)
                    self.inspector(varvalue)
                except Exception:
                    msgbox("python object: {}\n---\n{}".format(type(varvalue),
                           pprint.pformat(varvalue)), win=self.topwindow)
        elif action == 'quit':
            self.inqueue.put((action, 0))
            # close console if opened from debugger
            if theconsole.console and theconsole.console.parent == self.topwindow:
                theconsole.close()
            self.vsplitter.dispose()
            self.hsplitter.dispose()
            self.topwindow.setVisible(False)
            self.topwindow.dispose()
            # self.topwindow.endExecute()
        elif action == 'restart':
            try:
                if self.scripturi.endswith("document"):
                    sfa = self.scriptprovider.provCtx.sfa
                    tempfile = tempfiles[self.topfilename]
                    sfa.copy(tempfile, self.topfilename)
                    self.scriptprovider = PythonScriptProvider(
                        self.ctx, self.component)
                script = self.scriptprovider.getScript(self.scripturi)
                self.func = script.func
                sys.settrace(None)
                self.controls['btnNEXT'].setFocus()
                self.inqueue = queue.Queue()
                apsodb = Apsodb(self)
                apsodb.start()
            except Exception:
                msgbox(traceback.format_exc(), win=self.topwindow)
        else:
            self.inqueue.put((action, 0))

    # XTopWindowListener
    def windowClosing(self, e):
        if theconsole.console and theconsole.console.parent == self.topwindow:
            theconsole.close()
        self.vsplitter.dispose()
        self.hsplitter.dispose()

    def windowDeactivated(self, e):
        pass

    def windowActivated(self, e):
        pass

    def windowOpened(self, e):
        pass

    def windowClosed(self, e):
        pass

    def windowMinimized(self, e):
        pass

    def windowNormalized(self, e):
        pass

    # XWindowListener
    def windowResized(self, event):
        try:
            ps_base = event.Source.PosSize
            footer_width = self.controls['lb_scope'].Size.Width
            footer_height = self.controls['lb_output'].Size.Height
            footer_top = ps_base.Height - (footer_height + MARGIN)
            code_height = footer_top - \
                (CODE_TOP + SPLITTER + LABEL_HEIGHT + 2*MARGIN)
            if ps_base.Height > (CODE_TOP + footer_height + SPLITTER + LABEL_HEIGHT + 2*MARGIN):
                self.controls['ft_output'].setPosSize(
                    0, footer_top - LABEL_HEIGHT, 0, 0, PS_Y)
                self.controls['lb_output'].setPosSize(
                    0, footer_top, 0, 0, PS_Y)
                self.controls['lb_scope'].setPosSize(0, footer_top, 0, 0, PS_Y)
                self.controls['ft_scope'].setPosSize(
                    0, footer_top - LABEL_HEIGHT, 0, 0, PS_Y)
                self.vsplitter.setPosSize(
                    0, footer_top - (LABEL_HEIGHT + SPLITTER + MARGIN), 0, 0, PS_Y)
                self.hsplitter.setPosSize(
                    0, footer_top - (LABEL_HEIGHT + SPLITTER + MARGIN), 0, 0, PS_Y)
                self.controls['lb_code'].setPosSize(
                    0, 0, 0, code_height, PS_HEIGHT)
            if ps_base.Width > footer_width + SPLITTER + 2*MARGIN:
                self.controls['ft_output'].setPosSize(0, 0,
                                                      ps_base.Width -
                                                      (footer_width +
                                                       SPLITTER + 3*MARGIN - 1),
                                                      0, PS_WIDTH)
                self.controls['lb_output'].setPosSize(0, 0,
                                                      ps_base.Width -
                                                      (footer_width +
                                                       SPLITTER + 3*MARGIN),
                                                      0, PS_WIDTH)
                self.controls['ft_scope'].setPosSize(
                    ps_base.Width - (footer_width + MARGIN - 1), 0, 0, 0, PS_X)
                self.controls['lb_scope'].setPosSize(
                    ps_base.Width - (footer_width + MARGIN), 0, 0, 0, PS_X)
                self.vsplitter.setPosSize(0, 0, ps_base.Width, 0, PS_WIDTH)
                self.hsplitter.setPosSize(
                    ps_base.Width - (footer_width + SPLITTER + 1.5*MARGIN), 0, 0, 0, PS_X)
                self.controls['lb_code'].setPosSize(
                    0, 0, ps_base.Width - 2*MARGIN, 0, PS_WIDTH)
        except Exception:
            traceback.print_exc()

    def windowMoved(self, e):
        pass

    def windowShown(self, e):
        pass

    def windowHidden(self, e):
        pass


class Apsodb(bdb.Bdb, threading.Thread):
    ALERT = 0xff0000
    EXCEPTION = 0xff0101
    RETURN = 0x198a8a    # 0x2aa198

    def __init__(self, dialog):
        # bdb.Bdb.__init__(self)
        bdb.Bdb.__init__(self, skip=(__name__,))
        threading.Thread.__init__(self)
        linecache.clearcache()
        self.dialog = dialog
        self.func = dialog.func
        self.topfilename = self.dialog.topfilename
        self.toprealfilename, self.topdisplayname = self.realfilename(
            self.topfilename)
        self.topfuncname = self.func.__name__
        self.wait_for_topfile = 1
        self.catch_exc = 0
        self.inqueue = self.dialog.inqueue
        self.ui_output = self.dialog.ui_output
        self.stack = []
        self.sources = {}
        self.currentframe = None
        self.currentfilename = ''
        self.lineno = 0

    def trace_dispatch(self, frame, event, arg):
        if self.quitting:
            return  # None
        fn, _ = self.realfilename(frame.f_code.co_filename)
        if not linecache.getline(fn, 1, frame.f_globals):
            return self.trace_dispatch
        if self.wait_for_topfile and fn != self.toprealfilename:
            return self.trace_dispatch
        else:
            self.wait_for_topfile = 0
        if event == 'line':
            return self.dispatch_line(frame)
        elif event == 'call':
            return self.dispatch_call(frame, arg)
        elif event == 'return':
            return self.dispatch_return(frame, arg)
        elif event == 'exception':
            return self.dispatch_exception(frame, arg)
        elif event == 'c_call':
            return self.trace_dispatch
        elif event == 'c_exception':
            return self.trace_dispatch
        elif event == 'c_return':
            return self.trace_dispatch
        self.dialog.writeoutput(
            ('bdb.Bdb.dispatch: unknown debugging event:', repr(event)))
        return self.trace_dispatch

    def dispatch_exception(self, frame, arg):
        self.user_exception(frame, arg)
        if self.quitting:
            raise BdbQuit
        return self.trace_dispatch

    def user_call(self, frame, args):
        # msgbox('user_call', win=self.dialog.topwindow)
        self.updatedisplay(frame)
        name = frame.f_code.co_name
        if not name:
            name = '???'
        frames, _ = self.get_stack(frame, None)
        try:
            argvalues = inspect.formatargvalues(*inspect.getargvalues(frame),
                                                formatvalue=lambda value: '=' + self.repr_(value))
        except Exception:
            print('user_call: error on argvalues')
            argvalues = '({})'.format(UNKNOWN)
        func_argvalues = name + argvalues
        self.stack.append(func_argvalues)
        self.dialog.writeoutput(self.formatstack())
        self.setscope(frame)
        self.catch_exc = 0
        # self.dialog.writeoutput('{}'.format(self.stack[-1]))
        self.wait_for_action(frame, args)

    def user_line(self, frame):
        # msgbox('user_line', win=self.dialog.topwindow)
        self.updatedisplay(frame)
        # find a better solution to keep exception output visible until 'except' instruction
        if self.dialog.ui_output.Model.TextColor == self.EXCEPTION:
            line = linecache.getline(
                self.currentfilename, frame.f_lineno).strip()
            if not (line.startswith('except:') or line.startswith('except ')):
                self.dialog.writeoutput(self.formatstack())
        elif self.dialog.ui_output.Model.TextColor == self.ALERT:
            self.dialog.writeoutput(self.formatstack())
        elif self.dialog.ui_output.SelectedItemPos < self.dialog.ui_output.ItemCount-1:
            self.dialog.ui_output.selectItemPos(
                self.dialog.ui_output.ItemCount-1, True)
        self.setscope(frame)
        self.catch_exc = 0
        self.wait_for_action(frame)

    def user_return(self, frame, retval):
        # msgbox('user_return', win=self.dialog.topwindow)
        if len(self.stack) > 1:
            name = self.stack.pop()
            self.dialog.writeoutput(self.formatstack())
        else:
            self.updatedisplay(frame)
            self.setscope(frame)
            name = frame.f_code.co_name
            self.dialog.writeoutput('[{}] returns: {}'.format(
                name, retval), textcolor=self.RETURN)
        # self.wait_for_action(frame)

    def user_exception(self, frame, exc_info):
        # msgbox('user_exception', win=self.dialog.topwindow)
        exc_type, exc_value, exc_traceback = exc_info
        exc_type_ = str(exc_type).split("'")[1]
        # next line is required as __file__ may sometimes return the compile file name, ending with '.pyc'
        runningfile = __file__.rstrip('c')
        if (frame.f_code.co_filename == runningfile and frame.f_code.co_name == 'run'):
            addtostack = 0
            for innerframe, filename, lineno, name, lines, index in inspect.getinnerframes(exc_traceback):
                fn, dfn = self.realfilename(filename)
                if addtostack:
                    if not name:
                        name = '???'
                    func_argvalues = '{}{}'.format(
                        name, inspect.formatargvalues(*inspect.getargvalues(innerframe)))
                    self.stack.append(func_argvalues)
                if fn == self.toprealfilename:
                    addtostack = 1

            if fn != self.currentfilename:
                self.currentfilename = fn
                self.updatesource(fn, dfn)
            # self.dialog.gotoline(lineno-15)
            self.dialog.gotoline(lineno-1)
            self.dialog.writeoutput(self.formatstack())
            self.currentframe = innerframe
            self.setscope(innerframe)
            msgbox('{}: {}'.format(exc_type_, exc_value),
                   win=self.dialog.topwindow)
            self.catch_exc = 1
            sys.settrace(None)
            # post mortem actions
            self.wait_for_action(innerframe)
        else:
            self.dialog.writeoutput('{}: {}'.format(
                exc_type_, exc_value), self.EXCEPTION)
            # self.catch_exc = 0
            # self.wait_for_action()

    def set_quit(self):
        self.stopframe = self.botframe
        self.returnframe = None
        self.quitting = 1
        sys.settrace(None)

    # clear temporary breakpoint
    def do_clear(self, arg):
        self.clear_break(self.currentfilename, self.lineno)
        self.lineno = 0

    # ## bdb user methods ## #
    def do_next(self, frame):
        if sys.gettrace():
            self.set_next(frame)
        else:
            self.wait_for_action(frame)

    def do_restart(self, frame):
        raise Restart

    def do_step(self, frame):
        if sys.gettrace():
            self.set_step()
        else:
            self.wait_for_action(frame)

    def do_until(self, frame):
        if sys.gettrace():
            # self._set_stopinfo(frame, None, frame.f_lineno+1)
            self.set_until(frame)
        else:
            self.wait_for_action(frame)

    def do_return(self, frame):
        if sys.gettrace():
            self.set_return(frame)
        else:
            self.wait_for_action(frame)

    def do_quit(self, frame):
        print('do_quit')
        self.quitting = 1
        sys.settrace(None)
        raise Restart

    def do_loadframe(self, frame):
        frames_lineno, _ = self.get_stack(frame, None)
        f, lineno = frames_lineno[self.lineno-len(self.stack)]
        self.updatedisplay(f, lineno)
        self.setscope(f)
        self.wait_for_action(frame)

    def do_jump(self, frame):
        if not sys.gettrace():
            self.wait_for_action(frame)
        f = self.currentframe
        lines, firstline = self.getfunclines(f)
        lastline = firstline + len(lines) - 1
        currentline = f.f_lineno
        if currentline == self.lineno:
            self.wait_for_action(frame)
        elif not firstline <= self.lineno <= lastline:
            msgbox(RR.resolvestring('msg37'),
                   boxtype='warning', win=self.dialog.topwindow)
            self.dialog.gotoline(currentline-1)
            self.wait_for_action(frame)
        elif currentline > self.lineno:
            msgbox(RR.resolvestring('msg38'),
                   boxtype='warning', win=self.dialog.topwindow)
            self.dialog.gotoline(currentline-1)
            self.wait_for_action(frame)
        elif not self.checkline(self.lineno):
            msgbox(RR.resolvestring('msg39'),
                   boxtype='warning', win=self.dialog.topwindow)
            self.dialog.gotoline(currentline-1)
            self.wait_for_action(frame)
        else:
            if self.currentframe != frame:
                n = self.dialog.ui_output.SelectedItemPos + 1
                self.stack = self.stack[:n]
                self.dialog.writeoutput(self.formatstack())
            self._set_stopinfo(f, None, self.lineno)

    def do_edit(self, frame):
        if self.currentframe:
            f = self.currentframe
        lineno = f.f_lineno
        filename = f.f_code.co_filename
        try:
            filename = tempfiles[filename]
        except KeyError:
            filename = uno.systemPathToFileUrl(filename)
        # lineno = self.ui_code.SelectedItemPos +1
        apso = self.dialog.create("apso.python.script.organizer.impl")
        apso.trigger("open::{}::{}::0".format(filename, lineno))
        self.wait_for_action(frame)

    def do_console(self, frame):
        try:
            loc = self.currentframe.f_locals
            loc.update(self.currentframe.f_globals)
            console(WIDTH=400, loc=loc, parent=self.dialog.topwindow)
            self.wait_for_action(frame)
        except Exception:
            msgbox(traceback.format_exc(), win=self.dialog.topwindow)

    def checkline(self, lineno):
        line = self.sources[self.currentfilename][lineno-1]
        line = line.split('.', 1)[1].strip()
        if not line or line.startswith('#'):
            print('blank line or comment')
            return 0
        return 1

    # ## threading.Thread ## #
    def run(self):
        try:
            print('debugger started')
            self.stack = []
            self.wait_for_topfile = 1
            self.catch_exc = 0
            self.set_trace()
            self.func()
            sys.settrace(None)
            while True:
                self.wait_for_action(self.currentframe)
        except Restart:
            print('Restart exception')
            pass
        except Exception:
            sys.settrace(None)
            if not self.catch_exc:
                trace = traceback.format_exc().split('\n')
                self.dialog.writeoutput(trace, textcolor=self.ALERT)
                # msgbox(traceback.format_exc(), win=self.dialog.topwindow)
        finally:
            print('debugger exited')

    # ## other ## #
    def updatedisplay(self, frame, lineno=None):
        if lineno is None:
            lineno = frame.f_lineno
        fn, dfn = self.realfilename(frame.f_code.co_filename)
        if fn != self.currentfilename:
            self.currentfilename = fn
            self.updatesource(fn, dfn)
        self.currentframe = frame
        # self.dialog.gotoline(lineno-15)  # to center selection :)
        self.dialog.gotoline(lineno-1)

    def realfilename(self, filename):
        '''Convert uno uri protocol to system url.
        Uri protocol exists only with embedded scripts'''
        try:
            fn = tempfiles[filename]
            x = filename.find('/Scripts/python')
            filename_ = self.dialog.currentcomponent + filename[x:]
            return uno.fileUrlToSystemPath(fn), filename_
        except KeyError:
            fn = self.canonic(filename)
            return fn, fn

    def getfunclines(self, frame):
        fn, _ = self.realfilename(frame.f_code.co_filename)
        firstline = frame.f_code.co_firstlineno
        lines = linecache.getlines(fn)[firstline-1:]
        blocklines = inspect.getblock(lines)
        return blocklines, firstline

    def updatesource(self, filename, displayname):
        self.dialog.ui_code.Model.removeAllItems()
        if filename in self.sources:
            source = self.sources[filename]
        else:
            _source = linecache.getlines(filename)
            source = []
            nalign = len(str(len(_source)))
            for n, line in enumerate(_source, 1):
                try:
                    source.append('{:>{nalign}}.  {}'.format(
                        n, line.decode('utf-8').encode(ENCODING), nalign=nalign))
                except Exception:
                    source.append('{:>{nalign}}.  {}'.format(
                        n, line, nalign=nalign))
            self.sources[filename] = source
        self.dialog.setfilename(displayname)
        self.dialog.ui_code.addItems(tuple(source), 0)

    def wait_for_action(self, frame, args=None):
        try:
            cmd, self.lineno = self.inqueue.get()
            getattr(self, "do_"+cmd)(frame)
        except Restart:
            pass

    def formatstack(self):
        try:
            fstack = self.stack[:1]
            sep = chr(0x2514)
            for n, f in enumerate(self.stack[1:], 1):
                fstack.append('\n{}{} {}'.format(n*' ', sep, self.stack[n]))
            return fstack
        except IndexError:
            return ''

    class EmptyVar():
        def __repr__(self):
            return ''

    def setscope(self, frame):
        f_locals = frame.f_locals
        # nbarg = frame.f_code.co_argcount
        nbarg = 0
        # local namespace
        varnames = sorted(
            frame.f_code.co_varnames[nbarg:], key=lambda s: s.lower())
        varvalues = []
        # # TODO: how to get some classes infos
        for var in varnames:
            varvalues.append('{} : {}'.format(
                var, self.repr_(f_locals.get(var, self.EmptyVar()))))

        # # global variables used by the frame
        # f_globals = {k:v for k,v in frame.f_globals.items() if k in frame.f_code.co_names}
        # varvalues += sorted('*{} : {}'.format(x, f_globals[x]) for x in f_globals)
        # f_locals.update(f_globals)

        self.dialog.ui_scope.Model.removeAllItems()
        self.dialog.ui_scope.addItems(tuple(varvalues), 0)
        # local scope must be available from the dialog thread
        # for post mortem inspection
        self.dialog.localscope = f_locals

    def repr_(self, obj):
        '''prevent error on some pyuno objects
        not defining '__format__' method'''
        try:
            return repr(obj)
        except Exception:
            # msgbox(traceback.format_exc(), win=self.dialog.topwindow)
            return UNKNOWN


def debug(uri, script, scriptprovider):
    try:
        # getcallargs will raise an error before launching debug machinery
        # if func arguments are not correct
        inspect.getcallargs(script.func)
        db = Debugger(uri, script, scriptprovider)
        db.executedebug()
    except Exception:
        msgbox(traceback.format_exc())
    finally:
        sys.settrace(None)
