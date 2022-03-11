""" In house parser on the the tokens provided by OOBasicLexer
    (becouse the ANTLR parser is too slow)
 """
from typing import List, Tuple

from odbinfo.pure.datatype.base import BasicToken
from odbinfo.pure.datatype.basicfunction import BasicCall, BasicFunction
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.pure.parser.parser import (Parser, a, anyof, find, maybe, skip,
                                        someof)
from odbinfo.pure.parser.tokenizer import get_token_stream, get_tokens


def extract_functioncalls(acallable: BasicFunction):
    """Extract functioncalls"""
    return FunctionBodyParser(acallable.body_tokens).functioncalls()


def extract_stringliterals(acallable: BasicFunction) -> List[BasicToken]:
    """Extract stringliterals"""
    return list(
        filter(lambda t: t.type == OOBasicLexer.STRINGLITERAL,
               acallable.body_tokens))


def analyze_callable(acallable: BasicFunction):
    """Extract and store functioncalls and stringliterals from the body"""
    acallable.calls = extract_functioncalls(acallable)
    acallable.strings = extract_stringliterals(acallable)


class FunctionBodyParser(Parser):
    """Scan for functioncalls"""

    def functioncalls(self) -> List[BasicCall]:
        """find all tokens in functioncalls"""
        calls = all_functioncalls(self)
        if not calls:
            calls = []
        return calls


def functioncall(parser: FunctionBodyParser):
    """ Parse a function call """
    tokens = a(maybe(OOBasicLexer.IDENTIFIER, skip(OOBasicLexer.DOT)),
               OOBasicLexer.IDENTIFIER,
               skip(maybe(OOBasicLexer.WS), OOBasicLexer.LPAREN))(parser)
    if len(tokens) == 2:
        return BasicCall(name_token=tokens[1], module_token=tokens[0])
    return BasicCall(name_token=tokens[0], module_token=None)


def all_functioncalls(parser: FunctionBodyParser):
    """find all functioncalls """
    return maybe(someof(find(functioncall)))(parser)


def get_basic_tokens(basiccode) -> List[BasicToken]:
    """ Tokenize `basiccode` """
    return get_tokens(get_token_stream(basiccode, OOBasicLexer), BasicToken)


# pylint:disable=too-few-public-methods
class ModuleParser(Parser):
    """Looks for basic functions"""

    def __init__(self, tokens: List[BasicToken], alltokens: List[BasicToken],
                 library: str, module: str):
        super().__init__(tokens)
        self.alltokens: List[BasicToken] = alltokens
        self.library = library
        self.module = module

    # pylint: disable=too-many-arguments
    def _create_basicfunction(self, start: int, bodystart: int, bodyend: int,
                              end: int,
                              name_token: BasicToken) -> BasicFunction:
        _basicfunction = BasicFunction(name=name_token.text,
                                       library=self.library,
                                       module=self.module)
        _basicfunction.body_tokens = list(self.tokens[bodystart:bodyend])
        _basicfunction.name_token_index = name_token.index

        start_index = self.tokens[start].index
        end_index = self.tokens[end - 1].index
        _basicfunction.tokens = list(self.alltokens[start_index:end_index + 1])

        analyze_callable(_basicfunction)
        return _basicfunction

    def parse(self) -> List[BasicFunction]:
        """Performs the parsing and returns a list of BasicFunctions"""
        callables = []
        callable_infos = all_basicfunctions(self)
        if callable_infos:
            for callable_info in callable_infos:
                acallable = self._create_basicfunction(*callable_info)
                callables.append(acallable)
        return callables


def function_signature(parser: ModuleParser) -> Tuple[int, int, BasicToken]:
    """ Recognizes basicfunction signature.
        Returns a tuple with the starting position, the end position and the Token
        containing the function name """
    start_pos = parser.cursor
    result = a(
        skip(
            maybe(
                anyof(OOBasicLexer.GLOBAL, OOBasicLexer.PUBLIC,
                      OOBasicLexer.PRIVATE), OOBasicLexer.WS)),
        skip(maybe(OOBasicLexer.STATIC, OOBasicLexer.WS)),
        skip(anyof(OOBasicLexer.FUNCTION, OOBasicLexer.SUB)),
        skip(OOBasicLexer.WS), OOBasicLexer.IDENTIFIER,
        skip(find(OOBasicLexer.NEWLINE)))(parser)
    id_token = result[0]
    end_pos = parser.cursor - 1
    return start_pos, end_pos, id_token


def basicfunction(
        parser: ModuleParser) -> Tuple[int, int, int, int, BasicToken]:
    """ Recognizes basicfunction and returns
        a tuple with starting position, the starting position of the function
        body, the end position of the function body, the end position of the
        basicfunction and the Token containing the function name"""

    amacro = a(
        function_signature,
        skip(find(anyof(OOBasicLexer.END_FUNCTION,
                        OOBasicLexer.END_SUB))))(parser)

    function_end_pos = parser.cursor
    signature_start_pos, signature_end_pos, name_token = amacro[0]

    body_start_pos = signature_end_pos + 1
    body_end_pos = function_end_pos - 1
    return signature_start_pos, body_start_pos, body_end_pos, function_end_pos, name_token


def all_basicfunctions(
        parser: ModuleParser) -> List[Tuple[int, int, int, int, BasicToken]]:
    """ find all basic functions """
    macros = maybe(someof(find(basicfunction)))(parser)
    return macros


def parse_basic(alltokens: List[BasicToken], library: str,
                module: str) -> List[BasicFunction]:
    """ Creates a list of BasicFunctions parsed from `alltokens` """
    tokens = [token for token in alltokens if not token.hidden]
    parser = ModuleParser(tokens, alltokens, library, module)
    return parser.parse()
