""" Test the reader and create fixture(s) """
import pickle

from odbinfo.test.test_new_site import libreoffice  # pylint:disable=unused-import
from odbinfo.test.connect import datasource
from odbinfo.test.resource import TEST_OUTPUT, DEFAULT_TESTDB
from odbinfo.reader import read_metadata


# pylint:disable=unused-argument
def test_read_metadata(libreoffice):  # pylint:disable=redefined-outer-name
    """ make fixture """
    dsource = datasource()
    metadata = read_metadata(dsource, DEFAULT_TESTDB)
    outdir = TEST_OUTPUT.format("")
    with open(f"{outdir}/metadata.pickle", "wb") as out:
        pickle.dump(metadata, out)
