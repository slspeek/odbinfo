""" Facade fot the SQLiteParser """
from antlr4 import ParseTreeWalker

from odbinfo.pure.parser.scanner import (convert_token, get_token_stream,
                                         get_tokens)
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
    stream = get_token_stream(sqlcommand, SQLiteLexer)
    parser = SQLiteParser(stream)
    tree = parser.parse()
    walker = ParseTreeWalker()
    listener = SQLListener()

    walker.walk(listener, tree)

    return listener.tablenames, get_tokens(stream)
