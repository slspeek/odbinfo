""" Facade fot the OOBasicParser """
from antlr4 import InputStream, CommonTokenStream,\
    ParseTreeWalker
import antlr4
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener
from antlr4.atn.PredictionMode import PredictionMode
from odbinfo.parser.oobasic.OOBasicParser import OOBasicParser
from odbinfo.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.parser.oobasic.OOBasicListener import\
    OOBasicListener
from odbinfo.datatype import Callable, Token


class BasicListener(OOBasicListener):
    "Collect tablenames"

    def __init__(self, library, module):
        super().__init__()
        self.library = library
        self.module = module
        self.callables = []
        self.cur_callable = None

    def _set_cur_callable(self, function):
        self.cur_callable = function
        if self.cur_callable is not None:
            self.callables.append(function)

    def enterFunctionStmt(self, ctx):
        bcallable = Callable(self.library,
                             self.module,
                             ctx.ambiguousIdentifier().getText(),
                             ctx.getText())
        self._set_cur_callable(bcallable)

    def exitFunctionStmt(self, ctx):
        self._set_cur_callable(None)

    def enterSubStmt(self, ctx):
        self.enterFunctionStmt(ctx)

    def exitSubStmt(self, ctx):
        self.exitFunctionStmt(ctx)

    def _add_call(self, callee):
        if self.cur_callable is not None:
            if self.cur_callable.name != callee:
                self.cur_callable.callees.add(callee)

    # call graph collection of callees
    def enterECS_ProcedureCall(self, ctx):
        self._add_call(ctx.ambiguousIdentifier().getText())

    def enterECS_MemberProcedureCall(self, ctx):
        self._add_call(ctx.ambiguousIdentifier().getText())

    def enterICS_B_ProcedureCall(self, ctx):
        self._add_call(ctx.certainIdentifier().getText())

    def enterICS_B_MemberProcedureCall(self, ctx):
        self._add_call(ctx.ambiguousIdentifier().getText())

    def enterICS_S_VariableOrProcedureCall(self, ctx):
        self._add_call(ctx.ambiguousIdentifier().getText())

    def enterICS_S_NestedProcedureCall(self, ctx):
        self._add_call(ctx.ambiguousIdentifier().getText())

    def enterIcsAmbiguousIdentifier(self, ctx):
        self._add_call(ctx.ambiguousIdentifier().getText())

# pylint:disable=too-few-public-methods


class ThrowingErrorListener(ErrorListener):
    " An ErrorListeners that raises an Error"

    # pylint:disable=too-many-arguments
    # pylint:disable=invalid-name
    # pylint:disable=no-self-use
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        "raise the error"
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: ", str(stack))
        print("line", line, ":", column, "at", offendingSymbol, ":", msg)
        raise RuntimeError("Parse failed")


def scan_basic(basiccode) -> [str]:
    " extract procedure names "
    tokens = get_basic_tokens(basiccode)
    # print(tokens)
    index = 0
    while True:
        name, index, start, stop = _find_callable(tokens, index)
        print(name, index, start, stop)
        if name is None:
            break


def _proceed_visibility(tokens, index) -> int:
    i = index
    atoken = tokens[i]
    if atoken.type in [OOBasicLexer.GLOBAL,
                       OOBasicLexer.PUBLIC,
                       OOBasicLexer.PRIVATE]:
        i += 1
        atoken = tokens[i]
        if atoken.type == OOBasicLexer.WS:
            return i + 1
    return index


def _proceed_static(tokens, index) -> int:
    i = index
    atoken = tokens[i]
    if atoken.type == OOBasicLexer.STATIC:
        i += 1
        atoken = tokens[i]
        if atoken.type == OOBasicLexer.WS:
            return i + 1
    return index


def _proceed_callable(tokens, index) -> int:
    i = index
    atoken = tokens[i]
    if atoken.type in [OOBasicLexer.SUB,
                       OOBasicLexer.FUNCTION]:
        i += 1
        atoken = tokens[i]
        if atoken.type == OOBasicLexer.WS:
            i += 1
            atoken = tokens[i]
            if atoken.type == OOBasicLexer.IDENTIFIER:
                name = atoken.text
                # continue to NEWLINE to find body
                found, i = _find(tokens, i, [OOBasicLexer.NEWLINE])
                if not found:
                    raise RuntimeError("Newline not found")
                body_start = i
                found, i = _find(tokens, i, [OOBasicLexer.END_SUB,
                                             OOBasicLexer.END_FUNCTION])
                if not found:
                    raise RuntimeError("No callable end found")
                body_end = i
                return (name, i, body_start, body_end)

    return (None, index, -1, -1)


def _find(tokens, index, types: [int]) -> (bool, int):
    for i in range(index, len(tokens)):
        atoken = tokens[i]
        if atoken.type in types:
            return (True, i)
    return (False, i)


def _find_callable(tokens, index) -> (str, int):
    for i in range(index, len(tokens)):
        i = _proceed_visibility(tokens, i)
        i = _proceed_static(tokens, i)
        name, i, start, stop = _proceed_callable(tokens, i)
        if name is not None:
            return (name, i, start, stop)
    return (None, i, -1, -1)


def get_basic_tokens(basiccode) -> [Token]:
    "Tokenize `basiccode`"
    input_stream = InputStream(basiccode)
    lexer = OOBasicLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.setup()
    stream.fill()
    tokens = []
    i = 0
    while True:
        i = stream.nextTokenOnChannel(i, antlr4.Token.DEFAULT_CHANNEL)
        atoken = stream.get(i)
        tokens.append(Token(atoken.column,
                            atoken.line,
                            atoken.text,
                            atoken.type))
        if atoken.type == antlr4.Token.EOF:
            break
        i += 1
    return tokens


def parse(basiccode, library, module, diagnostic=False) -> [Callable]:
    " Returns callables "
    input_stream = InputStream(basiccode)
    lexer = OOBasicLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OOBasicParser(stream)
    parser.removeErrorListeners()
    if diagnostic:
        parser.addErrorListener(DiagnosticErrorListener())
        # pylint:disable=protected-access
        parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION
    else:
        parser.addErrorListener(ThrowingErrorListener())
    tree = parser.startRule()
    walker = ParseTreeWalker()
    listener = BasicListener(library, module)
    walker.walk(listener, tree)

    return listener.callables
