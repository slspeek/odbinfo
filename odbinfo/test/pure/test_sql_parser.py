" sql parser tests "
from odbinfo.pure.parser.sql import parse


def test_parse():
    " call parse "
    parse("")


def test_parse_select():
    " call parse select"
    parse('select * from "table", "second_table", (select * from "foo")')


def test_parse_error():
    " call parse select"
    parse('select * fom "table"')
