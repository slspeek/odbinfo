" for my personal understanding of python"
from abc import ABC, abstractmethod
from dataclasses import dataclass

import pytest


class AnAbstractClass(ABC):  # pylint: disable=too-few-public-methods
    "abstract"
    @property
    @abstractmethod
    def name(self):
        "name property"


def test_a():
    "this shows you cannot use dataclasses to implement abstractproperties"
    @dataclass
    class SubClass(AnAbstractClass):  # pylint: disable=too-few-public-methods
        "subclass"
        name: str
    with pytest.raises(TypeError):
        SubClass("MyName")  # pylint: disable=abstract-class-instantiated


def test_classvar():
    "test class property"
    class ClassB():  # pylint: disable=too-few-public-methods
        " class with class property"
        name: str = "Hey"

    instance = ClassB()
    instance.name = "Me"
    assert instance.name == "Me"
    assert ClassB.name == "Hey"

    other_instance = ClassB()
    assert other_instance.name == "Hey"
