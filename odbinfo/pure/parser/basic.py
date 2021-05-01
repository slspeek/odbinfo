""" Hand crafted scanner on the the tokones of OOBasicLexer """

import antlr4
from antlr4 import CommonTokenStream, InputStream

from odbinfo.pure.datatype import Callable, Token
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.pure.parser.scanner import (Scanner, a, anyof, find, maybe, skip,
                                         someof)


def scan_basic(basiccode, library, module) -> [str]:
    " extract procedure names "
    alltokens = get_basic_tokens(basiccode)
    tokens = list(filter(lambda x: not x.hidden, alltokens))
    scanner = BasicScanner(tokens, alltokens, library, module)
    return scanner.scan()


# pylint:disable=too-few-public-methods
class BasicScanner(Scanner):
    "scan for procedure names"

    def __init__(self, tokens, alltokens, library, module):
        super().__init__(tokens)
        self.alltokens = alltokens
        self.library = library
        self.module = module

    # pylint: disable=too-many-arguments
    def _callable(self, start, bodystart, bodyend, end, name):
        acallable = Callable(self.library, self.module, name)
        acallable.body_tokens = self.tokens[bodystart:bodyend]

        bodyscanner = BodyScanner(acallable.body_tokens)
        acallable.calls = bodyscanner.functioncalls()

        acallable.strings = list(
            filter(
                lambda t: t.type == OOBasicLexer.STRINGLITERAL,
                acallable.body_tokens)
        )

        start_index = self.tokens[start].index
        end_index = self.tokens[end - 1].index
        acallable.tokens = self.alltokens[start_index:end_index + 1]
        return acallable

    def scan(self):
        "perform the scan"
        callables = []
        callable_infos = allmacros(self)
        if callable_infos:
            for callable_info in callable_infos:
                acallable = self._callable(*callable_info)
                callables.append(acallable)
        return callables


def signature(parser) -> (int, int, [Token]):
    " recognize macro signature "
    start = parser.cursor
    result = a(skip(maybe(anyof(OOBasicLexer.GLOBAL,
                                OOBasicLexer.PUBLIC,
                                OOBasicLexer.PRIVATE), OOBasicLexer.WS)),
               skip(maybe(OOBasicLexer.STATIC, OOBasicLexer.WS)),
               skip(anyof(OOBasicLexer.FUNCTION, OOBasicLexer.SUB)),
               skip(OOBasicLexer.WS),
               OOBasicLexer.IDENTIFIER,
               skip(find(OOBasicLexer.NEWLINE)))(parser)
    id_token = result[0]
    end = parser.cursor
    return start, end, id_token.text


def macro(parser) -> (int, int, int, int, str):
    " recognize callable "

    amacro = a(signature, skip(find(anyof(OOBasicLexer.END_FUNCTION,
                                          OOBasicLexer.END_SUB))))(parser)
    end = parser.cursor
    start, sigend, name = amacro[0]
    return start, sigend, end - 1, end, name


def allmacros(parser) -> [(int, int, int, int, str)]:
    " find all macros "
    macros = maybe(someof(find(macro)))(parser)
    return macros


class BodyScanner(Scanner):
    "Scan for functioncalls"

    def functioncalls(self):
        "find all tokens in functioncalls"
        calls = all_functioncalls(self)
        if not calls:
            calls = []
        return calls


def all_functioncalls(parser):
    "find all functioncalls "
    return maybe(someof(find(functioncall)))(parser)


def functioncall(parser):
    " Parse a function call "
    tokens = a(maybe(OOBasicLexer.IDENTIFIER, skip(OOBasicLexer.DOT)),
               OOBasicLexer.IDENTIFIER,
               skip(maybe(OOBasicLexer.WS), OOBasicLexer.LPAREN))(parser)
    if len(tokens) == 2:
        return (tokens[0], tokens[1])
    if tokens:
        return (tokens[0], )
    return None


def get_basic_tokens(basiccode) -> [Token]:
    "Tokenize `basiccode`"
    input_stream = InputStream(basiccode)
    lexer = OOBasicLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()
    # exclude EOF token, by leaving the last token out
    atokens = stream.tokens[:-1]

    def convert_token(atoken) -> Token:
        hidden = atoken.channel == antlr4.Token.HIDDEN_CHANNEL
        return\
            Token(atoken.column,
                  atoken.line,
                  atoken.text,
                  atoken.type,
                  atoken.tokenIndex,
                  hidden
                  )
    return list(map(convert_token, atokens))
