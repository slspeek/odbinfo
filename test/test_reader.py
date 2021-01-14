""" Reader tests """
import json

from test.resource import DEFAULT_TESTDB
from odbinfo.reader import _forms, read_forms


def test_forms():
    " _forms  "
    info = _forms(DEFAULT_TESTDB)
    for _, form in info:
        print(json.dumps(form, indent=4))


def test_read_forms():
    " read_forms  "
    info = read_forms(DEFAULT_TESTDB)
    for form in info:
        print(form)
