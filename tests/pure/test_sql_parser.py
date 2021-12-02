""" sql parser tests """
import pytest

from odbinfo.pure.parser.sql import parse


@pytest.mark.slow
def test_parse():
    """ call parse """
    parse("")


@pytest.mark.slow
def test_parse_outer_join_escape():
    """ outer join escape """
    outer_join_escape = """
    SELECT "personer"."foretag", "personer"."fnamn", "personer"."enamn",
    "befattningnamn"."namn" FROM  { OJ "public"."befattning" "befattning"
    LEFT OUTER JOIN "public"."personer" "personer" ON
    "befattning"."personid" = "personer"."personid" },
    "public"."kommentar" "kommentar", "public"."personer" "personer",
    "public"."befattning" "befattning",   "public"."befattningnamn"
    "befattningnamn" WHERE  0 = 1
    """
    parse(outer_join_escape)


@pytest.mark.slow
def test_parse_select():
    """ call parse select"""
    parse('select * from "table", "second_table", (select * from "foo")')


@pytest.mark.slow
def test_parse_error():
    """ call parse select"""
    assert len(parse('select * fom "table"')[1]) == 0


@pytest.mark.slow
@pytest.mark.parametrize("specifier", ["", "both", "leading", "trailing"])
def test_parse_trim(specifier):
    """ call parse trim(from 'foo')"""
    assert len(
        parse(f'select trim({specifier} from "name") from "table"')[1]) == 1


@pytest.mark.slow
@pytest.mark.parametrize("specifier", ["year", "month", "day",
                                       "hour", "minute", "second"])
def test_parse_extract(specifier):
    """ call parse extract(from)"""
    assert len(
        parse(f'select extract({specifier} from "datefield") from "table"')[1]) == 1


@pytest.mark.slow
def test_parse_position():
    """position(in)"""
    assert len(
        parse('select position("foo" in "foobar") from "table"')[1]) == 1


@pytest.mark.slow
@pytest.mark.parametrize("forclause", ["", "FOR 3"])
def test_parse_substring(forclause):
    """substring(from for)"""
    assert len(
        parse(f'select substring("name" FROM 1 {forclause}) from "table"')[1]) == 1
