""" Processor module """
from typing import Sequence, Union

from odbinfo.pure.datatype.base import (Identifier, UseAggregator, User,
                                        content_type)
from odbinfo.pure.datatype.basicfunction import BasicFunction
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.exec import Module
from odbinfo.pure.datatype.metadata import Metadata
from odbinfo.pure.datatype.tabular import QueryBase
from odbinfo.pure.datatype.ui import (AbstractCommander, Control, Form, Grid,
                                      ListBox, SubForm)
from odbinfo.pure.dependency import search_dependencies
from odbinfo.pure.graph import generate_graphs
from odbinfo.pure.util import timed


@timed("Parse basic modules", indent=4)
def preprocess_modules(modules: Sequence[Module]) -> None:
    """preprocesses of the of libraries"""
    for module in modules:
        module.preprocess()


# TODO: move to SubForm
def set_depth(depth: int, subform: SubForm) -> None:
    """ sets depth recursively in `subform`"""
    subform.depth = depth
    for asubform in subform.subforms:
        set_depth(depth + 1, asubform)


# TODO: move to Form
def set_form_height(form: Form) -> None:
    """ set the max height into the `form` """
    form.height = max([sf.height for sf in form.subforms], default=0)


# TODO: move to SubForm
def process_subform(subform: SubForm) -> None:
    """ simplifies control.type for all (nested) controls """

    # TODO move to Control
    def process_control(control: Union[Control, Grid, ListBox]) -> None:
        if isinstance(control, Grid):
            return
        control.type = control.type.split(".")[-1]

    for control in subform.controls:
        process_control(control)
    for asubform in subform.subforms:
        process_subform(asubform)


# TODO: move to Form
def preprocess_form(form: Form) -> None:
    """ calculate depth for its subforms """
    for subform in form.subforms:
        set_depth(0, subform)
        process_subform(subform)
    set_form_height(form)


def aggregate_uses_from_children(user_agg: UseAggregator) -> None:
    """Collect aggregated uses from its children """
    for user in user_agg.all_objects():
        if isinstance(user, User) and user.link:
            user_agg.uses.append(user.link)


@timed("Aggregate uses", indent=4)
def aggregate_uses(metadata: Metadata) -> None:
    """Collect all aggregated uses """
    for use_agg in metadata.all_objects():
        if isinstance(use_agg, UseAggregator):
            aggregate_uses_from_children(use_agg)


def aggregate_used_by(metadata: Metadata) -> None:
    """Collect all used_by"""
    for user in metadata.all_active_users:
        metadata.usable_by_link[user.link].used_by.append(user.identifier)


@timed("Parse queries", indent=4)
def preprocess_queries(metadata: Metadata) -> None:
    """process all query-like objects"""
    for query in metadata.by_content_type(QueryBase):
        query.preprocess()


def preprocess_commanders(commanders: Sequence[AbstractCommander]) -> None:
    """ if command is a direct query, set an EmbeddedQuery obj"""
    for cmdr in commanders:
        cmdr.preprocess()


def preprocess_forms(form_defs: Sequence[Form]):
    """preprocesses all forms in `form_defs`"""
    for form in form_defs:
        preprocess_form(form)


def rewrite_module_callable_links(module_seq: Sequence[Module]) -> None:
    """ links to targets are rewritten to links to targets in
        modules (using #bookmarks)"""

    # process module source tokens to support callable links at module level
    # e.g /Lib1.Mod1/#macro
    # By rewriting Identifier(type="BasicFunction" local_id="call.Mod1.Lib1")
    # to Identifier("Module", "Mod1.Lib1", bookmark="call")
    # TODO: move to Module
    def rewrite_module(basic_module: Module):
        def rewrite_link(link: Identifier):
            if not link.content_type == content_type(BasicFunction):
                return link
            lmacro, lmodule, llib = link.local_id.split('.')
            return Identifier(content_type(Module), f"{lmodule}.{llib}", lmacro)

        def copy_links(func):
            for token in func.tokens:
                module_token = basic_module.tokens[token.index]
                if token.link:
                    module_token.link = rewrite_link(token.link)

        for function in basic_module.callables:
            copy_links(function)

    for module in module_seq:
        rewrite_module(module)


@timed("Process metadata", indent=2)
def process_metadata(config: Configuration, metadata: Metadata) -> Metadata:
    """ preprocessing of the data before it is written """
    preprocess_modules(metadata.module_defs)
    preprocess_commanders(metadata.commanders)
    preprocess_queries(metadata)
    preprocess_forms(metadata.form_defs)

    metadata.prepare_indexed_tree()

    # TODO move these 3 lines to dependency module
    search_dependencies(metadata)
    rewrite_module_callable_links(metadata.module_defs)
    aggregate_uses(metadata)
    aggregate_used_by(metadata)

    metadata.graphs = generate_graphs(metadata, config)
    metadata.set_parent_links(None)
    # for test purposes only
    return metadata
