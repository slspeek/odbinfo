""" writer regression tests """
import os

import pytest

from odbinfo.pure.writer import _write_metadata, chdir
from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        metadata_processed)
from odbinfo.test.resource import TEST_OUTPUT_TPL


def write_writer_fixture(output_dir, name, metadata):
    " generate report and verify"
    site_dir = f"{output_dir}/{name}"
    os.makedirs(site_dir, exist_ok=True)
    with chdir(site_dir):
        _write_metadata(name, metadata)


@pytest.mark.slow
def test_site_regression(metadata_processed, shared_datadir):
    """ Run without database scan """
    name = "testdb"
    make_site_regression_test(name, metadata_processed,
                              shared_datadir / "writer_fixtures/testdb")


@pytest.mark.slow
def test_site_regression_empty(empty_metadata_processed, shared_datadir):
    """ Run without database scan """
    name = "emptydb"
    make_site_regression_test(name, empty_metadata_processed,
                              shared_datadir / "writer_fixtures/emptydb")


def make_site_regression_test(name, metadata, fixture_name: str):
    " generate report and verify"
    output_dir = TEST_OUTPUT_TPL.format("test_writer_regression")
    write_writer_fixture(output_dir, name, metadata)
    site_dir = f"{output_dir}/{name}"
    assert os.system(f"diff -r {fixture_name}/ {site_dir}/") == 0
