""" provides a dialog with actionlistener """
import logging
import threading

import unohelper
from com.sun.star.awt import XActionListener  # pylint: disable=import-error

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


class ButtonListener(unohelper.Base, XActionListener):
    """ actionlistener for the start button """

    def __init__(self, ctx, dlg, target, *args):
        super().__init__()
        self.target = target
        self.args = args
        self.ctx = ctx
        self.dlg = dlg

    def disposing(self, _):
        """ do nothing on disposing dialog """

    # pylint: disable=invalid-name
    def actionPerformed(self, _):  # NOQA
        """ disable start button, focus Close button, start the target on a separate thread """
        start_button = self.dlg.getControl("start_button")
        start_button.setEnable(False)
        close_button = self.dlg.getControl("Close")
        close_button.setFocus()

        thread = threading.Thread(target=self.target,
                                  args=self.args)
        thread.start()


def create_logging_dialog(target, *args, ctx=None):
    """ create the verify dialog """
    smgr = ctx.getServiceManager()
    dprovider = smgr.createInstanceWithContext(
        "com.sun.star.awt.DialogProvider", ctx)
    dlg = dprovider.createDialog(
        "vnd.sun.star.script:odbinfo_ui.LoggingDialog.xdl?"
        "location=application")
    start_button = dlg.getControl("start_button")
    start_button.addActionListener(ButtonListener(ctx, dlg, target, *args))
    # logging.info(dir(start_button))
    start_button.setFocus()
    log_text = dlg.getControl("log_text")
    dlg.setTitle("ODBInfo")
    logging.info(dir(dlg))
    # logging.info(dir(log_text.AccessibleContext))
    # logging.info(dir(log_text))
    logging.getLogger().addHandler(DialogLogger(
        log_text, logging.INFO, "%(levelname)s: %(message)s"))

    return dlg


# def logging_dialog(ctx=None):
#     """ runs the Verify Queries Dialog """
#     dlg = create_logging_dialog(ctx)
#     dlg.execute()
#     dlg.dispose()
