""" Reader tests """
import json

from test.resource import DEFAULT_TESTDB
from odbinfo.reader import _read_from_odb, _forms_index, _forms


def test_read_from_db():
    " _read_from_db "
    info = _read_from_odb(DEFAULT_TESTDB, "content.xml")
    info = info["office:document-content"]["office:body"]
    print(json.dumps(info, indent=4))


def test_forms_index():
    " _forms_index "
    info = _forms_index(DEFAULT_TESTDB)
    print(json.dumps(info, indent=4))


def test_forms():
    " _forms  "
    info = _forms(DEFAULT_TESTDB)
    for _, form in info:
        print(json.dumps(form, indent=4))
