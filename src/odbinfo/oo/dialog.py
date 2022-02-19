""" provides a dialog with actionlistener """
import abc
import logging
import os
import threading

import unohelper
from com.sun.star.awt import XActionListener  # pylint: disable=import-error

from odbinfo.pure import diagnostics

# Define a new logging handler class which inherits the logging.Handler class


class DialogLogger(logging.Handler):
    """ Logging handler that updates a textfield widget"""

    # The init function needs the widget which will hold the log messages passed to it as
    # well as other basic information (log level, format, etc.)

    def __init__(self, widget, log_level, _format):
        logging.Handler.__init__(self)

        # Basic logging configuration
        self.setLevel(log_level)
        self.setFormatter(logging.Formatter(_format))
        self.widget = widget

        # The ScrolledText box must be disabled so users can't enter their own text
        # self.widget.config(state='disabled')

    # This function is called when a log message is to be handled
    def emit(self, record):
        # Append log message to the widget
        self.widget.insertText(self.widget.getSelection(),
                               str(self.format(record) + '\n'))


class DialogActionListener(unohelper.Base, XActionListener):
    """ actionlistener for dialogs """

    def __init__(self, ctx, dlg):
        super().__init__()
        self.ctx = ctx
        self.dlg = dlg

    def disposing(self, _):
        """ do nothing on disposing dialog """

    # pylint: disable=invalid-name
    def actionPerformed(self, _):  # NOQA
        """ action command """


class ButtonListener(DialogActionListener):
    """ actionlistener for the start button """

    def __init__(self, ctx, dlg, target, *args):
        super().__init__(ctx, dlg)
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
    """ create the verify dialog """
    dlg = create_dialog(ctx, "odbinfo_ui.LoggingDialog")

    start_button = dlg.getControl("start_button")
    start_button.addActionListener(ButtonListener(ctx, dlg, target, *args))
    # logging.info(dir(start_button))
    start_button.setFocus()
    log_text = dlg.getControl("log_text")
    dlg.setTitle("ODBInfo logging")
    # logging.info(dir(dlg))
    # logging.info(dir(log_text.AccessibleContext))
    # logging.info(dir(log_text))
    logging.getLogger().addHandler(
        DialogLogger(log_text, logging.INFO, "%(levelname)s: %(message)s"))

    return dlg


# def logging_dialog(ctx=None):
#     """ runs the Verify Queries Dialog """
#     dlg = create_logging_dialog(ctx)
#     dlg.execute()
#     dlg.dispose()


class GUICommand(abc.ABC):
    """ Command that dispatches on the dialog"""

    def __init__(self, dlg):
        self.dlg = dlg

    @abc.abstractmethod
    def run(self):
        """ Do some gui stuff"""


class CheckAction(GUICommand):
    """ Verification action """

    def __init__(self, dlg, name, target):
        super().__init__(dlg)
        self.name = name
        self.target = target

    def run(self, ):
        found, msg = diagnostics.try_run(self.target)
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


class DiagnosticsAction(DialogActionListener):
    """ Run all diagnostics action """

    def __init__(self, ctx, dlg):
        super().__init__(ctx, dlg)
        self.actions = [
            CheckAction(dlg, name, getattr(diagnostics, f"{name}_version"))
            for name in ["graphviz", "gohugo", "wget"]
        ] + [PathAction(dlg)]

        logging.info("Diagnostics constructor finished")

    def actionPerformed(self, _):
        for action in self.actions:
            action.run()
            print("action " + action.name)


def create_diagnostics_dialog(ctx):
    """ create the verify dialog """
    dlg = create_dialog(ctx, "odbinfo_ui.DiagnosticsDialog")

    diagnostics_button = dlg.getControl("all_check")
    diagnostics_button.addActionListener(DiagnosticsAction(ctx, dlg))
    diagnostics_button.setFocus()

    dlg.setTitle("ODBInfo self diagnostics")

    return dlg
