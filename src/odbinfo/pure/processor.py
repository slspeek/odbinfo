""" Processor module
    Processing consists of
    1. Preprocessing for the dependency search (e.g. parsing)
    2. Dependency search
    3. Graph generation
    4. Color highlighting BASIC
    5. Sets the parent links (e.g. BasicFunction -> Module -> Library)
"""
import dataclasses
from typing import List, Sequence, Union

from odbinfo.pure.datatype.base import (BasicToken, Identifier, Preprocessable,
                                        Usable, UseAggregator, UseLink, User,
                                        content_type)
from odbinfo.pure.datatype.basicfunction import BasicFunction
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.exec import Module
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import QueryBase
from odbinfo.pure.datatype.ui import Control, Form, ListBox, SubForm
from odbinfo.pure.dependency import search_dependencies
from odbinfo.pure.graph import generate_main_graph
from odbinfo.pure.parser.basic import (OOBasicLexer, get_basic_tokens,
                                       parse_basic)
from odbinfo.pure.parser.sql import parse
from odbinfo.pure.util import timed
from odbinfo.pure.visitor import (BasicTokenVisitor, FormVisitor,
                                  ModuleVisitor, PreprocessableVisitor,
                                  QueryBaseVisitor)


class FormPreprocessor(FormVisitor):
    """Form preprocessor, set the height of the form"""

    def height(self, subform: SubForm) -> int:
        """ Returns the maximum path length to a leaf subform """
        return max((self.height(sf) + 1 for sf in subform.subforms), default=0)

    @staticmethod
    def set_depth(depth: int, subform: SubForm) -> None:
        """ Sets depth recursively in `subform`"""
        subform.depth = depth
        for asubform in subform.subforms:
            FormPreprocessor.set_depth(depth + 1, asubform)

    def set_form_height(self, form: Form) -> None:
        """ Set the maximum height into the `form` """
        form.height = max([self.height(sf) for sf in form.subforms], default=0)

    def visit_form(self, form: Form):
        for subform in form.subforms:
            self.set_depth(0, subform)
        self.set_form_height(form)

    def visit_subform(self, subform: SubForm):
        pass

    @staticmethod
    def simplify_type(control: Union[Control, ListBox]):
        """Simplies the Staroffice components type"""
        control.type = control.type.split(".")[-1]

    def visit_control(self, control: Control):
        self.simplify_type(control)

    def visit_listbox(self, listbox: ListBox):
        self.simplify_type(listbox)


def undouble_uses(usecases: List[UseLink]) -> List[UseLink]:
    """Merge sources of UseLinks with identical target"""

    def unique_identifiers() -> List[Identifier]:
        return list(dict.fromkeys(u.link for u in usecases))

    def collect_sources_by_page(identifier: Identifier):
        return sum(
            [user.sources for user in usecases if user.link == identifier], [])

    return [
        UseLink(identifier, collect_sources_by_page(identifier))
        for identifier in unique_identifiers()
    ]


def aggregate_uses_from_children(user_agg: UseAggregator,
                                 collapse_multiple_uses: bool) -> None:
    """
        Collect aggregated uses from its children.
        Queries and Forms are UseAggregators.

        One can call these uses the implied uses.
        E.g. a Query "SELECT * FROM "table_1";" has an implied use of Table "table_1".
        While a SQLToken (child of that Query) referring to the Table is the actual
        user.
    """
    collected_uses: List[UseLink] = []
    for node in user_agg.all_objects():
        if isinstance(node, User) and node.link:
            collected_uses.append(UseLink(node.link, [node.obj_id]))
    if collapse_multiple_uses:
        user_agg.uses = undouble_uses(collected_uses)
    else:
        user_agg.uses = collected_uses


def aggregate_uses(use_aggregators: List[UseAggregator],
                   collapse_multiple_uses: bool) -> None:
    """Collect uses by children for all UseAggregators"""
    for use_agg in use_aggregators:
        aggregate_uses_from_children(use_agg, collapse_multiple_uses)


def merge_used_by(users: Sequence[Identifier]) -> List[Identifier]:
    """If two ids have the same content_type and local_id merge their bookmarks"""

    def unique_page_identifiers():
        """ Returns all unique the WebPages involved in `users`,
            that is discarding the bookmark part of the Identifier
            when comparing """
        return list(dict.fromkeys((i.content_type, i.local_id) for i in users))

    def identifiers_matching(apage):
        return [
            user for user in users
            if user.content_type == apage[0] and user.local_id == apage[1]
        ]

    result = []
    for page_id in unique_page_identifiers():
        bookmark = ",".join(identifier.bookmark
                            for identifier in identifiers_matching(page_id)
                            if identifier.bookmark)
        result.append(Identifier(page_id[0], page_id[1], bookmark))
    return result


def aggregate_used_by(metadata: Metadata,
                      collapse_multiple_uses: bool) -> None:
    """Collect all used_by"""
    for user in metadata.actual_users:
        metadata.usable_by_link[user.link].used_by.append(user.identifier)
    if collapse_multiple_uses:
        for usable in metadata.by_content_type(Usable):
            usable.used_by = merge_used_by(usable.used_by)


def rewrite_module_callable_links(module_seq: Sequence[Module]) -> None:
    """ links to targets are rewritten to links to targets in
        modules (using #bookmarks)"""

    # process module source tokens to support callable links at module level
    # e.g /Lib1.Mod1/#macro
    # By rewriting Identifier(type="BasicFunction" local_id="call.Mod1.Lib1")
    # to Identifier(type="Module", local_id="Mod1.Lib1", bookmark="call")
    def rewrite_module(basic_module: Module):

        def rewrite_link(link: Identifier):
            if not link.content_type == content_type(BasicFunction):
                return link
            lmacro, lmodule, llib = link.local_id.split('.')
            return Identifier(content_type(Module), f"{lmodule}.{llib}",
                              lmacro)

        def copy_links(func):
            for token in func.tokens:
                module_token = basic_module.tokens[token.index]
                if token.link:
                    module_token.link = rewrite_link(token.link)

        for function in basic_module.callables:
            copy_links(function)

    for module in module_seq:
        rewrite_module(module)


class ModulePreprocessor(ModuleVisitor):
    """Preprocesses a Module"""

    @staticmethod
    def link_name_tokens(module: Module):
        """Link the name tokens to the function-detail pages"""
        for name_index, acallable in zip(module.name_indexes,
                                         module.callables):
            module.tokens[name_index].link_to(acallable)

    @staticmethod
    def copy_tokens(module: Module):
        """Copies the modules tokens"""
        module.tokens = [dataclasses.replace(token) for token in module.tokens]

    def visit_module(self, module: Module):
        """ 1. Tokenizes
            2. Parses
            3. Deep copies the module tokens (so they can diverge from the function tokens)
            4. Sets the indexes of the tokens that are the names of the procedures
            5. Links to procedure name tokens to function-detail page
        """
        module.tokens = \
            get_basic_tokens(module.source)
        module.callables = \
            parse_basic(module.tokens, module.library, module.name)
        self.copy_tokens(module)
        module.name_indexes = \
            [c.name_token_index for c in module.callables]
        self.link_name_tokens(module)


class QueryBasePreprocessor(QueryBaseVisitor):
    """Preprocessor for QueryBase"""

    @staticmethod
    def parse_query(query: QueryBase):
        """Parses `query.command`"""
        parse_result = parse(query.command)
        query.tokens = parse_result.tokens
        query.table_tokens = parse_result.tablenames
        query.literal_values = parse_result.literal_values

    @staticmethod
    def color_hightlight_query(query: QueryBase):
        """Sets the class attribute on the special tokens"""
        for littoken in query.literal_values:
            littoken.cls = "literalvalue"

    @timed("Parse query", indent=4, arg=1)
    def visit_querybase(self, query: QueryBase):
        """Preprocesses `query`, that is parses it and does its the color highlighting"""
        self.parse_query(query)
        self.color_hightlight_query(query)


class Preprocessor(PreprocessableVisitor, ModulePreprocessor,
                   QueryBasePreprocessor, FormPreprocessor):
    """All preprocessor implementations together.
       ModulePreprocessor, QueryBasePreprocessor with FormPreprocessor implement
       PreprocessableVisitor
    """


BASICTOKEN_CLASSES = {
    OOBasicLexer.STRINGLITERAL: "stringlit",
    OOBasicLexer.COMMENT: "comment",
    OOBasicLexer.IDENTIFIER: "identifier"
}


class Highlighter(BasicTokenVisitor):
    """ Color highlighter"""

    def visit_basictoken(self, token: BasicToken):
        if token.type in BASICTOKEN_CLASSES:
            token.cls = BASICTOKEN_CLASSES[token.type]


def highlight_tokens(tokens: Sequence[BasicToken]):
    """ Visits all `tokens` to do color highlighting"""
    visitor = Highlighter()
    for token in tokens:
        token.accept(visitor)


def preprocess(preprocessables: Sequence[Preprocessable]):
    """Preprocess all"""
    visitor = Preprocessor()
    for node in preprocessables:
        node.accept(visitor)


@timed("Process metadata", indent=2)
def process_metadata(config: Configuration, metadata: Metadata) -> Metadata:
    """ Processing of the `metadata`"""
    preprocess(metadata.by_content_type(Preprocessable))

    metadata.prepare_indexed_tree()

    search_dependencies(metadata)
    rewrite_module_callable_links(metadata.module_defs)
    aggregate_uses(metadata.by_content_type(UseAggregator),
                   config.graph.collapse_multiple_uses)
    aggregate_used_by(metadata, config.graph.collapse_multiple_uses)

    metadata.graph = generate_main_graph(metadata, config)
    metadata.set_parent_links(None)

    highlight_tokens(metadata.by_content_type(BasicToken))
    # for test purposes only, needed for benchmarking
    return metadata
