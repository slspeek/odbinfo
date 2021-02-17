""" test site creation """
import os
import logging

from pytest import fixture
import pytest

from odbinfo.writer import new_site
from odbinfo.core import generate_report
from odbinfo.test.connect import start_office, oodocument
from odbinfo.test.resource import TEST_OUTPUT, DEFAULT_TESTDB

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.DEBUG)


@pytest.mark.slow
def test_new_site():
    """ test new site scaffolding """
    result = new_site(TEST_OUTPUT.format(""), "test-site")
    assert result == os.path.join(TEST_OUTPUT.format(""), "test-site")


@pytest.mark.slow
# pylint:disable=unused-argument
def test_generate_report(libreoffice):  # pylint:disable=redefined-outer-name
    """ test generate-site """
    oodoc = oodocument()
    generate_report(oodoc)


@fixture(scope="session")
def libreoffice():
    """ A libreoffice running on a test repository """
    testdb = os.getenv("ODBINFO_TESTDB", DEFAULT_TESTDB)
    office_proc = start_office(testdb)
    yield office_proc
    office_proc.terminate()
    logger.debug("LibreOffice killed")
