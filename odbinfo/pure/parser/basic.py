""" Facade for the OOBasicParser """
import antlr4
from antlr4 import CommonTokenStream, InputStream

from odbinfo.pure.datatype import Callable, Token
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.pure.parser.scanner import Scanner


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

    def _find_callable(self) -> Callable:
        for index in range(self.cursor, self.tokens_length):
            self.set_cursor(index)
            start_callable = index
            if self.oneof([OOBasicLexer.GLOBAL,
                           OOBasicLexer.PUBLIC,
                           OOBasicLexer.PRIVATE]):
                if not self.eat(OOBasicLexer.WS):
                    continue
            self.maybe_seq([OOBasicLexer.STATIC, OOBasicLexer.WS])
            if self.oneof([OOBasicLexer.FUNCTION, OOBasicLexer.SUB]):
                if not self.eat(OOBasicLexer.WS):
                    continue
                id_token = self.eat(OOBasicLexer.IDENTIFIER)
                # print("Function id: ", id_token)
                if id_token:
                    name = id_token.text
                    # continue to NEWLINE to find body
                    if not self.find_oneof([OOBasicLexer.NEWLINE]):
                        raise RuntimeError(f"Newline not found in module: "
                                           f"{self.module}"
                                           f"library: {self.library}")
                    start_body = self.cursor
                    if not self.find_oneof([OOBasicLexer.END_SUB,
                                            OOBasicLexer.END_FUNCTION]):
                        raise RuntimeError("No callable end found in module: "
                                           f"{self.module}"
                                           f"library: {self.library}")
                    end_callable = self.cursor - 1
                    start_callable_index = self.tokens[start_callable].index
                    end_callable_index = self.tokens[end_callable].index

                    result = Callable(self.library,
                                      self.module,
                                      name)
                    result.tokens = self.alltokens[start_callable_index:
                                                   end_callable_index + 1]
                    result.body_tokens =\
                        self.tokens[start_body:
                                    end_callable]

                    return result

        return None

    def scan(self):
        "perform the scan"
        callables = []
        while True:
            acallable = self._find_callable()
            if acallable is None:
                break
            callables.append(acallable)

        return callables


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
