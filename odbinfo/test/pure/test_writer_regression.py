""" writer regression tests """
import os

import pytest

from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        metadata_processed)
from odbinfo.test.pure.writer_fixture_writer import write_writer_fixture
from odbinfo.test.resource import FIXTURE_DIR_TPL, TEST_OUTPUT_TPL


@pytest.mark.slow
def test_site_regression(metadata_processed):
    """ Run without database scan """
    name = "testdb"
    make_site_regression_test(name, metadata_processed,
                              FIXTURE_DIR_TPL.format("writer_fixtures/testdb"))


@pytest.mark.slow
def test_site_regression_empty(empty_metadata_processed):
    """ Run without database scan """
    name = "emptydb"
    make_site_regression_test(name, empty_metadata_processed,
                              FIXTURE_DIR_TPL.format("writer_fixtures/emptydb"))


def make_site_regression_test(name, metadata, fixture_name: str):
    " generate report and verify"
    write_writer_fixture(name, metadata)
    site_dir = TEST_OUTPUT_TPL.format(name)
    assert os.system(f"diff -r {fixture_name}/ {site_dir}/") == 0
