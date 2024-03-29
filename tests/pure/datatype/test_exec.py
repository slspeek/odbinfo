""" test module for exec.py """
from odbinfo.pure.datatype.basicfunction import BasicFunction
from odbinfo.pure.datatype.exec import (Library, Module, PythonLibrary,
                                        PythonModule)


def test_python_module():
    pmodule = PythonModule("Module1", "Standard",  "")
    assert pmodule.title == "Standard.Module1"


def test_python_library():
    plib = PythonLibrary("pathlib", [])
    assert not plib.children()


def test_basicfunction():
    basicfunction = BasicFunction("methodName",  "LibName", "ModuleName")
    assert basicfunction.title == "methodName.ModuleName.LibName"
    assert basicfunction.children() == []


def test_library():
    lib = Library("basiclib", [])
    assert not lib.children()


def test_module():
    module = Module("modname", "libname", "")
    assert module.title == "modname.libname"
    assert not list(module.children())
