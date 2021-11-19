""" test site creation """
from pathlib import Path
from unittest.mock import patch

import pytest

from odbinfo.oo.core import generate_report
from odbinfo.oo.ooutil import document_path
from odbinfo.pure import writer
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.writer import chdir
from odbinfo.test.oo.connect import (  # pylint:disable=unused-import
    emptydb_doc, libreoffice, testdb_doc)
from odbinfo.test.resource import TEST_OUTPUT_PATH


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
    config.general.output_dir = str(
        (TEST_OUTPUT_PATH / "test_core").absolute())
    config.graph.user_excludes = []

    odbpath = document_path(oodoc)
    with chdir(odbpath.parent):
        with patch.object(writer, 'find_free_port', return_value=1313):
            benchmark(generate_report, oodoc, config,
                      odbpath=Path(".") / odbpath.name)
