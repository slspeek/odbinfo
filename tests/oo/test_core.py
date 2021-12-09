""" test site creation """
from pathlib import Path
from unittest.mock import patch

import pytest

from odbinfo.oo import ooutil
from odbinfo.oo.core import generate_report
from odbinfo.oo.ooutil import document_path
from odbinfo.pure import builder
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.util import chdir
from odbinfo.pure.writer import localsite
from tests.resource import TEST_OUTPUT_PATH
from tests.util import clear_generated_graphs


@pytest.mark.veryslow
def test_generate_report(testdb_doc, benchmark, directory_regression):
    """ test generate-site """
    generate_report_test(testdb_doc, benchmark, directory_regression)


@pytest.mark.veryslow
def test_generate_report_empty(emptydb_doc, benchmark, directory_regression):
    """ test generate-site """
    generate_report_test(emptydb_doc, benchmark, directory_regression)


def generate_report_test(oodoc, benchmark, directory_regression):
    """ generate report """
    config = get_configuration()
    config.general.output_dir = str(
        (TEST_OUTPUT_PATH / "test_core").absolute())
    config.graph.user_excludes = []

    odbpath = document_path(oodoc)
    with chdir(odbpath.parent):
        with patch.object(builder, 'find_free_port', return_value=1313) as free_port:
            with patch.object(ooutil, 'document_path',
                              return_value=(Path("") / odbpath.name)) as doc_path:
                benchmark(generate_report, oodoc, config)

        free_port.assert_called()
        doc_path.assert_called()

        # remove the dot generated svg files (depend on dot version)
        clear_generated_graphs(localsite(config.site_path))

        directory_regression.check(localsite(config.site_path))