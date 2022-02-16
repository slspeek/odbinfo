""" Entrypoint for odbinfo extension """

import logging

from odbinfo.oo import dialog
from odbinfo.oo.core import generate_report


def make_site():
    """ Generate report on database metadata """
    # pylint: disable=undefined-variable
    doc = XSCRIPTCONTEXT.getDocument()
    ctx = XSCRIPTCONTEXT.getComponentContext()
    generate_report(doc, gui=True, ctx=ctx)


def verify_installation():
    """ verify installation """
    logging.basicConfig(level=logging.INFO)
    # pylint: disable=undefined-variable
    ctx = XSCRIPTCONTEXT.getComponentContext()
    dlg = dialog.create_diagnostics_dialog(ctx)
    dlg.execute()
    dlg.dispose()
