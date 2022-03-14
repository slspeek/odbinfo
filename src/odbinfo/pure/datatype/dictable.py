""" Interface for converting an object to a dictionary """
from abc import ABC, abstractmethod
from typing import Any, List


# pylint:disable=too-few-public-methods
class Dictable(ABC):
    """Dictionary representable"""

    @abstractmethod
    def to_dict(self):
        """ Returns dictionary representation
            used for the write-out to the hugo site"""


def list_to_dict(values: List[Any]) -> List[Any]:
    """ Convert list values to dict """
    if values:
        if isinstance(values[0], Dictable):
            # It is assumed that all values are Dictable instances too
            return [d.to_dict() for d in values]
    return values


def to_dict(value: Any):
    """ Returns dictionay representation of `value`"""
    if isinstance(value, List):
        return list_to_dict(value)
    if isinstance(value, Dictable):
        return value.to_dict()
    return value
