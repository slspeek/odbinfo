""" Generic token scanner """
from odbinfo.pure.datatype import Token


class Scanner:
    " Holds position "

    def __init__(self, tokens: [Token]):
        self.tokens = tokens
        self.tokens_length = len(tokens)
        self.cursor = 0
        self.cur_token = None
        self.set_cursor(0)

    def eat(self, token_type):
        " consume token"
        if self.cur_token is not None and self.cur_token.type == token_type:
            token = self.cur_token
            self.step()
            return token
        return None

    def set_cursor(self, position: int):
        " set cur_node "
        if position < self.tokens_length:
            self.cursor = position
            self.cur_token = self.tokens[self.cursor]

    def step(self):
        " Go one token further"
        if self.cur_token is not None:
            self.cursor += 1
            self.set_cursor(self.cursor)


class ParserError(Exception):
    "Parser error"


def unify(*args):
    " wrap non callables in a()"
    args = (arg if callable(arg) else a(arg) for arg in args)
    return a(*args)


def just(token_type):
    " just a token of type `type`"
    def inner(parser):
        token = parser.eat(token_type)
        if token is None:
            raise ParserError
        return token
    return inner


def maybe(*args):
    " maybe read `args`"
    def inner(parser):
        mark = parser.cursor
        result = None
        try:
            result = unify(*args)(parser)
        except ParserError:
            parser.set_cursor(mark)
        return result
    return inner


def skip(*args):
    " skip `args` "
    def inner(parser):
        unify(*args)(parser)
    return inner


def anyof(*args):
    " eat any of `args`"
    def inner(parser):
        for arg in args:
            result = maybe(arg)(parser)
            if result:
                return result
        raise ParserError
    return inner


def someof(*args):
    "eat one or more `args`"
    def inner(parser):
        result = unify(*args)(parser)
        while True:
            part = maybe(unify(*args))(parser)
            if part:
                result.extend(part)
            else:
                break
        return result
    return inner

#pylint: disable=invalid-name


def a(*args):
    "eat `args`"
    def inner(parser):
        result = []
        for arg in args:
            if isinstance(arg, int):
                arg = just(arg)
            arg = arg(parser)
            if arg is not None:
                if not isinstance(arg, list):
                    result.append(arg)
                else:
                    result.extend(arg)
        return result
    return inner


def find(*args):
    " look for `args`"
    def inner(parser):
        mark = parser.cursor
        for cursor in range(parser.cursor, len(parser.tokens)):
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
