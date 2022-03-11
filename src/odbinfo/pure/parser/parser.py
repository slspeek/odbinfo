""" Small parser combinator library adapted from
https://github.com/qweeze/python-parser/blob/master/python_parser/parser.py
"""
from typing import Callable, Optional, Sequence

from odbinfo.pure.datatype.base import BasicToken


class Parser:
    """ Holds parsing position """

    def __init__(self, tokens: Sequence[BasicToken]):
        self.tokens = tokens
        self.tokens_length = len(tokens)
        self.cur_token: Optional[BasicToken] = None
        self.set_cursor(0)

    def set_cursor(self, position: int):
        """ sets cur_token """
        self.cursor = position
        if position < self.tokens_length:
            self.cur_token = self.tokens[self.cursor]

    def _step(self):
        """ Go one token further"""
        if self.cur_token is not None:
            self.set_cursor(self.cursor + 1)

    def eat(self, token_type: int):
        """ consume token"""
        if self.cur_token is not None and self.cur_token.type == token_type:
            token = self.cur_token
            self._step()
            return token
        return None


class ParserError(Exception):
    """Parser error"""


def unify(*args):
    """ wrap non targets in a()"""
    args = (arg if callable(arg) else a(arg) for arg in args)
    return a(*args)


def just(token_type: int) -> Callable[[Parser], BasicToken]:
    """ just a token of type `type`"""

    def inner(parser: Parser) -> BasicToken:
        token = parser.eat(token_type)
        if token is None:
            raise ParserError
        return token

    return inner


def maybe(*args):
    """ maybe read `args`"""

    def inner(parser: Parser):
        mark = parser.cursor
        result = None
        try:
            result = unify(*args)(parser)
        except ParserError:
            parser.set_cursor(mark)
        return result

    return inner


def skip(*args):
    """ skip `args` """

    def inner(parser: Parser):
        unify(*args)(parser)

    return inner


def anyof(*args):
    """ eat any of `args`"""

    def inner(parser: Parser):
        for arg in args:
            result = maybe(arg)(parser)
            if result:
                return result
        raise ParserError

    return inner


def someof(*args):
    """eat one or more `args`"""

    def inner(parser: Parser):
        result = unify(*args)(parser)
        while True:
            part = maybe(unify(*args))(parser)
            if part:
                result.extend(part)
            else:
                break
        return result

    return inner


# pylint: disable=invalid-name
def a(*args):
    """eat `args`"""

    def inner(parser: Parser):
        result = []
        for arg in args:
            if isinstance(arg, int):
                arg = just(arg)
            parse_result = arg(parser)
            if parse_result is not None:
                if not isinstance(parse_result, list):
                    result.append(parse_result)
                else:
                    result.extend(parse_result)
        return result

    return inner


def find(*args):
    """ scan for `args`"""

    def inner(parser: Parser):
        mark = parser.cursor
        for cursor in range(parser.cursor, parser.tokens_length):
            result = []
            parser.set_cursor(cursor)
            found = maybe(*args)(parser)
            if not found:
                continue
            result.extend(found)
            return result
        parser.set_cursor(mark)
        raise ParserError

    return inner
