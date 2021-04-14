""" Test the reader and create fixture(s) """
import pickle

from odbinfo.oo.reader import read_metadata
from odbinfo.test.oo.connect import libreoffice  # pylint:disable=unused-import
from odbinfo.test.oo.connect import datasource
from odbinfo.test.resource import DEFAULT_TESTDB, TEST_OUTPUT


# pylint:disable=unused-argument
def test_read_metadata(libreoffice):  # pylint:disable=redefined-outer-name
    """ make fixture """
    dsource = datasource()
    metadata = read_metadata(dsource, DEFAULT_TESTDB)
    with open(TEST_OUTPUT.format("metadata.pickle"), "wb") as out:
        pickle.dump(metadata, out)