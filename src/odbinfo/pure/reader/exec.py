""" reading python and basic libraries """
import os
from typing import List
from xml.dom.minidom import Element
from zipfile import ZipFile

from odbinfo.pure.datatype.exec import (Library, Module, PythonLibrary,
                                        PythonModule)
from odbinfo.pure.reader.common import document_element


def manifest_fileentries(odbzip: ZipFile) -> List[Element]:
    """ returns the <manifest:file-entry> elements from `odbzip`"""
    manifest = document_element(odbzip, "META-INF/manifest.xml")
    return manifest.getElementsByTagName("manifest:file-entry")


def read_python_libraries(odbzip: ZipFile) -> List[PythonLibrary]:
    """ Read python libraries from `odbzip`"""
    libraries = []
    for entry in manifest_fileentries(odbzip):
        fullpath = entry.getAttribute("manifest:full-path")
        if fullpath.startswith("Scripts/python")\
                and entry.getAttribute("manifest:media-type") == "application/binary":
            libraries.append(read_python_library(odbzip, fullpath))
    return libraries


def read_python_library(odbzip: ZipFile, prefix: str) -> PythonLibrary:
    """ reads one python library from `odbzip` that has file prefix `prefix`"""
    libname = os.path.basename(prefix.rstrip("/"))
    modules = []
    for entry in manifest_fileentries(odbzip):
        entrypath = entry.getAttribute("manifest:full-path")
        if entrypath.startswith(prefix)\
                and entry.getAttribute("manifest:media-type") == "":
            modname = os.path.basename(entrypath)
            if prefix + modname == entrypath:
                modules.append(read_python_module(odbzip, entrypath, libname))
    return PythonLibrary(libname, modules)


def read_python_module(odbzip: ZipFile, fullpath: str,
                       library: str) -> PythonModule:
    """reads a python module file from `odbzip`"""
    return PythonModule(os.path.basename(fullpath), library,
                        odbzip.read(fullpath).decode())


def has_libraries(odbzip) -> bool:
    """ return True if `odbzip` contains Basic libraries"""
    for entry in manifest_fileentries(odbzip):
        if entry.getAttribute("manifest:full-path").startswith("Basic"):
            return True
    return False


def read_libraries(odbzip) -> List[Library]:
    """ Reads Basic libraries """
    libraries = []
    if has_libraries(odbzip):
        script_lc = document_element(odbzip, "Basic/script-lc.xml")
        libraries = \
            [read_library(odbzip, elem.getAttribute("library:name")) for elem in
                script_lc.getElementsByTagName("library:library")]
    return libraries


def read_library(odbzip: ZipFile, libname: str) -> Library:
    """ reads `libname` from `odbzip`"""
    script_lb = document_element(odbzip, f"Basic/{libname}/script-lb.xml")
    lib_elems = script_lb.getElementsByTagName("library:element")
    return Library(libname, [
        read_module(odbzip, libname, elem.getAttribute("library:name"))
        for elem in lib_elems
    ])


def _get_text(elem: Element) -> str:

    def gettext(nodelist):
        tnodes = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                tnodes.append(node.data)
        return ''.join(tnodes)

    return gettext(elem.childNodes)


def read_module(odbzip: ZipFile, library_name: str,
                module_name: str) -> Module:
    """ read one Basic module from `odbzip` from """
    module_doc = document_element(odbzip,
                                  f"Basic/{library_name}/{module_name}.xml")
    return Module(module_name, library_name, _get_text(module_doc))
