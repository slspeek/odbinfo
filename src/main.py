""" Entrypoint for odbinfo extension """

from odbinfo.oo.core import generate_report


def make_site():
    """ Generate report on database metadata """
    # pylint: disable=undefined-variable
    doc = XSCRIPTCONTEXT.getDocument()
    generate_report(doc, gui=True, ctx=ctx)


def verify_installation():
    """ verify installation """
    # pylint: disable=redefined-outer-name
    # pylint: disable=import-outside-toplevel
    from odbinfo.pure.init import verify_installation
    verify_installation()
