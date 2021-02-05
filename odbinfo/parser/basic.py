""" Facade fot the OOBasicParser """
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from odbinfo.parser.oobasic.OOBasicParser import OOBasicParser
from odbinfo.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.parser.oobasic.OOBasicListener import\
    OOBasicListener


class BasicListener(OOBasicListener):
    "Collect tablenames"

    def __init__(self):
        super().__init__()
        self.functionnames = []

    def enterFunctionStmt(self, ctx):
        self.functionnames.append(
            ctx.ambiguousIdentifier().getText()
        )
        print(f"Entering {ctx.ambiguousIdentifier().getText()}")

    def enterImplicitCallStmt_InBlock(self, ctx):
        print(ctx.getText())

    def exitImplicitCallStmt_InBlock(self, ctx):
        print(ctx.getText())

    def enterICS_B_ProcedureCall(self, ctx):
        print(ctx.getText())

    def enterMsgBox(self, ctx):
        print(ctx.getText())

    def enterVsNot(self, ctx):
        print("&&&&&&&&&&&&&&&")
        print(ctx.getText())

    def enterInlineIfThenElse(self, ctx):
        print("IF THEN")
        print(ctx.getText())


def parse(basiccode):
    " Returns parsetree object "
    input_stream = InputStream(basiccode)
    lexer = OOBasicLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OOBasicParser(stream)
    tree = parser.startRule()
    walker = ParseTreeWalker()
    listener = BasicListener()
    walker.walk(listener, tree)

    print(listener.functionnames)
    return tree
