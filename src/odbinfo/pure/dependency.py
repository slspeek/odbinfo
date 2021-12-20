"""Dependency search matrix"""
from abc import ABC
from typing import Sequence, cast

from odbinfo.pure.datatype.base import Dependent, Usable
from odbinfo.pure.datatype.basicfunction import BasicFunction
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import (EmbeddedQuery, Key, Query,
                                           QueryBase, Table, View)
from odbinfo.pure.datatype.ui import (AbstractCommander, DatabaseDisplay,
                                      EventListener, ListBox, Report, SubForm,
                                      TextDocument)
from odbinfo.pure.util import timed
from odbinfo.pure.visitor import (CommanderVisitor, DependentVisitor,
                                  EventListenerVisitor, KeyVisitor,
                                  QueryBaseVisitor)


def search_combinations(sources: Sequence[Dependent], targets: Sequence[Usable]) -> None:
    """ search for uses of `targets` in `sources`"""
    for source in sources:
        for target in targets:
            source.consider_uses(target)


def search_combinations_new(sources: Sequence[Dependent], targets: Sequence[Usable]) -> None:
    """ search for uses of `targets` in `sources`"""
    for source in sources:
        for target in targets:
            visitor = DepencencySearch(target)
            source.accept(visitor)


class DependencySearchBase(ABC):
    """Stores the target"""

    def __init__(self, target: Usable):
        self.target = target


class KeySearch(KeyVisitor, DependencySearchBase):
    """ Visitor for depencency search in Keys"""

    def visit_key(self, key: Key):
        if self.target.users_match(key.referenced_table):
            key.link = self.target.identifier


class QueryBaseSearch(QueryBaseVisitor, DependencySearchBase):
    """ Visitor for depencency search in Query-like objects"""

    def visit_querybase(self, query: QueryBase):
        for token in query.table_tokens:
            if self.target.users_match(token.text[1:-1]):
                token.link_to(self.target)


class EventListenerSearch(EventListenerVisitor, DependencySearchBase):
    """ Visitor for depencency search in EventListeners"""

    def visit_eventlistener(self, eventlistener: EventListener):
        if not isinstance(self.target, BasicFunction):
            return
        func = cast(BasicFunction, self.target)
        if func.script_url == eventlistener.parsescript():
            eventlistener.link_to(func)


class CommanderSearch(CommanderVisitor, DependencySearchBase):
    """ Commander depencency search """

    def visit_commander(self, commander: AbstractCommander):
        if not commander.issqlcommand and \
                self.target.users_match(commander.command):
            commander.link_to(self.target)

    def visit_listbox(self, listbox: ListBox):
        self.visit_commander(listbox)

    def visit_subform(self, subform: SubForm):
        self.visit_commander(subform)


class DepencencySearch(KeySearch,
                       QueryBaseSearch,
                       EventListenerSearch,
                       CommanderSearch,
                       DependentVisitor):
    """All dependency search visitors"""


#
# BasicFunction in BasicFunction
#

def remove_recursive_calls(funcs: Sequence[BasicFunction]):
    """remove the probably unintended recursive call made by assignment"\
        "of the return value"""
    for function in funcs:
        function.remove_recursive_calls()


def search_calls(source: BasicFunction, targets: Sequence[BasicFunction]):
    """ search for calls from source in `targets`"""

    # source's module
    def filter_own_module(call: BasicFunction):
        return (call.module == source.module
                and call.library == source.library)

    # targets in own library
    def filter_own_library(call: BasicFunction):
        return (not (call.module == source.module)
                and call.library == source.library)

    # targets in other libraries
    def filter_other_library(call: BasicFunction):
        return not call.library == source.library

    # the order is crucial as it represents scope in OOBasic
    ordered_targets = (list(filter(filter_own_module, targets))
                       + list(filter(filter_own_library, targets))
                       + list(filter(filter_other_library, targets)))
    for candidate in ordered_targets:
        source.consider_calls(candidate)


def search_callable_in_callable(callables: Sequence[BasicFunction]) -> None:
    """ dependency search amoung the basic targets and linking the
    parsed tokens to the targets
    the callable tokens are linked during search
    the module tokens links are rewritten afterwards
    find calls from one to another """

    for acallable in callables:
        search_calls(acallable, callables)
    remove_recursive_calls(callables)


@timed("Search dependencies", indent=4)
def search_dependencies(metadata: Metadata) -> None:
    """ dependency search in `metadata`"""
    search_combinations_new(metadata.eventlisteners,
                            metadata.basicfunction_defs)
    search_callable_in_callable(metadata.basicfunction_defs)
    search_combinations(metadata.basicfunction_defs,
                        metadata.by_content_type(Table,
                                                 Query,
                                                 View,
                                                 Report,
                                                 TextDocument))

    search_combinations_new(metadata.by_content_type(Key), metadata.table_defs)
    search_combinations_new(metadata.by_content_type(View),
                            metadata.by_content_type(Table, View))
    search_combinations_new(metadata.by_content_type(Query, EmbeddedQuery),
                            metadata.by_content_type(Table, Query, View))
    search_combinations_new(metadata.commanders,
                            metadata.by_content_type(Table, Query, View))
    search_combinations(metadata.by_content_type(DatabaseDisplay),
                        metadata.by_content_type(Table, Query, View))
