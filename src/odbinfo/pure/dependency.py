"""Dependency search matrix"""
from typing import Sequence

from odbinfo.pure.datatype.base import Dependent, Usable
from odbinfo.pure.datatype.basicfunction import BasicFunction
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import (EmbeddedQuery, Key, Query, Table,
                                           View)
from odbinfo.pure.datatype.ui import DatabaseDisplay, Report, TextDocument
from odbinfo.pure.util import timed


def search_combinations(sources: Sequence[Dependent], targets: Sequence[Usable]) -> None:
    """ search for uses of `targets` in `sources`"""
    for source in sources:
        for target in targets:
            source.consider_uses(target)


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
    search_combinations(metadata.eventlisteners,
                        metadata.basicfunction_defs)
    search_callable_in_callable(metadata.basicfunction_defs)
    search_combinations(metadata.basicfunction_defs,
                        metadata.by_content_type(Table,
                                                 Query,
                                                 View,
                                                 Report,
                                                 TextDocument))

    search_combinations(metadata.by_content_type(Key), metadata.table_defs)
    search_combinations(metadata.by_content_type(View),
                        metadata.by_content_type(Table, View))
    search_combinations(metadata.by_content_type(Query, EmbeddedQuery),
                        metadata.by_content_type(Table, Query, View))
    search_combinations(metadata.commanders,
                        metadata.by_content_type(Table, Query, View))
    search_combinations(metadata.by_content_type(DatabaseDisplay),
                        metadata.by_content_type(Table, Query, View))
