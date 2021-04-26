# pylint: disable=too-many-lines
# pylint: disable=protected-access
" parser tests "
import pytest

from odbinfo.pure.parser.basic import (BasicScanner, get_basic_tokens,
                                       scan_basic)


def parse(source):
    " wrap parse with default arguments "
    return scan_basic(source, "Standard", "Module")


def basicscanner(source: str) -> BasicScanner:
    "Instantiates BasicScanner on `source`"
    tokens = get_basic_tokens(source)
    alltokens = get_basic_tokens(source, True)
    return BasicScanner(tokens, alltokens, "Standard", "Module1")


def test_callable_id_not_found():
    " test id not found "
    source = "private static function end function"
    scanner = basicscanner(source)
    assert not scanner._find_callable()


def test_newline_not_found():
    " test newline is not found "
    source = "function foo(arg)"
    scanner = basicscanner(source)
    with pytest.raises(RuntimeError):
        scanner._find_callable()


def test_end_function_not_found():
    " test newline is not found "
    source = """function foo(arg)
                end"""
    scanner = basicscanner(source)
    with pytest.raises(RuntimeError):
        scanner._find_callable()


def test_find_callable_continu1():
    " test first continu "
    source = """public function foo(arg)
                end function"""
    tokens = get_basic_tokens(source)
    alltokens = get_basic_tokens(source, True)
    del tokens[1]
    scanner = BasicScanner(tokens, alltokens, "Standard", "Module1")
    assert scanner._find_callable()


def test_find_callable_continu2():
    " test first continu"
    source = """public function foo(arg)
                end function"""
    tokens = get_basic_tokens(source)
    alltokens = get_basic_tokens(source, True)
    del tokens[3]
    scanner = BasicScanner(tokens, alltokens, "Standard", "Module1")
    assert not scanner._find_callable()


def test_parse():
    " call parse "
    callables = parse("""
        function foo(arg)
            bar(0): gnu(9)
            a = spooler(45, 0)
            baz(9).graphics(kaleidos(a), 0)
            call linux()
            foo = 3
        end function
        """)
    assert callables[0].name == "foo"
    assert len(callables[0].body_tokens) == 50


BODY = """Select case Fop(a)
    case 1: a = Foo(0)
    case else
    end select
    """

SELECT = f"""
Sub Foo () {BODY} end sub
"""


def test_parse_select():
    " call parse select"
    callables = parse(SELECT)
    assert len(callables) == 1


TOKENSOURCECODE = """
rem procedure Foo
sub Foo(a as String)
   print a
   closedatabase()
end sub ' sub foo

public sub Bar()
end sub
rem end of file"""


def test_get_basic_tokens():
    "test basic tokenizer"
    tokens = get_basic_tokens(TOKENSOURCECODE, True)
    for tok in tokens:
        print(tok)
    assert len(tokens) == 37
    tokens = get_basic_tokens(TOKENSOURCECODE, False)
    for tok in tokens:
        print(tok)
    assert len(tokens) == 34


def test_scan_basic():
    "test scan_basic"
    callables = parse(TOKENSOURCECODE)
    assert len(callables) == 2
    assert len(callables[1].body_tokens) == 0


BARSOURCE = """
sub Bar()
rem nop
end sub"""


def test_scan_basic_empty_method():
    "empty body_tokens"
    callables = parse(BARSOURCE)
    assert len(callables) == 1
    assert len(callables[0].body_tokens) == 1
