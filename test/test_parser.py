" parser tests "
from odbinfo.parser.sql import parse


def test_parse():
    " call parse "
    parse("")


def test_parse_select():
    " call parse select"
    parse('select * from "table"')


def test_parse_error():
    " call parse select"
    parse('select * fom "table"')
