""" search dependencies in ui """
from typing import Iterable

from odbinfo.pure.datatype import BasicFunction, EventListener

#
# BasicFunction in EventListener
#


def search_basicfunction_in_eventlistener(funcs: Iterable[BasicFunction],
                                          eventlisteners: Iterable[EventListener]):
    """searches for references to basic macros in eventlisteners"""
    for evl in eventlisteners:
        for func in funcs:
            if f"{func.library}.{func.module}.{func.name}" == evl.parsescript():
                evl.link = func.identifier
