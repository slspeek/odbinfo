""" scanner tests """
import pytest

from odbinfo.pure.datatype import Token
from odbinfo.pure.parser.basic import get_basic_tokens
from odbinfo.pure.parser.scanner import (ParserError, Scanner, a, anyof, find,
                                         just, maybe)


def get_token(text: str, token_type: int):
    """Constructs a token with some defaults """
    return Token(text, token_type, 0, False)


def test_just():
    """ test just combinator """
    token = get_token("Sub", 0)
    tokens = [token]
    scanner = Scanner(tokens)
    result = just(0)(scanner)
    assert result == token


def test_a():
    """ test a combinator """
    token0 = get_token("Sub", 0)
    token1 = get_token("Foo", 1)
    tokens = [token0, token1]
    scanner = Scanner(tokens)
    result = a(0, 1)(scanner)
    assert result == tokens

    scanner = Scanner(tokens)
    with pytest.raises(ParserError):
        a(0, 0)(scanner)

    scanner = Scanner(tokens)
    assert not maybe(0, 0)(scanner)
    assert scanner.cursor == 0

    scanner = Scanner(tokens)
    assert a(0, anyof(0, 1))(scanner) == tokens


def test_find_found():
    """test find"""
    token0 = get_token(" ", 2)
    token1 = get_token("Sub", 0)
    token2 = get_token("Foo", 1)
    tokens = [token0, token1, token2]
    scanner = Scanner(tokens)

    assert find(2, 0)(scanner) == [token0, token1]
    assert scanner.cursor == 2


def new_scanner(source: str) -> Scanner:
    """Instantiates ModuleScanner on `source`"""
    tokens = get_basic_tokens(source)
    return Scanner(tokens)


def test_empty_input():
    """ on [] """
    scanner = Scanner([])
    scanner.step()
    assert scanner.cursor == 0
