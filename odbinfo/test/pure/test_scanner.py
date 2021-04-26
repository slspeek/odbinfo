" scanner tests "
from odbinfo.pure.parser.basic import get_basic_tokens
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.pure.parser.scanner import Scanner


def new_scanner(source: str) -> Scanner:
    "Instantiates BasicScanner on `source`"
    tokens = get_basic_tokens(source)
    return Scanner(tokens)


def test_empty_input():
    " on [] "
    scanner = Scanner([])
    scanner.step()
    assert scanner.cursor == 0


def test_find_oneof_not_found():
    " test when something is not found "
    source = "function foo(arg)"
    scanner = new_scanner(source)
    assert not scanner.find_oneof([OOBasicLexer.GLOBAL])
    assert scanner.cursor == 0


def test_find_oneof_found():
    " test when something is not found "
    source = "function foo(arg)"
    scanner = new_scanner(source)
    assert scanner.find_oneof([OOBasicLexer.IDENTIFIER])
    assert scanner.cursor == 3


def test_oneof_found():
    " test when something is not found "
    source = "function foo(arg)"
    scanner = new_scanner(source)
    assert scanner.oneof([OOBasicLexer.IDENTIFIER, OOBasicLexer.FUNCTION])
    assert scanner.cursor == 1
