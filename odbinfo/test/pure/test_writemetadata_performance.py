""" writer regression tests """
import os
from pathlib import Path

import pytest

from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.writer import write_metadata
from odbinfo.test.resource import TEST_OUTPUT_PATH


def benchmark_writer(output_dir: Path, name, data_loader, benchmark):
    """ generate report and verify"""
    conf = get_configuration(name=name, output_dir=str(output_dir))

    def setup():
        metadata = data_loader()
        return (conf, metadata), {}

    os.makedirs(conf.site_path, exist_ok=True)
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
    """ generate report and verify"""
    output_dir = TEST_OUTPUT_PATH / "test_writer_performance"
    benchmark_writer(output_dir, name, metadata, benchmark)
