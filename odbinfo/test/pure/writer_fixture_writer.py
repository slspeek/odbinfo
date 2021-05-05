""" writer regression tests """
import os

import pytest

from odbinfo.pure.writer import _write_metadata, chdir
from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        metadata_processed)
from odbinfo.test.resource import TEST_OUTPUT_TPL


@pytest.mark.slow
def test_site_regression(metadata_processed):
    """ Run without database scan """
    name = "testdb"
    write_writer_fixture(name, metadata_processed)


@pytest.mark.slow
def test_site_regression_empty(empty_metadata_processed):
    """ Run without database scan """
    name = "emptydb"
    write_writer_fixture(name, empty_metadata_processed)


def write_writer_fixture(name, metadata):
    " generate report and verify"
    site_dir = TEST_OUTPUT_TPL.format(name)
    os.makedirs(site_dir, exist_ok=True)
    with chdir(site_dir):
        _write_metadata(name, metadata)
