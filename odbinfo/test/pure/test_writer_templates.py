""" writer regression tests """

import pytest

from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.writer import (build_site, new_site, write_graphs,
                                 write_metadata)
from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        metadata_processed)
from odbinfo.test.regression import directory_regression
from odbinfo.test.resource import TEST_OUTPUT_PATH
from odbinfo.test.util import remove_generated_graphs


@pytest.mark.slow
def test_template_regression(metadata_processed, directory_regression):
    """ Run without database scan """
    perform_template_regression_test("testdb", metadata_processed,
                                     directory_regression)


@pytest.mark.slow
def test_template_regression_empty(empty_metadata_processed, directory_regression):
    """ Run without database scan """
    perform_template_regression_test("emptydb", empty_metadata_processed,
                                     directory_regression)


def perform_template_regression_test(name, metadata, directory_regression):
    " generate report and verify"
    config = get_configuration(name, TEST_OUTPUT_PATH
                               / "test_template_regression")
    new_site(config.site_path)
    write_metadata(config, metadata)
    write_graphs(metadata.graphs, config.site_path)
    build_site(config.site_path)

    remove_generated_graphs(config.site_path / "public")
    directory_regression.check(config.site_path / "public")
