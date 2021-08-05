# pylint: disable=too-many-lines
# pylint: disable=protected-access
" parser tests "
from odbinfo.pure.datatype import BasicFunction
from odbinfo.pure.parser.basic import (BodyScanner, ModuleScanner,
                                       all_functioncalls, allmacros,
                                       extract_stringliterals, functioncall,
                                       get_basic_tokens, macro, maybe,
                                       scan_basic, signature)


def parse(source):
    " wrap parse with default arguments "
    return scan_basic(get_basic_tokens(source), "Standard", "Module")


def module_scanner(source: str) -> ModuleScanner:
    "Instantiates ModuleScanner on `source`"
    alltokens = get_basic_tokens(source)
    tokens = list(filter(lambda x: not x.hidden, alltokens))
    return ModuleScanner(tokens, alltokens, "Standard", "Module1")


def bodyscanner(source: str) -> BodyScanner:
    "Instantiates bodyscanner"
    tokens = get_basic_tokens(source)
    return BodyScanner(tokens)


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


def test_allmacros():
    " test allmacros"
    scanner = module_scanner(TOKENSOURCECODE)
    macros = allmacros(scanner)
    print("All Macros: ", macros)


def test_allmacros_empty():
    " test allmacros"
    scanner = module_scanner("")
    macros = allmacros(scanner)
    print("All Macros: ", macros)


def test_extract_stringliterals():
    " test extract_stringliterals"
    tokens = get_basic_tokens("""ModuleFoo.Foo("Hello world!")""")
    print(tokens)
    acallable = BasicFunction("methodName", "ModuleName", "LibName")
    acallable.body_tokens = tokens
    strings = extract_stringliterals(acallable)
    assert len(strings) == 1
    assert strings[0].text == "\"Hello world!\""


def test_functioncall():
    " test functioncall"
    scanner = bodyscanner("ModuleFoo.Foo()")
    call = functioncall(scanner)
    assert call.module_token.text == "ModuleFoo"
    assert call.name_token.text == "Foo"


def test_allfunctioncalls():
    " test all_functioncalls"
    scanner = bodyscanner("ModuleFoo.Foo()")
    calls = all_functioncalls(scanner)
    assert calls[0].module_token.text == "ModuleFoo"
    assert calls[0].name_token.text == "Foo"


def test_allfunctioncalls_multiple_calls():
    " test all_functioncalls"
    scanner = bodyscanner("ModuleFoo.Foo() Unqualified() NoCall")
    calls = all_functioncalls(scanner)
    assert calls[0].module_token.text == "ModuleFoo"
    assert calls[0].name_token.text == "Foo"
    assert calls[1].name_token.text == "Unqualified"
    assert len(calls) == 2


def test_allfunctioncalls_method():
    " test functioncalls method"
    scanner = bodyscanner("ModuleFoo.Foo() Unqualified() NoCall")
    assert len(scanner.functioncalls()) == 2


def test_signature():
    " test signature"
    scanner = module_scanner("public static sub foo()\n")
    start, end, name_token = signature(scanner)

    print(start, end, name_token)
    assert name_token.text == "foo"


def test_macro():
    " test macro"
    scanner = module_scanner("sub foo()\nend sub\n")
    amacro = macro(scanner)
    print("Macro: ", amacro)


def test_find_signature():
    " test _signature"
    scanner = module_scanner("public static sub sub foo()\n")
    result = maybe(signature)(scanner)
    print(result)


def test_get_basic_tokens():
    "test basic tokenizer"
    tokens = get_basic_tokens(TOKENSOURCECODE)
    # for tok in tokens:
    #      print(tok)
    assert len(tokens) == 37
    tokens = list(filter(lambda x: not x.hidden, tokens))
    # for tok in tokens:
    #     print(tok)
    assert len(tokens) == 34


def test_scan_basic_empty():
    "test scan_basic"
    assert parse("") == []


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
