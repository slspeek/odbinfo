" test dependency search in basicfunctions "
import unittest

from odbinfo.pure.datatype import (Identifier, Library, Module, WebPage,
                                   content_type)
from odbinfo.pure.dependency.searchexec import (_link_name_tokens, consider,
                                                rewrite_module_callable_links,
                                                search_callable_in_callable)
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from odbinfo.pure.processor import _process_library

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

SOURCE_FUNCTION = """
Function Answer()
    Answer() = 42
End Function
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


def test_remove_recursive_calls():
    "remove_recursive_calls"
    callables = _scan_basic(SOURCE_FUNCTION, "Standard", "ModuleOne")
    search_callable_in_callable(callables)


class ModuleOneTest(unittest.TestCase):
    " a processed Module "

    def setUp(self):
        self.module = Module("Module", "Lib", SOURCE_MODULEONE)
        lib = Library("Lib", [self.module])
        _process_library(lib)
        search_callable_in_callable(self.module.callables)


class RewriteModuleLinksTest(ModuleOneTest):
    "rewrite_module_callable_links"

    def test_rewrite_module_callable_links(self):
        "only basicfunction links"
        rewrite_module_callable_links([self.module])
        linkindex = self.module.callables[0].calls[0].name_token.index
        token = self.module.tokens[linkindex]
        identifier = Identifier(content_type(
            Module), "Module.Lib", "Bar")
        assert token.link == identifier

    def test_rewrite_module_callable_links_with_skip(self):
        "other link"
        self.module.callables[-1].tokens[-1].link = WebPage("foo").identifier
        rewrite_module_callable_links([self.module])
        # other links untouched
        assert self.module.callables[-1].tokens[-1].link == WebPage(
            "foo").identifier


class LinkNameTokens(ModuleOneTest):
    "_link_name_tokens"

    def test_link_name_tokens(self):
        "_link_name_tokens"
        _link_name_tokens(self.module)
        func = self.module.callables[0]
        name_token = self.module.tokens[func.name_token_index]
        assert name_token.link == func.identifier
