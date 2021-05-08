""" test site creation """
import pytest

from odbinfo.oo.core import generate_report
from odbinfo.test.oo.connect import (  # pylint:disable=unused-import
    emptydb_doc, libreoffice, testdb_doc)
from odbinfo.test.resource import TEST_OUTPUT_TPL


@pytest.mark.slow
def test_generate_report(testdb_doc):
    """ test generate-site """
    generate_report_test(testdb_doc)


@pytest.mark.slow
def test_generate_report_empty(emptydb_doc):
    """ test generate-site """
    generate_report_test(emptydb_doc)


def generate_report_test(oodoc):
    " generate report "
    generate_report(oodoc, TEST_OUTPUT_TPL.format("test_core"))
