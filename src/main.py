""" Entrypoint for odbinfo extension """

import logging

from odbinfo.oo import dialog
from odbinfo.oo.core import generate_report_ui


def make_site():
    """ Generate report on database metadata
        It reads from the current database document.
    """
    # pylint: disable=undefined-variable
    doc = XSCRIPTCONTEXT.getDocument()
    ctx = XSCRIPTCONTEXT.getComponentContext()
    generate_report_ui(oodocument=doc, ctx=ctx, open_browser=True)


def diagnostics():
    """ Opens a diagnostics dialog, to check for the dependenies
        needed to run ODBInfo
    """
    logging.basicConfig(level=logging.INFO)
    # pylint: disable=undefined-variable
    ctx = XSCRIPTCONTEXT.getComponentContext()
    dlg = dialog.create_diagnostics_dialog(ctx)
    dlg.execute()
    dlg.dispose()
