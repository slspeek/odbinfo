""" Entrypoint for odbinfo extension """

import time

from odbinfo.oo.core import generate_report


def make_site():
    """ Generate report on database metadata """
    # pylint: disable=undefined-variable
    doc = XSCRIPTCONTEXT.getDocument()
    reportdir = generate_report(doc)


def verify_installation():
    " verify installation "
    # pylint: disable=redefined-outer-name
    # pylint: disable=import-outside-toplevel
    from odbinfo.pure.init import verify_installation
    verify_installation()
