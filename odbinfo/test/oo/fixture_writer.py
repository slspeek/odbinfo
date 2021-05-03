""" Test the reader and create fixture(s) """
import pickle

from odbinfo.oo.reader import read_metadata
from odbinfo.test.oo.connect import (  # pylint:disable=unused-import
    datasource, empty_libreoffice, libreoffice)
from odbinfo.test.resource import DEFAULT_TESTDB, EMPTYDB, TEST_OUTPUT


# pylint:disable=unused-argument
def test_write_fixture_default(libreoffice):  # pylint:disable=redefined-outer-name
    """ make fixture """
    dsource = datasource()
    metadata = read_metadata(dsource, DEFAULT_TESTDB)
    with open(TEST_OUTPUT.format("metadata.pickle"), "wb") as out:
        pickle.dump(metadata, out)

# pylint:disable=unused-argument


def test_write_fixture_empty(empty_libreoffice):  # pylint:disable=redefined-outer-name
    """ make fixture """
    dsource = datasource()
    metadata = read_metadata(dsource, EMPTYDB)
    with open(TEST_OUTPUT.format("empty-metadata.pickle"), "wb") as out:
        pickle.dump(metadata, out)
