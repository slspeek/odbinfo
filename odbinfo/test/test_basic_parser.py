# pylint: disable=too-many-lines
" parser tests "
from functools import partial
from zipfile import ZipFile

import pytest

import odbinfo
from odbinfo.datatype import Module
from odbinfo.parser.basic import get_basic_tokens, scan_basic
from odbinfo.reader import _parse_xml,  mapiflist
from odbinfo.test.resource import BASEDOCUMENTER

CODE = """
dim number1, number2 as integer
dim answer as integer

Myfunction("go for it")
console.writeline("enter first number")
number1=int(console.readline())
console.writeline("enter second number")
number2=int(console.readline())
total=number1+number2
console.writeline("the answer is "& answer)

"""


def parse(source):
    " wrap parse with default arguments "
    return odbinfo.parser.basic.parse(source, "Standard", "Module")


@pytest.mark.slow
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
    assert callables[0].callees == set(["a", "bar", "gnu", "baz", "graphics",
                                        "kaleidos", "linux", "spooler"])


@pytest.mark.slow
def test_parse_module_statements():
    " call parse "
    parse(CODE)
    # print(tree.toStringTree())


SELECT = """
Sub Foo ()
    Select case Fop(a)
        case 1: a = Foo(0)
        case else
    end select
end sub
"""


def test_parse_select():
    " call parse select"
    parse(SELECT)


def test_for_next():
    "for next loop parsing"
    parse("""
    sub foo()
        for i = 0 to 10
            Print(i)
        next i
    end sub
    """)


def _read_module(odbzip, library_name,  data) -> Module:
    name = data["@library:name"]
    data = _parse_xml(odbzip, f"{library_name}/{name}.xba")
    return Module("BaseDocumenter", name, data["script:module"]["#text"])


ADDNUMERIC = """
sub foo()
    pvdefault _AddNumeric()= Null
end sub
"""


ERRORMESSAGE1 = """
sub foo()
    i = Len(bar)-1
end sub
"""


def test_error_message():
    "error message"
    parse(ERRORMESSAGE1)


def test_add_numeric():
    " add numeric"
    parse(ADDNUMERIC)


REMHEADER = """
REM =======================================================================================================================
REM ===						The BaseDocumenter library is an extension to LibreOffice.									===
REM ===			Full documentation is available on http://www.access2base.com/basedocumenter.html						===
REM =======================================================================================================================

Option Explicit

REM -----------------------------------------------------------------
REM			BASEDOCUMENTER constants
REM -----------------------------------------------------------------

REM BaseDocumenter general constants
REM -----------------------------------------------------------------

"""


def test_rem_header():
    " REM header "
    parse(REMHEADER)


TOKENSOURCECODE = """
rem procedure Foo
sub Foo(a as String)
   print a
   closedatabase()
end sub ' sub foo

public sub Bar()
end sub
"""


def test_get_basic_tokens():
    "test basic tokenizer"
    tokens = get_basic_tokens(TOKENSOURCECODE)
    for tok in tokens:
        print(tok)
    assert len(tokens) == 35


def test_scan_basic():
    "test scan_basic"
    scan_basic(TOKENSOURCECODE)


@pytest.mark.endless
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
            scan_basic(module.source)
