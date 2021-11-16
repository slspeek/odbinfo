""" writer regression tests """
import os
from pathlib import Path

import pytest

from odbinfo.pure.datatype import Metadata
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.writer import write_metadata
from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        empty_metadata_processed_loader,
                                        metadata_processed,
                                        metadata_processed_loader)
from odbinfo.test.resource import TEST_OUTPUT_PATH


def write_writer_fixture(output_dir: Path, name: str, metadata: Metadata):
    " generate report and verify"
    conf = get_configuration()
    site_dir = output_dir / name
    os.makedirs(site_dir, exist_ok=True)
    conf.name = name
    write_metadata(conf, metadata, site_dir)


@pytest.mark.slow
def test_writer_regression(metadata_processed, shared_datadir):
    """ Run without database scan """
    name = "testdb"
    make_writer_regression_test(name, metadata_processed,
                                shared_datadir / "writer_fixtures/testdb")


@pytest.mark.slow
def test_writer_regression_empty(empty_metadata_processed, shared_datadir):
    """ Run without database scan """
    name = "emptydb"
    make_writer_regression_test(name, empty_metadata_processed,
                                shared_datadir / "writer_fixtures/emptydb")


def make_writer_regression_test(name, metadata, fixture_name: str):
    " generate report and verify"
    output_dir = TEST_OUTPUT_PATH / "test_writer_regression"
    write_writer_fixture(output_dir, name, metadata)
    site_dir = output_dir / name
    assert os.system(f"diff -r {fixture_name}/ {str(site_dir)}/") == 0


def benchmark_writer(output_dir: Path, name, data_loader, benchmark):
    " generate report and verify"
    conf = get_configuration()
    conf.name = name

    def setup():
        metadata = data_loader()
        return (conf, metadata, output_dir / name), {}
    site_dir = f"{output_dir}/{name}"
    os.makedirs(site_dir, exist_ok=True)
    benchmark.pedantic(write_metadata, setup=setup)


@pytest.mark.slow
def test_writer_performance(metadata_processed_loader, benchmark):
    """ Run without database scan """
    name = "testdb"
    make_writer_performance_test(name, metadata_processed_loader,
                                 benchmark)


@pytest.mark.slow
def test_writer_performance_empty(empty_metadata_processed_loader, benchmark):
    """ Run without database scan """
    name = "emptydb"
    make_writer_performance_test(name, empty_metadata_processed_loader,
                                 benchmark)


def make_writer_performance_test(name, metadata, benchmark):
    " generate report and verify"
    output_dir = TEST_OUTPUT_PATH / "test_writer_performance"
    benchmark_writer(output_dir, name, metadata, benchmark)
