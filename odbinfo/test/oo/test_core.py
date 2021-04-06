""" test site creation """
import logging

import pytest

from odbinfo.oo.core import generate_report
from odbinfo.test.oo.connect import libreoffice  # pylint:disable=unused-import
from odbinfo.test.oo.connect import oodocument

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.DEBUG)


@pytest.mark.slow
# pylint:disable=unused-argument
def test_generate_report(libreoffice):  # pylint:disable=redefined-outer-name
    """ test generate-site """
    oodoc = oodocument()
    generate_report(oodoc)
