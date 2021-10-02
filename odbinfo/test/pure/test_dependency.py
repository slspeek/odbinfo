" tests for dependency search "
from odbinfo.pure.datatype import Identifier, Table, Token
from odbinfo.pure.dependency import (consider, link_token,
                                     search_callable_in_callable)
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic

SOURCE_MODULEONE = """
Sub Foo()
    Bar()
End Sub

Sub Bar()
    print "Hello Foo()"
    rem Foo
End Sub
"""

SOURCE_MODULETWO = """
Sub Wose()
    Bar()
    ModuleOne.Foo()
End Sub

Sub Foo()
End Sub

Sub Bar()
End Sub
"""


def _scan_basic(source, lib, module):
    return scan_basic(get_basic_tokens(source), lib, module)


def test_search_callable_in_callable():
    " total search test"
    callables = _scan_basic(SOURCE_MODULEONE, "LibBars", "ModuleBarBar")
    search_callable_in_callable(callables)
    all_tokens = sum(map(lambda x: x.tokens, callables), [])
    assert len([token for token in all_tokens if token.link]) == 1


def test_search_callable_in_callable_shadowing():
    " total search test"
    callables_one = _scan_basic(SOURCE_MODULEONE,  "Lib", "ModuleOne",)
    callables_two = _scan_basic(SOURCE_MODULETWO,  "Lib", "ModuleTwo")
    search_callable_in_callable(callables_one + callables_two)
    all_tokens = sum(
        map(lambda x: x.tokens, callables_one + callables_two), [])
    assert len([token for token in all_tokens if token.link]) == 3


def test_consider_simple():
    " Test consider "
    callables = _scan_basic(SOURCE_MODULEONE, "Library", "ModuleOne")
    foo_sub = callables[0]
    bar_sub = callables[1]
    consider(foo_sub, bar_sub)
    assert len([token for token in foo_sub.tokens if token.link]) == 1
    consider(bar_sub, foo_sub)
    assert len([token for token in bar_sub.tokens if token.link]) == 0


def test_consider_other_lib():
    " Test consider "
    callables = _scan_basic(SOURCE_MODULEONE, "Standard", "ModuleOne")
    mod1_foo_sub = callables[0]
    callables = _scan_basic(SOURCE_MODULETWO, "LibraryTwo", "ModuleTwo")
    mod2_wose_sub = callables[0]
    consider(mod1_foo_sub, mod2_wose_sub)
    assert len([token for token in mod1_foo_sub.tokens if token.link]) == 0
    consider(mod2_wose_sub, mod1_foo_sub)
    assert len([token for token in mod2_wose_sub.tokens if token.link]) == 1


def test_link_token():
    " test link_token when link already set "
    token = Token("'Plant'", 0, 0, False)
    link = Identifier("report", "Plant", None)
    token.link = link
    table = Table("Plant", "", [], [], [])
    link_token(token, table)
    assert token.link == table.identifier
