""" test site creation """
import pytest

from odbinfo.oo.core import generate_report
from odbinfo.test.oo.connect import empty_libreoffice, libreoffice, oodocument
from odbinfo.test.resource import TEST_OUTPUT_TPL


@pytest.mark.slow
def test_generate_report(libreoffice):
    """ test generate-site """
    generate_report_test()


@pytest.mark.slow
def test_generate_report_empty(empty_libreoffice):
    """ test generate-site """
    generate_report_test()


def generate_report_test():
    " generate report "
    oodoc = oodocument()
    generate_report(oodoc, TEST_OUTPUT_TPL.format("test_core"))
