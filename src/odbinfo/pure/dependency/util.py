""" utilities for dependency search """
from typing import Sequence

from odbinfo.pure.datatype import Dependent, Usable


def search_combinations(sources: Sequence[Dependent], targets: Sequence[Usable]) -> None:
    """ search for uses of `targets` in `sources`"""
    for source in sources:
        for target in targets:
            source.consider_uses(target)
