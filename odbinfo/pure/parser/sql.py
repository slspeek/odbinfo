""" Facade fot the SQLiteParser """
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from odbinfo.pure.parser.scanner import convert_token
from odbinfo.pure.parser.sqlite.SQLiteLexer import SQLiteLexer
from odbinfo.pure.parser.sqlite.SQLiteParser import SQLiteParser
from odbinfo.pure.parser.sqlite.SQLiteParserListener import \
    SQLiteParserListener


class SQLListener(SQLiteParserListener):
    "Collect tablenames"

    def __init__(self):
        super().__init__()
        self.tablenames = []

    def enterTable_name(self, ctx):
        self.tablenames.append(
            convert_token(ctx.start)
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

    return listener.tablenames
