""" Reader tests """
import json

from test.resource import DEFAULT_TESTDB
from odbinfo.reader import _forms, read_forms, _read_subforms


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


def test_read_form():
    " _read_form  "
    info = _forms(DEFAULT_TESTDB)
    for _, frmdata in info:
        forms = _read_subforms(frmdata)
        print(forms)
