" tests for dependency search "
from odbinfo.pure.datatype import UseCase
from odbinfo.pure.dependency import (consider, get_identifier,
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
    cases = search_callable_in_callable(callables, [])
    print(cases)
    assert len(cases) == 1


def test_search_callable_in_callable_shadowing():
    " total search test"
    callables_one = _scan_basic(SOURCE_MODULEONE,  "Lib", "ModuleOne",)
    callables_two = _scan_basic(SOURCE_MODULETWO,  "Lib", "ModuleTwo")
    cases = search_callable_in_callable(callables_one + callables_two, [])
    usecase = UseCase(
        get_identifier(callables_two[0]),
        get_identifier(callables_one[0]),
        "invokes"
    )
    assert len(cases) == 3
    # qualified call from ModuleTwo.Wose --> ModuleOne.Foo
    assert usecase in cases


def test_consider_simple():
    " Test consider "
    callables = _scan_basic(SOURCE_MODULEONE, "Library", "ModuleOne")
    foo_sub = callables[0]
    bar_sub = callables[1]
    assert len(consider(foo_sub, bar_sub)) == 1
    assert len(consider(bar_sub, foo_sub)) == 0


def test_consider_other_lib():
    " Test consider "
    callables = _scan_basic(SOURCE_MODULEONE, "Standard", "ModuleOne")
    mod1_foo_sub = callables[0]
    callables = _scan_basic(SOURCE_MODULETWO, "LibraryTwo", "ModuleTwo")
    mod2_wose_sub = callables[0]
    assert len(consider(mod1_foo_sub, mod2_wose_sub)) == 0
    assert len(consider(mod2_wose_sub, mod1_foo_sub)) == 1
