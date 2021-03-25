""" Entrypoint for odbinfo extension """


from odbinfo.oo.core import generate_report


def make_site():
    """ Generate report on database metadata """
    # pylint: disable=undefined-variable
    doc = XSCRIPTCONTEXT.getDocument()
    reportdir = generate_report(doc)
    print(f"ODBInfo: report written in {reportdir}")
