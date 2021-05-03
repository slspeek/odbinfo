""" Test the reader and create fixture(s) """
import pickle

from odbinfo.pure.processor import process_metadata
from odbinfo.test.pure.fixtures import (  # pylint:disable=unused-import
    empty_metadata, metadata)
from odbinfo.test.resource import TEST_OUTPUT


# pylint:disable=unused-argument
def test_write_processor_fixture(metadata):  # pylint:disable=redefined-outer-name
    """ make fixture """

    process_metadata(metadata)
    with open(TEST_OUTPUT.format("metadata-processed.pickle"), "wb") as out:
        pickle.dump(metadata, out)

# pylint:disable=unused-argument


def test_write_processor_fixture_empty(empty_metadata):  # pylint:disable=redefined-outer-name
    """ make fixture """

    process_metadata(empty_metadata)
    with open(TEST_OUTPUT.format("empty-metadata-processed.pickle"), "wb") as out:
        pickle.dump(empty_metadata, out)
