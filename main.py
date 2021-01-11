""" Entrypoint for odbinfo extension """


from odbinfo.core import generate_report


def make_site():
    """ Generate report on database metadata """
    # pylint: disable=undefined-variable
    doc = XSCRIPTCONTEXT.getDocument()
    generate_report(doc)
