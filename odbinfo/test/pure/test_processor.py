" Tests for the processor "
from odbinfo.pure.processor import process_metadata
from odbinfo.test.pure.fixtures import (empty_metadata,
                                        empty_metadata_processed, metadata,
                                        metadata_processed)


def test_processor_regression(metadata, metadata_processed):
    " regression test "
    process_and_check(metadata, metadata_processed)


def test_processor_regression_empty(empty_metadata, empty_metadata_processed):
    " regression test on empty database"
    process_and_check(empty_metadata, empty_metadata_processed)


def process_and_check(unprocessed, processed):
    " do processing and checked againt known value `processed`"
    process_metadata(unprocessed)  # changes `unprocessed`
    assert unprocessed == processed
