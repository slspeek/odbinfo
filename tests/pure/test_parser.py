""" scanner tests """
import pytest

from odbinfo.pure.datatype.base import BasicToken
from odbinfo.pure.parser.basic import get_basic_tokens
from odbinfo.pure.parser.parser import (Parser, ParserError, a, anyof, find,
                                        just, maybe)


def create_token(text: str, token_type: int):
    """Constructs a token with some defaults """
    return BasicToken(text, token_type, 0, False)


def test_just():
    """ test just combinator """
    token = create_token("Sub", 0)
    tokens = [token]
    parser = Parser(tokens)
    result = just(0)(parser)
    assert result == token


def test_a():
    """ test a combinator """
    token0 = create_token("Sub", 0)
    token1 = create_token("Foo", 1)
    tokens = [token0, token1]
    parser = Parser(tokens)
    result = a(0, 1)(parser)
    assert result == tokens

    parser = Parser(tokens)
    with pytest.raises(ParserError):
        a(0, 0)(parser)

    parser = Parser(tokens)
    assert not maybe(0, 0)(parser)
    assert parser.cursor == 0

    parser = Parser(tokens)
    assert a(0, anyof(0, 1))(parser) == tokens


def test_find_found():
    """test find"""
    token0 = create_token(" ", 2)
    token1 = create_token("Sub", 0)
    token2 = create_token("Foo", 1)
    tokens = [token0, token1, token2]
    scanner = Parser(tokens)

    assert find(2, 0)(scanner) == [token0, token1]
    assert scanner.cursor == 2


def create_scanner(source: str) -> Parser:
    """Instantiates ModuleScanner on `source`"""
    tokens = get_basic_tokens(source)
    return Parser(tokens)


def test_empty_input():
    """ on [] """
    parser = Parser([])
    parser._step()
    assert parser.cursor == 0
