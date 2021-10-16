" test report reading "
import json

import pytest

from odbinfo.pure.reader.report import _reports, read_reports
from odbinfo.test.pure.fixtures import empty_odbzip, odbzip


@pytest.mark.slow
def test_reports(odbzip):
    " _reports  "
    info = _reports(odbzip)
    for _, form in info:
        # print(name,
        json.dumps(form, indent=4)
        # )


@pytest.mark.slow
def test_reports_empty(empty_odbzip):
    " _reports  "
    info = _reports(empty_odbzip)
    for _, form in info:
        # print(name,
        json.dumps(form, indent=4)
        # )


@pytest.mark.slow
def test_read_reports(odbzip):
    " reports "
    read_reports(odbzip)
