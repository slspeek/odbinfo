""" test site creation """
import logging
import os

import pytest

from odbinfo.oo.core import generate_report
from odbinfo.test.connect import libreoffice  # pylint:disable=unused-import
from odbinfo.test.connect import oodocument
from odbinfo.test.resource import TEST_OUTPUT
from odbinfo.writer import new_site

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
