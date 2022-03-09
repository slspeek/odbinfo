""" reading python and basic libraries """
import os
from typing import List
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype.exec import (Library, Module, PythonLibrary,
                                        PythonModule)
from odbinfo.pure.reader.common import document_element


def manifest_fileentries(odbzip: ZipFile) -> List[Element]:
    """ returns the <manifest:file-entry> elements from the manifest in `odbzip`"""
    manifest = document_element(odbzip, "META-INF/manifest.xml")
    return manifest.getElementsByTagName("manifest:file-entry")


# Python libraries and modules
def create_python_module(odbzip: ZipFile, fullpath: str,
                         library: str) -> PythonModule:
    """creates a PythonModule from the file `fullpath` in `odbzip`"""
    return PythonModule(os.path.basename(fullpath), library,
                        odbzip.read(fullpath).decode())


def create_python_library(odbzip: ZipFile, prefix: str) -> PythonLibrary:
    """ Creates a PythonLibrary read from `odbzip` that has file prefix `prefix`"""
    libname = os.path.basename(prefix.rstrip("/"))
    modules = []
    for entry in manifest_fileentries(odbzip):
        entrypath = entry.getAttribute("manifest:full-path")
        if entrypath.startswith(prefix) \
                and entry.getAttribute("manifest:media-type") == "":
            modname = os.path.basename(entrypath)
            # this check is needed because 'Scripts/python' can be a library too,
            # besides 'Scripts/python/libname'
            if prefix + modname == entrypath:
                modules.append(create_python_module(odbzip, entrypath,
                                                    libname))
    return PythonLibrary(libname, modules)


def read_python_libraries(odbzip: ZipFile) -> List[PythonLibrary]:
    """ Read python libraries from `odbzip`"""
    libraries = []
    for entry in manifest_fileentries(odbzip):
        fullpath = entry.getAttribute("manifest:full-path")
        if fullpath.startswith("Scripts/python") \
                and entry.getAttribute("manifest:media-type") == "application/binary":
            libraries.append(create_python_library(odbzip, fullpath))
    return libraries


# Basic libraries and modules


def create_library(odbzip: ZipFile, libname: str) -> Library:
    """ creates a PythonLibrary with`libname` from `odbzip`"""
    script_lb = document_element(odbzip, f"Basic/{libname}/script-lb.xml")
    lib_elems = script_lb.getElementsByTagName("library:element")
    return Library(libname, [
        create_module(odbzip, libname, elem.getAttribute("library:name"))
        for elem in lib_elems
    ])


def get_text(element: Element) -> str:
    """ returns the collected text from the text nodes directly under `element`"""
    tnodes = []
    for node in element.childNodes:
        if node.nodeType == node.TEXT_NODE:
            tnodes.append(node.data)
    return ''.join(tnodes)


def create_module(odbzip: ZipFile, library_name: str,
                  module_name: str) -> Module:
    """ creates a Module from  from `odbzip` using `library_name` and `module_name` """
    module_element = document_element(
        odbzip, f"Basic/{library_name}/{module_name}.xml")
    return Module(module_name, library_name, get_text(module_element))


def has_libraries(odbzip: ZipFile) -> bool:
    """ return True if `odbzip` contains Basic libraries"""
    for entry in manifest_fileentries(odbzip):
        if entry.getAttribute("manifest:full-path").startswith("Basic"):
            return True
    return False


def read_libraries(odbzip: ZipFile) -> List[Library]:
    """ Reads Basic libraries from the `odbzip`"""
    libraries = []
    if has_libraries(odbzip):
        script_lc = document_element(odbzip, "Basic/script-lc.xml")
        libraries = \
            [create_library(odbzip, elem.getAttribute("library:name")) for elem in
             script_lc.getElementsByTagName("library:library")]
    return libraries
