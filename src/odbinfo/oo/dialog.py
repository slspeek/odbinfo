""" provides a dialog with actionlistener """
import abc
import logging
import os
import threading

import unohelper
from com.sun.star.awt import XActionListener  # pylint: disable=import-error

from odbinfo.pure import diagnostics


class TextFieldLogger(logging.Handler):
    """ Logging handler that updates a textfield widget"""

    def __init__(self, textfield, log_level, _format):
        logging.Handler.__init__(self)

        # Basic logging configuration
        self.setLevel(log_level)
        self.setFormatter(logging.Formatter(_format))
        self.textfield = textfield

        # The ScrolledText box must be disabled so users can't enter their own text
        # self.textfield.config(state='disabled')

    # This function is called when a log message is to be handled
    def emit(self, record):
        # Append log message to the widget
        self.textfield.insertText(self.textfield.getSelection(),
                                  str(self.format(record) + '\n'))


class DialogActionListener(unohelper.Base, XActionListener, abc.ABC):
    """ actionlistener for dialogs """

    def __init__(self, dlg):
        super().__init__()
        self.dlg = dlg

    def disposing(self, _):
        """ do nothing on disposing dialog """

    # pylint: disable=invalid-name
    def actionPerformed(self, _):  # NOQA
        """ action command """


class ButtonListener(DialogActionListener):
    """ actionlistener for the start button """

    def __init__(self, dlg, target, *args):
        super().__init__(dlg)
        self.target = target
        self.args = args

    def disposing(self, _):
        """ do nothing on disposing dialog """

    # pylint: disable=invalid-name
    def actionPerformed(self, _):  # NOQA
        """ disable start button, focus Close button, start the target on a separate thread """
        start_button = self.dlg.getControl("start_button")
        start_button.setEnable(False)
        close_button = self.dlg.getControl("Close")
        close_button.setFocus()

        thread = threading.Thread(target=self.target, args=self.args)
        thread.start()


def create_dialog(ctx, dialog_name: str):
    """ return Dialog for `dialog_name` (without .xdl) """
    smgr = ctx.getServiceManager()
    dprovider = smgr.createInstanceWithContext(
        "com.sun.star.awt.DialogProvider", ctx)
    dlg = dprovider.createDialog(f"vnd.sun.star.script:{dialog_name}.xdl?"
                                 "location=application")
    return dlg


def create_logging_dialog(target, *args, ctx=None):
    """ create the logging dialog with a start button
        which will execute `target` on `args` when pressed,
        while displaying the logging in the a textfield """
    dlg = create_dialog(ctx, "odbinfo_ui.LoggingDialog")

    start_button = dlg.getControl("start_button")
    start_button.addActionListener(ButtonListener(dlg, target, *args))
    # logging.info(dir(start_button))
    start_button.setFocus()
    log_text = dlg.getControl("log_text")
    dlg.setTitle("ODBInfo logging")
    logging.getLogger().addHandler(
        TextFieldLogger(log_text, logging.INFO, "%(levelname)s: %(message)s"))

    return dlg


class GUICommand(abc.ABC):
    """ Command that dispatches on the dialog"""

    def __init__(self, dlg):
        self.dlg = dlg

    @abc.abstractmethod
    def run(self):
        """ Do some gui stuff"""


class DiagnosticsAction(GUICommand):
    """ Diagnostics action """

    def __init__(self, dlg, name, target):
        """ possible names are
            "graphviz", "gohugo", "wget" """
        super().__init__(dlg)
        self.name = name
        self.target = target

    def run(self):
        found, msg = self.target()
        msg_label = self.dlg.getControl(f"{self.name}_msg")
        msg_label.Text = msg
        found_msg = self.dlg.getControl(f"{self.name}_found")
        # print(dir(found_msg.StyleSettings))
        found_msg.Text = "Found" if found else "Missing"
        found_msg.StyleSettings.LabelTextColor = 0x00D100 if found else 0xFF2424


class PathAction(GUICommand):
    """ Read PATH action """

    def __init__(self, dlg):
        super().__init__(dlg)
        self.name = "path"

    def run(self):
        msg_label = self.dlg.getControl("path_msg")
        msg_label.Text = os.getenv("PATH")


class AllDiagnosticsAction(DialogActionListener):
    """ Run all diagnostics actions, that is
        1. check for graphivz
        2. check for gohugo
        3. check for wget
        4. read the PATH var """

    def __init__(self, dlg):
        super().__init__(dlg)
        self.actions = [
            DiagnosticsAction(dlg, name, getattr(diagnostics,
                                                 f"{name}_version"))
            for name in ["graphviz", "gohugo", "wget"]
        ] + [PathAction(dlg)]

        logging.info("Diagnostics constructor finished")

    def actionPerformed(self, _):
        for action in self.actions:
            action.run()


def create_diagnostics_dialog(ctx):
    """ create the diagnostics dialog """
    dlg = create_dialog(ctx, "odbinfo_ui.DiagnosticsDialog")

    diagnostics_button = dlg.getControl("all_check")
    diagnostics_button.addActionListener(AllDiagnosticsAction(dlg))
    diagnostics_button.setFocus()

    dlg.setTitle("ODBInfo self diagnostics")

    return dlg
