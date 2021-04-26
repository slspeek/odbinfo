""" Facade for the OOBasicParser """
import operator
from functools import reduce

import antlr4
from antlr4 import CommonTokenStream, InputStream

from odbinfo.pure.datatype import Callable, Token
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer


def scan_basic(basiccode, library, module) -> [str]:
    " extract procedure names "
    tokens = get_basic_tokens(basiccode, include_hidden=False)
    alltokens = get_basic_tokens(basiccode, include_hidden=True)
    scanner = BasicScanner(tokens, alltokens, library, module)
    return scanner.scan()


# pylint:disable=too-few-public-methods
class BasicScanner:
    "scan for procedure names"

    def __init__(self, tokens, alltokens, library, module):
        self.tokens = tokens
        self.alltokens = alltokens
        self.library = library
        self.module = module
        self.index = 0
        self.callables = []

    def _token(self) -> Token:
        return self.tokens[self.index]

    def _read(self, token: int) -> bool:
        if self._token().type == token:
            self.index += 1
            return True
        return False

    def _read_seq_maybe(self, seq: [int]):
        mark = self.index
        for token in seq:
            if not self._read(token):
                self.index = mark
                return

    def _read_or(self, ptokens: [int]) -> bool:
        for token in ptokens:
            if self._read(token):
                return True
        return False

    def _find_or(self, types: [int]) -> bool:
        mark = self.index
        for i in range(self.index, len(self.tokens)):
            self.index = i
            if self._token().type in types:
                return True
        self.index = mark
        return False

    def _find_callable(self) -> Callable:
        for index in range(self.index, len(self.tokens)):
            self.index = index
            start_callable = self.index
            if self._read_or([OOBasicLexer.GLOBAL,
                              OOBasicLexer.PUBLIC,
                              OOBasicLexer.PRIVATE]):
                if not self._read(OOBasicLexer.WS):
                    continue
            self._read_seq_maybe([OOBasicLexer.STATIC, OOBasicLexer.WS])
            if self._read_or([OOBasicLexer.FUNCTION, OOBasicLexer.SUB]):
                if not self._read(OOBasicLexer.WS):
                    continue
                if self._read(OOBasicLexer.IDENTIFIER):
                    name = self.tokens[self.index - 1].text
                    # continue to NEWLINE to find body
                    if not self._find_or([OOBasicLexer.NEWLINE]):
                        raise RuntimeError(f"Newline not found in module: "
                                           f"{self.module}"
                                           f"library: {self.library}")
                    body_start_after = self.index
                    if not self._find_or([OOBasicLexer.END_SUB,
                                          OOBasicLexer.END_FUNCTION]):
                        raise RuntimeError("No callable end found in module: "
                                           f"{self.module}"
                                           f"library: {self.library}")
                    body_end_before = self.index
                    start_callable_index = self.tokens[start_callable].index
                    body_start_index = self.tokens[body_start_after].index
                    body_end_index = self.tokens[body_end_before].index

                    source = reduce(operator.add,
                                    map(lambda x: x.text,
                                        self.alltokens[start_callable_index:
                                                       body_end_index + 1]),
                                    "")
                    result = Callable(self.library,
                                      self.module,
                                      name,
                                      source)
                    result.tokens = self.alltokens[start_callable_index:
                                                   body_end_index + 1]
                    result.body_tokens =\
                        self.tokens[body_start_after + 1:
                                    body_end_before]

                    result.body_source =\
                        reduce(operator.add,
                               map(lambda x: x.text,
                                   self.alltokens[body_start_index + 1:
                                                  body_end_index]
                                   ),
                               "")
                    return result

        return None

    def scan(self):
        "perform the scan"
        while True:
            acallable = self._find_callable()
            if acallable is None:
                break
            self.callables.append(acallable)

        return self.callables


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
