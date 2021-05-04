""" Test the reader and create fixture(s) """
import pickle

from odbinfo.pure.datatype import Metadata
from odbinfo.pure.processor import process_metadata
from odbinfo.test.pure.fixtures import empty_metadata, metadata
from odbinfo.test.resource import TEST_OUTPUT


def pickle_out(data, filename):
    "Write `data` to `filename`.pickle in TEST_OUTPUT"
    with open(TEST_OUTPUT.format(f"{filename}.pickle"), "wb") as out:
        pickle.dump(data, out)


def write_processed_metadata_fixture(data: Metadata, filename):
    "Process `data` and write it out to `filename`.pickle"
    process_metadata(data)
    pickle_out(data, filename)


def test_write_processor_fixture(metadata):
    """ make fixture """
    write_processed_metadata_fixture(metadata, "metadata-processed")


def test_write_processor_fixture_empty(empty_metadata):
    """ make fixture """
    write_processed_metadata_fixture(
        empty_metadata, "empty-metadata-processed")
