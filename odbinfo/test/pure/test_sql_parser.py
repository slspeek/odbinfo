" sql parser tests "
import pytest

from odbinfo.pure.parser.sql import parse


def test_parse():
    " call parse "
    parse("")


def test_parse_select():
    " call parse select"
    parse('select * from "table", "second_table", (select * from "foo")')


def test_parse_error():
    " call parse select"
    assert len(parse('select * fom "table"')[0]) == 0


@pytest.mark.parametrize("specifier", ["", "both", "leading", "trailing"])
def test_parse_trim(specifier):
    " call parse trim(from 'foo')"
    assert len(
        parse(f'select trim({specifier} from "name") from "table"')[0]) == 1


@pytest.mark.parametrize("specifier", ["year", "month", "day",
                                       "hour", "minute", "second"])
def test_parse_extract(specifier):
    " call parse extract(from)"
    assert len(
        parse(f'select extract({specifier} from "datefield") from "table"')[0]) == 1


def test_parse_position():
    "position(in)"
    assert len(
        parse('select position("foo" in "foobar") from "table"')[0]) == 1


@pytest.mark.parametrize("forclause", ["", "FOR 3"])
def test_parse_substring(forclause):
    "substring(from for)"
    assert len(
        parse(f'select substring("name" FROM 1 {forclause}) from "table"')[0]) == 1
