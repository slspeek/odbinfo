""" Entrypoint for odbinfo extension """

import time

from odbinfo.oo.core import generate_report


def make_site():
    """ Generate report on database metadata """
    # pylint: disable=undefined-variable
    doc = XSCRIPTCONTEXT.getDocument()
    start_time = time.time()
    reportdir = generate_report(doc)
    end_time = time.time()
    print("ODBInfo: report written to {} in {} seconds.".format(
        reportdir, end_time-start_time))


def verify_installation():
    " verify installation "
    # pylint: disable=redefined-outer-name
    # pylint: disable=import-outside-toplevel
    from odbinfo.pure.init import verify_installation
    verify_installation()
