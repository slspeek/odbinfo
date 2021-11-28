""" Test the reader and create fixture(s) """
# Introduce data_regression and file_regression
# dbs in shared_datadir, as they may not be touched
# remove use of metadata fixtures, libreoffice should become document fixtures
#
import dataclasses
import pickle
from pathlib import Path
from urllib.parse import urlparse

import pytest

from odbinfo.oo.core import set_configuration_defaults
from odbinfo.oo.reader import read_metadata
from odbinfo.pure.datatype.config import get_configuration


def read_metadata_in_test(testdb_doc, monkeypatch, benchmark):
    """read_metadata in test setting"""
    dsource = testdb_doc.DataSource
    dbpath = Path(urlparse(testdb_doc.URL).path)
    # This is to makes sure the /tmp/.. path does not show in the data
    workdir = dbpath.parent
    dbfilename = Path(".") / dbpath.name
    monkeypatch.chdir(workdir)
    config = get_configuration()
    set_configuration_defaults(config, dbfilename)
    return benchmark(read_metadata, config, dsource, dbfilename)


# pylint:disable=too-many-arguments
def read_metadata_regression_test(testdb_doc, filename, data_regression,
                                  file_regression, monkeypatch,
                                  benchmark):
    """ runs read_metadata and asserts nothing changed """
    metadata_read = read_metadata_in_test(testdb_doc, monkeypatch, benchmark)
    data_regression.check(dataclasses.asdict(metadata_read))
    file_regression.check(pickle.dumps(metadata_read),
                          binary=True, extension=".pickle", basename=filename)


# pylint:disable=too-many-arguments


@pytest.mark.veryslow
def test_metadata_regression(testdb_doc, data_regression,
                             file_regression, monkeypatch,
                             benchmark):
    """ test read_metadata for regression """
    read_metadata_regression_test(testdb_doc, "metadata",
                                  data_regression, file_regression, monkeypatch,
                                  benchmark)


# pylint:disable=too-many-arguments


@pytest.mark.veryslow
def test_metadata_regression_empty(emptydb_doc, data_regression,
                                   file_regression, monkeypatch,
                                   benchmark):
    """ test read_metadata for regression """
    read_metadata_regression_test(emptydb_doc, "empty-metadata",
                                  data_regression, file_regression, monkeypatch,
                                  benchmark)
