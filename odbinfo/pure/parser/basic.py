""" Facade for the OOBasicParser """
import antlr4
from antlr4 import CommonTokenStream, InputStream

from odbinfo.pure.datatype import Callable, Token
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.pure.parser.scanner import (Scanner, a, anyof, find, maybe, skip,
                                         someof)


def scan_basic(basiccode, library, module) -> [str]:
    " extract procedure names "
    tokens = get_basic_tokens(basiccode, include_hidden=False)
    alltokens = get_basic_tokens(basiccode, include_hidden=True)
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
                # start, bodystart, bodyend, end, name = callable_info
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
    # if not result:
    #     raise ParserError
    id_token = result[0]
    end = parser.cursor
    return start, end, id_token.text


def macro(parser) -> (int, int, int, int, str):
    " recognize callable "

    amacro = a(signature, skip(find(anyof(OOBasicLexer.END_FUNCTION,
                                          OOBasicLexer.END_SUB))))(parser)
    end = parser.cursor
    # if not amacro:
    #     raise ParserError
    start, sigend, name = amacro[0]
    return start, sigend, end - 1, end, name


def allmacros(parser) -> [(int, int, int, int, str)]:
    " find all macros "
    macros = maybe(someof(find(macro)))(parser)
    return macros


def get_basic_tokens(basiccode, include_hidden=False) -> [Token]:
    "Tokenize `basiccode`"
    def convert_token(atoken) -> Token:
        return\
            Token(atoken.column,
                  atoken.line,
                  atoken.text,
                  atoken.type,
                  atoken.tokenIndex
                  )

    input_stream = InputStream(basiccode)
    lexer = OOBasicLexer(input_stream)
    stream = CommonTokenStream(lexer)
    tokens = []
    i = 0
    while True:
        atokens = []
        i = stream.nextTokenOnChannel(i, antlr4.Token.DEFAULT_CHANNEL)
        atoken = stream.get(i)
        if include_hidden:
            hidden_tokens = stream.getHiddenTokensToLeft(i)
            if hidden_tokens:
                atokens.extend(hidden_tokens)
        if not atoken.type == antlr4.Token.EOF:
            atokens.append(atoken)
        tokens.extend(map(convert_token, atokens))
        if atoken.type == antlr4.Token.EOF:
            break
        i += 1
    return tokens
