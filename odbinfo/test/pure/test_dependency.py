" tests for dependency search "
from odbinfo.pure.datatype import UseCase
from odbinfo.pure.dependency import (consider, get_identifier,
                                     search_callable_in_callable)
from odbinfo.pure.parser.basic import scan_basic

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
Sub Foo()
    Bar()
    Standard.ModuleOne.Foo()
End Sub

Sub Bar()
End Sub
"""


def test_search_callable_in_callable():
    " total search test"
    callables = scan_basic(SOURCE_MODULEONE, "BarBar", "LibBar")
    cases = search_callable_in_callable(callables)
    print(cases)
    assert len(cases) == 1


def test_search_callable_in_callable_shadowing():
    " total search test"
    callables_one = scan_basic(SOURCE_MODULEONE, "One", "Lib")
    callables_two = scan_basic(SOURCE_MODULETWO, "Two", "Lib")
    cases = search_callable_in_callable(callables_one + callables_two)
    usecase = UseCase(
        get_identifier(callables_one[0]),
        get_identifier(callables_one[1]),
        "invokes"
    )
    assert len(cases) == 3
    # local call prevails
    assert usecase in cases


def test_consider_simple():
    " Test consider "
    callables = scan_basic(SOURCE_MODULEONE, "ModuleOne", "Library")
    foo_sub = callables[0]
    bar_sub = callables[1]
    assert len(consider(foo_sub, bar_sub)) == 1
    assert len(consider(bar_sub, foo_sub)) == 0


def test_consider_other_lib():
    " Test consider "
    callables = scan_basic(SOURCE_MODULEONE, "ModuleOne", "Standard")
    mod1_foo_sub = callables[0]
    callables = scan_basic(SOURCE_MODULETWO, "ModuleTwo", "LibraryTwo")
    mod2_foo_sub = callables[0]
    assert len(consider(mod1_foo_sub, mod2_foo_sub)) == 0
    assert len(consider(mod2_foo_sub, mod1_foo_sub)) == 1
