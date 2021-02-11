""" Facade fot the OOBasicParser """
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener
from antlr4.atn.PredictionMode import PredictionMode
from odbinfo.parser.oobasic.OOBasicParser import OOBasicParser
from odbinfo.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.parser.oobasic.OOBasicListener import\
    OOBasicListener


class BasicListener(OOBasicListener):
    "Collect tablenames"

    def __init__(self):
        super().__init__()
        self.functionnames = set()
        self.callgraph = {}
        self._set_cur_func("")

    def _set_cur_func(self, function):
        self.cur_func = function
        if self.cur_func != "":
            self.functionnames.add(function)
            self.callgraph[function] = set()

    def enterFunctionStmt(self, ctx):
        self._set_cur_func(ctx.ambiguousIdentifier().getText())

    def exitFunctionStmt(self, ctx):
        self._set_cur_func("")

    def enterSubStmt(self, ctx):
        self._set_cur_func(ctx.ambiguousIdentifier().getText())

    def exitSubStmt(self, ctx):
        self._set_cur_func("")

    def _add_call(self, callee):
        if self.cur_func not in ["", callee]:
            self.callgraph[self.cur_func].add(callee)

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
        print(ctx.getText())
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


def parse(basiccode, diagnostic=False):
    " Returns parsetree object "
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
    listener = BasicListener()
    walker.walk(listener, tree)

    return (listener.functionnames, listener.callgraph)
