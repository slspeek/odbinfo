# pylint: disable=too-many-lines
# pylint: disable=protected-access
" parser tests "
from functools import partial
from zipfile import ZipFile

import pytest

from odbinfo.pure.datatype import Module
from odbinfo.pure.parser.basic import (BasicScanner, get_basic_tokens,
                                       scan_basic)
from odbinfo.pure.parser.oobasic.OOBasicLexer import OOBasicLexer
from odbinfo.pure.reader import _parse_xml, mapiflist
from odbinfo.test.resource import BASEDOCUMENTER


def parse(source):
    " wrap parse with default arguments "
    return scan_basic(source, "Standard", "Module")


def test_find_or_not_found():
    " test when something is not found "
    source = "function foo(arg)"
    tokens = get_basic_tokens(source)
    alltokens = get_basic_tokens(source, True)
    scanner = BasicScanner(tokens, alltokens, "Standard", "Module1")
    assert not scanner._find_or([OOBasicLexer.GLOBAL])
    assert scanner.index == 0


def test_find_or_found():
    " test when something is not found "
    source = "function foo(arg)"
    tokens = get_basic_tokens(source)
    alltokens = get_basic_tokens(source, True)
    scanner = BasicScanner(tokens, alltokens, "Standard", "Module1")
    assert scanner._find_or([OOBasicLexer.IDENTIFIER])
    assert scanner.index == 2


def test_newline_not_found():
    " test newline is not found "
    source = "function foo(arg)"
    tokens = get_basic_tokens(source)
    alltokens = get_basic_tokens(source, True)
    scanner = BasicScanner(tokens, alltokens, "Standard", "Module1")
    with pytest.raises(RuntimeError):
        scanner._find_callable()


def test_end_fucntion_not_found():
    " test newline is not found "
    source = """function foo(arg)
                end"""
    tokens = get_basic_tokens(source)
    alltokens = get_basic_tokens(source, True)
    scanner = BasicScanner(tokens, alltokens, "Standard", "Module1")
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


def _read_module(odbzip, library_name,  data) -> Module:
    name = data["@library:name"]
    data = _parse_xml(odbzip, f"{library_name}/{name}.xba")
    return Module("BaseDocumenter", name, data["script:module"]["#text"])


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


@pytest.mark.slow
def test_basedocumenter_sources():
    " parse all basedocumenter sources "
    with ZipFile(BASEDOCUMENTER, "r") as based:
        xlb = _parse_xml(based, "BaseDocumenter/script.xlb")
        data = xlb["library:library"]["library:element"]
        read_module = partial(_read_module, based, "BaseDocumenter")
        modules = mapiflist(read_module, data)
        for module in modules:
            print(f"Start parsing {module.name}")
            if module.name == "BD_Utils":
                module.source = module.source.replace(
                    '.setDefaultName(vFile(1)\n',
                    '.setDefaultName(vFile(1))\n')
            if module.name == "BD_Settings":
                module.source = module.source.replace(
                    "Public Sub _BD_SetActualSettings(ByVal plDatabaseID As"
                    " Long, ByRef psDatabaseName As String) As Variant",
                    "Public Sub _BD_SetActualSettings(ByVal plDatabaseID As"
                    " Long, ByRef psDatabaseName As String)")
            if module.name == "BD_Html":
                module.source = module.source.replace(
                    """, _BD_UTF8(Replace(_BD_GetLabel("PREFERENCESTITLE"),"""
                    """ "%0", BaseDocumenterTitle))""",
                    """, _BD_UTF8(Replace(_BD_GetLabel("PREFERENCESTITLE"),"""
                    """ "%0", BaseDocumenterTitle)))"""
                )
            # get_basic_tokens(module.source)
            scan_basic(module.source, "BaseDocumenter", module.name)
