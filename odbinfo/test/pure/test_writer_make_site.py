""" writer regression tests """
import pytest

from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.writer import make_site
from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        metadata_processed)
from odbinfo.test.resource import TEST_OUTPUT_TPL


@pytest.mark.slow
def test_make_site(metadata_processed):
    """ Run without database scan """
    name = "testdb"
    make_site_test(name, metadata_processed)


@pytest.mark.slow
def test_make_site_empty(empty_metadata_processed):
    """ Run without database scan """
    name = "emptydb"
    make_site_test(name, empty_metadata_processed)


def make_site_test(name, metadata):
    " generate report and verify"
    conf = get_configuration()
    conf.name = name
    conf.general.output_dir = TEST_OUTPUT_TPL.format("make_site_test")
    make_site(conf, metadata)
