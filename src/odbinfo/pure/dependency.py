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
from odbinfo.pure.visitor import (BasicFunctionVisitor, CommanderVisitor,
                                  DatabaseDisplayVisitor, DependentVisitor,
                                  EventListenerVisitor, KeyVisitor,
                                  QueryBaseVisitor)


def search_combinations(sources: Sequence[Dependent],
                        targets: Sequence[Usable]) -> None:
    """ search for uses of `targets` in `sources`"""
    for target in targets:
        visitor = DepencencySearch(target)
        for source in sources:
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
        if f"{func.library}.{func.module}.{func.name}" == \
                eventlistener.parsescript():
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


class DatabaseDisplaySearch(DatabaseDisplayVisitor, DependencySearchBase):
    """Dependency search in database display object in text documents"""

    def visit_databasedisplay(self, display: DatabaseDisplay):
        if self.target.users_match(display.table):
            display.link_to(self.target)


class BasicFunctionCallSearch(BasicFunctionVisitor):
    """ Dependency search in a basic function """

    def __init__(self, target: BasicFunction):
        self.target = target

    def visit_basicfunction(self, basicfunction: BasicFunction):
        for function_call in basicfunction.calls:
            function_call.consider_use(self.target)


class BasicFunctionStringSearch(BasicFunctionVisitor, DependencySearchBase):
    """ Dependency search in a basic function """

    def visit_basicfunction(self, basicfunction: BasicFunction):
        for string_literal in basicfunction.strings:
            if self.target.users_match(string_literal.text[1:-1]):
                string_literal.link_to(self.target)


class BasicFunctionRemoveRecurisveCalls(BasicFunctionVisitor):
    """ Removes the probably unintended link to itself for functions"""

    def visit_basicfunction(self, basicfunction: BasicFunction):
        """ Removes recursive calls
            to avoid linking every function to itself
            because of the way a return value is specified"""
        for call in basicfunction.calls:
            if call.module_token:
                continue
            if call.name_token.match(basicfunction.name):
                call.name_token.link = None


class DepencencySearch(KeySearch, QueryBaseSearch, EventListenerSearch,
                       CommanderSearch, DatabaseDisplaySearch,
                       BasicFunctionStringSearch, DependentVisitor):
    """All dependency search visitors"""


def remove_recursive_calls(funcs: Sequence[BasicFunction]):
    """remove the probably unintended recursive call made by assignment"\
        "of the return value"""
    remove_rec_calls_visitor = BasicFunctionRemoveRecurisveCalls()
    for function in funcs:
        function.accept(remove_rec_calls_visitor)


def search_calls(source: BasicFunction, targets: Sequence[BasicFunction]):
    """ search for calls from source in `targets`"""

    # source's module
    def filter_own_module(target: BasicFunction) -> bool:
        return (target.module == source.module
                and target.library == source.library)

    # targets in own library
    def filter_own_library(target: BasicFunction) -> bool:
        return (not (target.module == source.module)
                and target.library == source.library)

    # targets in other libraries
    def filter_other_library(target: BasicFunction) -> bool:
        return not target.library == source.library

    # the order is crucial as it represents scope in OOBasic
    ordered_targets = (list(filter(filter_own_module, targets)) +
                       list(filter(filter_own_library, targets)) +
                       list(filter(filter_other_library, targets)))
    for target in ordered_targets:
        source.accept(BasicFunctionCallSearch(target))


def search_callable_in_callable(callables: Sequence[BasicFunction]) -> None:
    """
    dependency search amoung the basicfunctions
    """
    for acallable in callables:
        search_calls(acallable, callables)
    remove_recursive_calls(callables)


@timed("Search dependencies", indent=4)
def search_dependencies(metadata: Metadata) -> None:
    """ dependency search in `metadata`"""
    search_callable_in_callable(metadata.basicfunction_defs)

    search_combinations(sources=metadata.eventlisteners,
                        targets=metadata.basicfunction_defs)
    search_combinations(sources=metadata.basicfunction_defs,
                        targets=metadata.by_content_type(
                            Table, Query, View, Report, TextDocument))
    search_combinations(sources=metadata.by_content_type(Key),
                        targets=metadata.table_defs)
    search_combinations(sources=metadata.by_content_type(View),
                        targets=metadata.by_content_type(Table, View))
    search_combinations(sources=metadata.by_content_type(Query, EmbeddedQuery),
                        targets=metadata.by_content_type(Table, Query, View))
    search_combinations(sources=metadata.commanders,
                        targets=metadata.by_content_type(Table, Query, View))
    search_combinations(sources=metadata.by_content_type(DatabaseDisplay),
                        targets=metadata.by_content_type(Table, Query, View))
