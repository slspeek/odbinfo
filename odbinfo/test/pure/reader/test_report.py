" test report reading "
import dataclasses

import pytest

from odbinfo.pure.reader.report import read_reports
from odbinfo.test.pure.fixtures import empty_odbzip, odbzip


@pytest.mark.slow
def test_read_reports(odbzip, data_regression):
    " reports "
    data_regression.check(list(map(dataclasses.asdict, read_reports(odbzip))))


@pytest.mark.slow
def test_read_reports_empty(empty_odbzip, data_regression):
    " reports "
    data_regression.check(
        list(map(dataclasses.asdict, read_reports(empty_odbzip))))
