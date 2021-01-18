""" Test the reader and create fixture(s) """
import pickle

from test.test_new_site import libreoffice  # pylint:disable=unused-import
from test.connect import datasource
from test.resource import DEFAULT_TESTDB
from odbinfo.reader import read_metadata


# pylint:disable=unused-argument
def test_read_metadata(libreoffice):  # pylint:disable=redefined-outer-name
    """ make fixture """
    dsource = datasource()
    metadata = read_metadata(dsource, DEFAULT_TESTDB)
    with open("test/resources/fixtures/metadata.pickle", "rb") as file:
        metadata_before = pickle.load(file)
        assert metadata == metadata_before
