""" Test the reader and create fixture(s) """
from odbinfo.test.oo.connect import empty_libreoffice, libreoffice
from odbinfo.test.oo.test_reader_regression import read_metadata_in_test
from odbinfo.test.pure.fixture_writer import pickle_out
from odbinfo.test.resource import DEFAULT_TESTDB, EMPTYDB


def test_write_fixture_default(libreoffice):
    """ make fixture """
    write_metadata_fixture(DEFAULT_TESTDB, "metadata")


def test_write_fixture_empty(empty_libreoffice):
    """ make fixture """
    write_metadata_fixture(EMPTYDB, "empty-metadata")


def write_metadata_fixture(dbpath, pickle_file):
    " read_metadata and write out to `pickle_file`"
    metadata = read_metadata_in_test(dbpath)
    pickle_out(metadata, pickle_file)
