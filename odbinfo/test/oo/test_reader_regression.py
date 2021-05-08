""" Test the reader and create fixture(s) """
# Introduce data_regression and file_regression
# dbs in shared_datadir, as they may not be touched
# remove use of metadata fixtures, libreoffice should become document fixtures
#
import dataclasses
import os
import pickle

import pytest

from odbinfo.oo.reader import read_metadata
from odbinfo.test.oo.connect import datasource, empty_libreoffice, libreoffice
from odbinfo.test.resource import DEFAULT_TESTDB, EMPTYDB


def read_metadata_in_test(dbpath):
    "read_metadata in test setting"
    dsource = datasource()
    return read_metadata(dsource, dbpath)


def read_metadata_regression_test(dbpath, filename, data_regression,
                                  file_regression, monkeypatch):
    " runs read_metadata and asserts nothing changed "
    workdir = os.path.dirname(dbpath)
    dbfilename = "./" + os.path.basename(dbpath)
    monkeypatch.chdir(workdir)
    metadata_read = read_metadata_in_test(dbfilename)
    data_regression.check(dataclasses.asdict(metadata_read))
    file_regression.check(pickle.dumps(metadata_read),
                          binary=True, extension=".pickle", basename=filename)


@pytest.mark.slow
def test_metadata_regression(libreoffice, data_regression,
                             file_regression, shared_datadir, monkeypatch):
    """ test read_metadata for regression """
    read_metadata_regression_test(str(shared_datadir / DEFAULT_TESTDB),
                                  "metadata", data_regression, file_regression, monkeypatch)


@pytest.mark.slow
def test_metadata_regression_empty(empty_libreoffice, data_regression,
                                   file_regression, shared_datadir, monkeypatch):
    """ test read_metadata for regression """
    read_metadata_regression_test(str(shared_datadir / EMPTYDB),
                                  "empty-metadata", data_regression, file_regression, monkeypatch)
