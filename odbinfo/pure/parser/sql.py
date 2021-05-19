""" Facade fot the SQLiteParser """
from antlr4 import ParseTreeWalker

from odbinfo.pure.parser.scanner import get_token_stream, get_tokens
from odbinfo.pure.parser.sqlite.SQLiteLexer import SQLiteLexer
from odbinfo.pure.parser.sqlite.SQLiteParser import SQLiteParser
from odbinfo.pure.parser.sqlite.SQLiteParserListener import \
    SQLiteParserListener


class SQLListener(SQLiteParserListener):
    "Collect tablenames"

    def __init__(self, tokens):
        super().__init__()
        self.tablenames = []
        self.tokens = tokens

    def enterTable_name(self, ctx):
        self.tablenames.append(
            self.tokens[ctx.start.tokenIndex]
        )


def parse(sqlcommand):
    " Returns parsetree object "
    stream = get_token_stream(sqlcommand, SQLiteLexer)
    tokens = get_tokens(stream)
    parser = SQLiteParser(stream)
    tree = parser.parse()
    walker = ParseTreeWalker()
    listener = SQLListener(tokens)

    walker.walk(listener, tree)

    return listener.tablenames, tokens
