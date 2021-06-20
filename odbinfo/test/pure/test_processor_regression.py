" Tests for the processor "
import dataclasses
import pickle

from odbinfo.pure.processor import process_metadata
from odbinfo.test.pure.fixtures import empty_metadata, metadata


def test_processor_regression(metadata, data_regression, file_regression):
    " regression test "
    # print("All objects count:", len(metadata.all_objects()))
    process_and_check(metadata, "metadata-processed",
                      data_regression, file_regression)


def test_processor_regression_empty(empty_metadata, data_regression,
                                    file_regression):
    " regression test on empty database"
    process_and_check(empty_metadata, "empty-metadata-processed",
                      data_regression, file_regression)


def process_and_check(unprocessed, filename, data_regression, file_regression):
    " do processing and check"
    process_metadata(unprocessed)  # changes `unprocessed`
    data_regression.check(dataclasses.asdict(unprocessed))
    file_regression.check(pickle.dumps(unprocessed), binary=True,
                          basename=filename, extension=".pickle")
