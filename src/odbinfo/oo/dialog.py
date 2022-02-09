""" provides a dialog with actionlistener """
import logging

import unohelper
from com.sun.star.awt import XActionListener  # pylint: disable=import-error
from msgbox import MsgBox

# Define a new logging handler class which inherits the logging.Handler class


class DialogLogger(logging.Handler):
    """ Logging handler that updates a textarea widget"""
    # The init function needs the widget which will hold the log messages passed to it as
    # well as other basic information (log level, format, etc.)

    def __init__(self, widget, logLevel, _format):
        logging.Handler.__init__(self)

        # Basic logging configuration
        self.setLevel(logLevel)
        self.setFormatter(logging.Formatter(_format))
        self.widget = widget

        # The ScrolledText box must be disabled so users can't enter their own text
        # self.widget.config(state='disabled')

    # This function is called when a log message is to be handled
    def emit(self, record):
        # Append log message to the widget
        self.widget.insertText(self.widget.getSelection(),
                               str(self.format(record) + '\n'))


class ButtonListener(unohelper.Base, XActionListener):
    """ actionlistener for the start button """

    def __init__(self, ctx, dlg):
        super().__init__()
        self.ctx = ctx
        self.dlg = dlg

    def disposing(self, _):
        """ do nothing on disposing dialog """

    # pylint: disable=invalid-name
    def actionPerformed(self, _):  # NOQA
        """ start the running of the queries and report results """
        msg_box = MsgBox(self.ctx)
        msg_box.addButton("Yes")
        msg_box.renderFromBoxSize(150)
        msg_box.numberOflines = 2
        msg_box.show("All queries can run", 0, "Success")


def create_logging_dialog(ctx=None):
    """ create the verify dialog """
    smgr = ctx.getServiceManager()
    dprovider = smgr.createInstanceWithContext(
        "com.sun.star.awt.DialogProvider", ctx)
    dlg = dprovider.createDialog(
        "vnd.sun.star.script:odbinfo_ui.LoggingDialog.xdl?"
        "location=application")
    log_text = dlg.getControl("log_text")
    logging.info(dir(log_text.AccessibleContext))
    logging.info(dir(log_text))
    logging.getLogger().addHandler(DialogLogger(
        log_text, logging.INFO, logging.BASIC_FORMAT))
    # start_button = dlg.getControl("Start")
    # start_button.addActionListener(ButtonListener(ctx, dlg))
    return dlg


def logging_dialog(ctx=None):
    """ runs the Verify Queries Dialog """
    dlg = create_logging_dialog(ctx)
    dlg.execute()
    dlg.dispose()
