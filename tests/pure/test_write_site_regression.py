""" writer regression tests """
import pytest

from odbinfo.pure.datatype.config import create_configuration
from odbinfo.pure.writer import write_site
from tests.resource import TEST_OUTPUT_PATH
from tests.util import clear_generated_graphs


@pytest.mark.veryslow
def test_write_site(metadata_processed, directory_regression):
    """ Run without database scan """
    write_site_test("testdb", metadata_processed, directory_regression)


@pytest.mark.veryslow
def test_write_site_empty(empty_metadata_processed, directory_regression):
    """ Run without database scan """
    write_site_test("emptydb", empty_metadata_processed, directory_regression)


def write_site_test(name, metadata, directory_regression):
    """ generate report and verify"""
    conf = create_configuration(
        name, str(TEST_OUTPUT_PATH / "write_site_test"))
    write_site(conf, metadata)

    clear_generated_graphs(conf.site_path)

    directory_regression.check(conf.site_path)
