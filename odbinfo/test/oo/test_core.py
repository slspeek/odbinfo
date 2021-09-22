""" test site creation """
import pytest

from odbinfo.oo.core import generate_report
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.test.oo.connect import (  # pylint:disable=unused-import
    emptydb_doc, libreoffice, testdb_doc)
from odbinfo.test.resource import TEST_OUTPUT_TPL


@pytest.mark.veryslow
def test_generate_report(testdb_doc, benchmark):
    """ test generate-site """
    generate_report_test(testdb_doc, benchmark)


@pytest.mark.veryslow
def test_generate_report_empty(emptydb_doc, benchmark):
    """ test generate-site """
    generate_report_test(emptydb_doc, benchmark)


def generate_report_test(oodoc, benchmark):
    " generate report "
    config = get_configuration()
    config.general.output_dir = TEST_OUTPUT_TPL.format("test_core")
    config.graph.user_excludes = []
    benchmark(generate_report, oodoc, config)
