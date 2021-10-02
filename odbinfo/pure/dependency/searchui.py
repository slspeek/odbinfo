" search dependencies in ui "
from typing import Iterable, Sequence

from odbinfo.pure.datatype import (BasicFunction, Commander, DatabaseDisplay,
                                   EventListener, TextDocument, WebPage)

#
# BasicFunction in EventListener
#


def search_basicfunction_in_eventlistener(funcs: Iterable[BasicFunction],
                                          eventlisteners: Iterable[EventListener]):
    "searches for references to basic macros in eventlisteners"
    for evl in eventlisteners:
        for func in funcs:
            if f"{func.library}.{func.module}.{func.name}" == evl.parsescript():
                evl.link = func.identifier

#
# DataObject (query, view, table) in Report, SubForm
#


def search_deps_in_commander(dataobjects: Sequence[WebPage],
                             commander_seq: Sequence[Commander]) -> None:
    " find uses of dataobject in report"
    def find_deps_in_commander(commander: Commander) -> None:
        " find dependency uses in `report` "
        def match_one_dep(dependency: WebPage) -> None:
            if (not commander.commandtype == "command"  # no matching of embedded
                # queries (COMMAND)
                    and dependency.users_match(commander.command)):
                commander.link = dependency.identifier
        for obj in dataobjects:
            match_one_dep(obj)
    for commander in commander_seq:
        find_deps_in_commander(commander)


def search_deps_in_documents(dataobjects: Sequence[WebPage],
                             documents: Sequence[TextDocument]) -> None:
    " find uses of dataobject in document"
    def find_deps_in_doc(document: TextDocument) -> None:

        def find_one_dep(dependency: WebPage) -> None:

            def find_in_databasedisplay(display: DatabaseDisplay) -> None:
                if dependency.users_match(display.table):
                    display.link = dependency.identifier

            for field in document.fields:
                find_in_databasedisplay(field)
        for obj in dataobjects:
            find_one_dep(obj)
    for doc in documents:
        find_deps_in_doc(doc)
