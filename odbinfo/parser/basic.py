""" Facade fot the OOBasicParser """
from antlr4 import InputStream, CommonTokenStream,\
    ParseTreeWalker
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


def get_basic_tokens(basiccode) -> [Token]:
    "Tokenize `basiccode`"
    input_stream = InputStream(basiccode)
    lexer = OOBasicLexer(input_stream)
    stream = CommonTokenStream(lexer)
    tokens = []
    for i in range(stream.getNumberOfOnChannelTokens()):
        atoken = stream.get(i)
        if atoken.type != -1:
            tokens.append(Token(atoken.column,
                                atoken.line,
                                atoken.text,
                                atoken.type))
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
