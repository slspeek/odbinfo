""" writer regression tests """
import os

import pytest

from odbinfo.pure.writer import make_site
from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        metadata_processed)
from odbinfo.test.resource import FIXTURE_DIR_TPL, TEST_OUTPUT_TPL


@pytest.mark.slow
def test_quick_view(metadata_processed):
    """ Run without database scan """
    name = "testdb"
    make_site_regression_test(name, metadata_processed, FIXTURE_DIR_TPL.format(
        "writer_fixtures/testdb-local"))


@pytest.mark.slow
def test_quick_view_empty(empty_metadata_processed):
    """ Run without database scan """
    name = "emptydb"
    make_site_regression_test(name, empty_metadata_processed, FIXTURE_DIR_TPL.format(
        "writer_fixtures/emptydb-local"))


def make_site_regression_test(name, metadata, fixture_name_local: str):
    " generate report and verify"
    outdir = TEST_OUTPUT_TPL.format("")
    site_dir_local = make_site(outdir, name, metadata)
    site_dir = site_dir_local[:-6]
    fixture_name = fixture_name_local[:-6]
    assert os.system(f"diff -r {fixture_name} {site_dir}") == 0
    