" Tests for the processor "
import dataclasses
import os
import pickle

from odbinfo.pure.datatype.config import get_configuration
from odbinfo.pure.processor import process_metadata
from odbinfo.test.pure.fixtures import empty_metadata, metadata


def test_processor_regression(metadata, data_regression, file_regression,
                              benchmark):
    " regression test "
    # print("All objects count:", len(metadata.all_objects()))
    process_and_check(metadata, "metadata-processed",
                      data_regression, file_regression, benchmark)


def test_processor_regression_empty(empty_metadata, data_regression,
                                    file_regression, benchmark):
    " regression test on empty database"
    process_and_check(empty_metadata, "empty-metadata-processed",
                      data_regression, file_regression, benchmark)


def process_and_check(unprocessed, filename, data_regression,
                      file_regression, benchmark):
    " do processing and check"
    config = get_configuration()
    config.name, _ = os.path.splitext(os.path.basename(unprocessed.name))
    benchmark(process_metadata, unprocessed, config)
    # data_regression.check(unprocessed)
    file_regression.check(pickle.dumps(unprocessed), binary=True,
                          basename=filename, extension=".pickle")
    unprocessed.graphs = []
    for obj in unprocessed.all_objects():
        obj.parent = None
    data_regression.check(dataclasses.asdict(unprocessed))
