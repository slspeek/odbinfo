""" Facade fot the SQLiteParser """
from antlr4 import InputStream, CommonTokenStream
from odbinfo.parser.sqlite.SQLiteParser import SQLiteParser
from odbinfo.parser.sqlite.SQLiteLexer import SQLiteLexer


def parse(sqlcommand):
    " Returns parsetree object "
    input_stream = InputStream(sqlcommand)
    lexer = SQLiteLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SQLiteParser(stream)
    tree = parser.parse()
    print(tree.toStringTree())
    return tree
