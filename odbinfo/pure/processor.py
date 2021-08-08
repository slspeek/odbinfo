""" Core module """
import dataclasses
import time
from typing import Sequence, Union

from odbinfo.pure.datatype import (Control, Form, Grid, Library, Metadata,
                                   Module, Query, SubForm)
from odbinfo.pure.datatype.base import (PageOwner, UseAggregator, User,
                                        get_source_identifier)
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.dependency import _link_name_tokens, search_dependencies
from odbinfo.pure.graph import generate_graphs
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from odbinfo.pure.parser.sql import parse


def copy_tokens(module):
    "Copies the modules tokens"
    def copy_token(token):
        new_token = dataclasses.replace(token)
        new_token.link = token.link
        return new_token
    module.tokens = list(map(copy_token, module.tokens))


def _process_library(library: Library) -> None:
    def parse_module(module: Module) -> None:
        # print("parsing: " + module.source)
        module.tokens =\
            get_basic_tokens(module.source)
        module.callables =\
            scan_basic(module.tokens, library.name, module.name)
        copy_tokens(module)
        module.name_indexes =\
            list(map(lambda c: c.name_token_index, module.callables))

    for module in library.modules:
        parse_module(module)


def _process_libraries(libraries: Sequence[Library]) -> None:
    for lib in libraries:
        _process_library(lib)


def _process_query(query: Query) -> None:
    query.table_tokens, query.tokens = parse(query.command)


def set_depth(depth: int, subform: SubForm) -> None:
    " sets depth recursively in `subform`"
    subform.depth = depth
    for asubform in subform.subforms:
        set_depth(depth + 1, asubform)


def height(subform: SubForm) -> int:
    " max path length to a leaf subform "
    if subform.subforms:
        return max(height(sf) for sf in subform.subforms) + 1
    return 0


def set_form_height(form: Form) -> None:
    " set the max height into the `form` "
    form.height = max([height(sf) for sf in form.subforms], default=0)


def process_subform(subform: SubForm) -> None:
    " simplifies control.type for all (nested) controls "
    def process_control(control: Union[Control, Grid]) -> None:
        if isinstance(control, Grid):
            return
        control.type = control.type.split(".")[-1]

    for control in subform.controls:
        process_control(control)
    for asubform in subform.subforms:
        process_subform(asubform)


def process_form(form: Form) -> None:
    " calculate depth for its subforms "
    for subform in form.subforms:
        set_depth(0, subform)
        process_subform(subform)
    set_form_height(form)


def time_func(func, *args):  # *args can take 0 or more
    '''function which prints the wall time it takes to execute the given command'''
    start_time = time.time()
    func(*args)
    end_time = time.time()
    print("it took this long to run: {}".format(end_time-start_time))


def distribute_usecases(metadata):
    "Decorate the PageOwners with their dependencies and use cases"
    for usecase in metadata.use_cases:
        source = metadata.index[(
            usecase.obj.object_type, usecase.obj.local_id)]
        source.uses.append(usecase.subject)
        target = metadata.index[(
            usecase.subject.object_type, usecase.subject.local_id)]
        target.used_by.append(usecase.obj)


def aggregate_uses_from_children(user_agg):
    "Collect aggregated uses from its children "
    for user in user_agg.all_objects():
        if isinstance(user, User) and user.link:
            user_agg.uses.append(user.link)


def aggregate_uses(metadata: Metadata) -> None:
    "Collect all aggregated uses "
    for use_agg in metadata.all_objects():
        if isinstance(use_agg, UseAggregator):
            aggregate_uses_from_children(use_agg)


def source_link(user):
    "returns a back link to this `user`"
    parent = user
    while not isinstance(parent, PageOwner):
        parent = parent.parent
    return get_source_identifier(parent, user)


def aggregate_used_by(metadata):
    "Collect all used_by"
    for user in metadata.all_active_users():
        print(user.link)
        if not user.link.bookmark:
            metadata.index[(user.link.object_type, user.link.local_id)
                           ].used_by.append(source_link(user))


def process_metadata(metadata: Metadata, config: Configuration) -> Metadata:
    " preprocessing of the data before it is send to hugo "
    start_time = time.time()
    _process_libraries(metadata.library_defs)
    end_time = time.time()
    print("Parse basic: {}".format(end_time-start_time))

    start_time = time.time()
    for query in metadata.query_defs:
        _process_query(query)
    for view in metadata.view_defs:
        _process_query(view)
    end_time = time.time()
    print("Parse queries and views: {}".format(end_time-start_time))

    start_time = time.time()
    for form in metadata.form_defs:
        process_form(form)
    end_time = time.time()
    print("Process forms: {}".format(end_time-start_time))

    start_time = time.time()
    metadata.set_parents(None)
    metadata.build_parent_index()
    metadata.set_titles()
    metadata.verify_titles_unique_in_kind()
    end_time = time.time()
    print("Set parents: {}".format(end_time-start_time))

    start_time = time.time()
    metadata.set_obj_ids()
    end_time = time.time()
    print("Set ids: {}".format(end_time-start_time))

    start_time = time.time()
    # is actually link_dependencies, assign should go
    search_dependencies(metadata)
    end_time = time.time()
    print("Dependency search: {}".format(end_time-start_time))

    start_time = time.time()
    metadata.create_index()
    end_time = time.time()
    print("Create index: {}".format(end_time-start_time))

    start_time = time.time()
    # distribute_usecases(metadata)
    aggregate_uses(metadata)
    aggregate_used_by(metadata)
    for module in metadata.module_defs():
        _link_name_tokens(module)
    end_time = time.time()
    print("Distribute usecases: {}".format(end_time-start_time))

    start_time = time.time()
    metadata.graphs = generate_graphs(metadata, config)
    end_time = time.time()
    print("Generate graphs: {}".format(end_time-start_time))
    # for test purposes only
    return metadata
