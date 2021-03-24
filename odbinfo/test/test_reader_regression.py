""" Test the reader and create fixture(s) """
import pickle

import pytest

from odbinfo.reader import read_metadata
from odbinfo.test.connect import libreoffice  # pylint:disable=unused-import
from odbinfo.test.connect import datasource
from odbinfo.test.resource import DEFAULT_TESTDB, FIXTURE_DIR


# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name
@pytest.mark.slow
def test_metadata_regression(libreoffice):
    """ make fixture """
    dsource = datasource()
    metadata = read_metadata(dsource, DEFAULT_TESTDB)
    with open(FIXTURE_DIR.format("metadata.pickle"), "rb") as file:
        metadata_before = pickle.load(file)
        assert metadata == metadata_before
    print(metadata)
