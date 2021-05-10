""" Hand crafted scanner on the the tokones of OOBasicLexer """

from antlr4 import CommonTokenStream, InputStream

from odbinfo.pure.datatype import BasicCall, Callable, Token
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.pure.parser.scanner import (Scanner, a, anyof, convert_token,
                                         find, maybe, skip, someof)


def scan_basic(alltokens, library, module) -> [str]:
    " extract procedure names "
    tokens = list(filter(lambda x: not x.hidden, alltokens))
    scanner = BasicScanner(tokens, alltokens, library, module)
    return scanner.scan()


def analyze_callable(acallable: Callable):
    "Extract and store functioncalls and stringliterals from the body"
    acallable.calls = extract_functioncalls(acallable)
    acallable.strings = extract_stringliterals(acallable)


def extract_functioncalls(acallable: Callable):
    "Extract functioncalls"
    return BodyScanner(acallable.body_tokens).functioncalls()


def extract_stringliterals(acallable: Callable) -> [str]:
    "Extract stringliterals"
    return list(
        filter(
            lambda t: t.type == OOBasicLexer.STRINGLITERAL,
            acallable.body_tokens)
    )


# pylint:disable=too-few-public-methods
class BasicScanner(Scanner):
    "scan for procedure names"

    def __init__(self, tokens, alltokens, library, module):
        super().__init__(tokens)
        self.alltokens = alltokens
        self.library = library
        self.module = module

    # pylint: disable=too-many-arguments
    def _callable(self, start, bodystart, bodyend, end, name_token):
        acallable = Callable(self.library, self.module, name_token.text)
        acallable.body_tokens = self.tokens[bodystart:bodyend]
        acallable.name_token_index = name_token.index

        start_index = self.tokens[start].index
        end_index = self.tokens[end - 1].index
        acallable.tokens = self.alltokens[start_index:end_index + 1]

        analyze_callable(acallable)
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
    return start, end, id_token


def macro(parser) -> (int, int, int, int, Token):
    " recognize callable "

    amacro = a(signature, skip(find(anyof(OOBasicLexer.END_FUNCTION,
                                          OOBasicLexer.END_SUB))))(parser)
    end = parser.cursor
    start, sigend, name_token = amacro[0]
    return start, sigend, end - 1, end, name_token


def allmacros(parser) -> [(int, int, int, int, Token)]:
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
        return BasicCall(tokens[1], tokens[0])
    return BasicCall(tokens[0], None)


def get_basic_tokens(basiccode) -> [Token]:
    "Tokenize `basiccode`"
    input_stream = InputStream(basiccode)
    lexer = OOBasicLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()
    # exclude EOF token, by leaving the last token out
    atokens = stream.tokens[:-1]

    return list(map(convert_token, atokens))
