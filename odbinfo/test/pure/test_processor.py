" Tests for the processor "
from odbinfo.pure.processor import process_metadata
# pylint:disable=unused-import
from odbinfo.test.pure.fixtures import metadata, metadata_processed


# pylint:disable=redefined-outer-name
def test_processor_regression(metadata_processed, metadata):
    " regression test "
    process_metadata(metadata)
    assert metadata == metadata_processed
