""" writer regression tests """
import pytest

from odbinfo.pure.datatype.config import create_configuration
from odbinfo.pure.writer import write_metadata
from tests.resource import TEST_OUTPUT_PATH


@pytest.mark.slow
def test_writemetadata(metadata_processed, directory_regression):
    """ Run without database scan """
    perform_writemetadata_regression_test("testdb", metadata_processed,
                                          directory_regression)


@pytest.mark.slow
def test_writemetadata_empty(empty_metadata_processed, directory_regression):
    """ Run without database scan """
    perform_writemetadata_regression_test("emptydb", empty_metadata_processed,
                                          directory_regression)


def perform_writemetadata_regression_test(name, metadata, directory_regression):
    """ generate report and verify"""
    output_dir = str(TEST_OUTPUT_PATH / "test_writemetadata_regression")
    config = create_configuration(name, output_dir)
    config.site_path.mkdir(exist_ok=True, parents=True)
    write_metadata(config, metadata)

    directory_regression.check(config.site_path)
