""" Facade fot the SQLiteParser """
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from odbinfo.parser.sqlite.SQLiteParser import SQLiteParser
from odbinfo.parser.sqlite.SQLiteLexer import SQLiteLexer
from odbinfo.parser.sqlite.SQLiteParserListener import\
    SQLiteParserListener


class SQLListener(SQLiteParserListener):
    "Collect tablenames"

    def __init__(self):
        super().__init__()
        self.tablenames = []

    def enterTable_name(self, ctx):
        self.tablenames.append(
            (ctx.getText(), ctx.start.line, ctx.start.column)
        )


def parse(sqlcommand):
    " Returns parsetree object "
    input_stream = InputStream(sqlcommand)
    lexer = SQLiteLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SQLiteParser(stream)
    tree = parser.parse()
    walker = ParseTreeWalker()
    listener = SQLListener()
    walker.walk(listener, tree)

    print(listener.tablenames)
    return tree
