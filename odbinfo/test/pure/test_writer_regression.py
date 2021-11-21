""" writer regression tests """
from pathlib import Path

import pytest

from odbinfo.pure.datatype import Metadata
from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.writer import write_metadata
from odbinfo.test.pure.fixtures import (empty_metadata_processed,
                                        metadata_processed)
from odbinfo.test.regression import directory_regression
from odbinfo.test.resource import TEST_OUTPUT_PATH


def write_writer_fixture(output_dir: Path, name: str, metadata: Metadata):
    " generate report and verify"
    conf = get_configuration(name, output_dir)
    conf.site_path.mkdir(exist_ok=True, parents=True)
    write_metadata(conf, metadata)


@pytest.mark.slow
def test_writer_regression(metadata_processed, directory_regression):
    """ Run without database scan """
    make_writer_regression_test("testdb", metadata_processed,
                                directory_regression)


@pytest.mark.slow
def test_writer_regression_empty(empty_metadata_processed, directory_regression):
    """ Run without database scan """
    make_writer_regression_test("emptydb", empty_metadata_processed,
                                directory_regression)


def make_writer_regression_test(name, metadata, directory_regression):
    " generate report and verify"
    output_dir = TEST_OUTPUT_PATH / "test_writer_regression"
    write_writer_fixture(output_dir, name,  metadata)
    directory_regression.check(output_dir / name)
