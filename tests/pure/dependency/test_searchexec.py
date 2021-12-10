""" test dependency search in basicfunctions """
import unittest

from odbinfo.pure.datatype import (Identifier, Module, Table, WebPage,
                                   content_type)
from odbinfo.pure.dependency.searchexec import (
    consider, search_callable_in_callable, search_string_refs_in_callables)
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from odbinfo.pure.processor import (link_name_tokens, preprocess_modules,
                                    rewrite_module_callable_links)

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
    """ total search test"""
    callables = _scan_basic(SOURCE_MODULEONE, "LibBars", "ModuleBarBar")
    search_callable_in_callable(callables)
    all_tokens = sum((x.tokens for x in callables), [])
    assert len([token for token in all_tokens if token.link]) == 1


def test_search_callable_in_callable_shadowing():
    """ total search test"""
    callables_one = _scan_basic(SOURCE_MODULEONE, "Lib", "ModuleOne", )
    callables_two = _scan_basic(SOURCE_MODULETWO, "Lib", "ModuleTwo")
    search_callable_in_callable(callables_one + callables_two)
    all_tokens = sum((x.tokens for x in callables_one + callables_two), [])
    assert len([token for token in all_tokens if token.link]) == 3


def test_consider_simple():
    """ Test consider """
    callables = _scan_basic(SOURCE_MODULEONE, "Library", "ModuleOne")
    foo_sub = callables[0]
    bar_sub = callables[1]
    consider(foo_sub, bar_sub)
    assert len([token for token in foo_sub.tokens if token.link]) == 1
    consider(bar_sub, foo_sub)
    assert len([token for token in bar_sub.tokens if token.link]) == 0


def test_consider_other_lib():
    """ Test consider """
    callables = _scan_basic(SOURCE_MODULEONE, "Standard", "ModuleOne")
    mod1_foo_sub = callables[0]
    callables = _scan_basic(SOURCE_MODULETWO, "LibraryTwo", "ModuleTwo")
    mod2_wose_sub = callables[0]
    consider(mod1_foo_sub, mod2_wose_sub)
    assert len([token for token in mod1_foo_sub.tokens if token.link]) == 0
    consider(mod2_wose_sub, mod1_foo_sub)
    assert len([token for token in mod2_wose_sub.tokens if token.link]) == 1


def test_remove_recursive_calls():
    """remove_recursive_calls"""
    callables = _scan_basic(SOURCE_FUNCTION, "Standard", "ModuleOne")
    search_callable_in_callable(callables)


class ModuleTest(unittest.TestCase):
    """ module based test"""

    def process_module(self, module_source: str):
        """parses `module` and puts result in self.module"""
        # pylint:disable=attribute-defined-outside-init
        self.module = Module("Module", "Lib", module_source)
        preprocess_modules([self.module])


class ModuleOneTest(ModuleTest):
    """ a processed Module """

    def setUp(self):
        self.process_module(SOURCE_MODULEONE)
        search_callable_in_callable(self.module.callables)


class RewriteModuleLinksTest(ModuleOneTest):
    """rewrite_module_callable_links"""

    def test_rewrite_module_callable_links(self):
        """only basicfunction links"""
        rewrite_module_callable_links([self.module])
        linkindex = self.module.callables[0].calls[0].name_token.index
        token = self.module.tokens[linkindex]
        identifier = Identifier(content_type(
            Module), "Module.Lib", "Bar")
        assert token.link == identifier

    def test_rewrite_module_callable_links_with_skip(self):
        """other link"""
        self.module.callables[-1].tokens[-1].link = WebPage("foo").identifier
        rewrite_module_callable_links([self.module])
        # other links untouched
        assert self.module.callables[-1].tokens[-1].link == WebPage(
            "foo").identifier


class LinkNameTokens(ModuleOneTest):
    """_link_name_tokens"""

    def test_link_name_tokens(self):
        """_link_name_tokens"""
        link_name_tokens(self.module)
        func = self.module.callables[0]
        name_token = self.module.tokens[func.name_token_index]
        assert name_token.link == func.identifier


STRING_REF_MODULE = """
Function WithRefs()
    Call("ref_one", "other_ref")
End Function
"""


class StringRefsInCallables(ModuleTest):
    """ search_string_refs_in_callables """

    def setUp(self):
        self.process_module(STRING_REF_MODULE)
        self.withref = self.module.callables[0]
        self.webpage = Table("ref_one", "", [], [], [])

    def test_match(self):
        """match ref_one"""
        search_string_refs_in_callables(
            [self.webpage], self.module.callables)
        assert self.withref.strings[0].link == self.webpage.identifier
