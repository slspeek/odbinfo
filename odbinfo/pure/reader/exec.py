" reading python and basic libraries "
import os
from functools import partial
from typing import List

from odbinfo.pure.datatype import Library, Module, PythonLibrary, PythonModule
from odbinfo.pure.reader.common import _parse_xml, mapiflist


def _manifest_fileentries(odbzip):
    manifest = _parse_xml(odbzip, "META-INF/manifest.xml")
    return manifest["manifest:manifest"]["manifest:file-entry"]


def read_python_libraries(odbzip):
    " Read python libraries from `odbzip`"
    libraries = []
    for entry in _manifest_fileentries(odbzip):
        fullpath = entry["@manifest:full-path"]
        if fullpath.startswith("Scripts/python")\
                and entry["@manifest:media-type"] == "application/binary":
            libraries.append(
                _read_python_library(odbzip, fullpath)
            )
    return libraries


def _read_python_library(odbzip, fullpath):
    name = os.path.basename(fullpath.rstrip("/"))
    # if name == "python":
    #     name = "DEFAULT"
    modules = []
    for entry in _manifest_fileentries(odbzip):
        entrypath = entry["@manifest:full-path"]
        if entrypath.startswith(fullpath)\
                and entry["@manifest:media-type"] == "":
            modname = os.path.basename(entrypath)
            if fullpath + modname == entrypath:
                modules.append(_read_python_module(odbzip, entrypath, name))
    return PythonLibrary(name, modules)


def _read_python_module(odbzip, fullpath, library):
    return PythonModule(
        os.path.basename(fullpath),
        library,
        odbzip.read(fullpath).decode()
    )


def _has_libraries(odbzip) -> bool:
    for entry in _manifest_fileentries(odbzip):
        if entry["@manifest:full-path"].startswith("Basic"):
            return True
    return False


def read_libraries(odbzip) -> List[Library]:
    " Reads Basic libraries "
    libraries = []
    if _has_libraries(odbzip):
        script_lc = _parse_xml(odbzip, "Basic/script-lc.xml")
        data = script_lc["library:libraries"]["library:library"]
        read_library = partial(_read_library, odbzip)
        libraries.extend(mapiflist(read_library, data))
    return libraries


def _read_library(odbzip, data) -> Library:
    name = data["@library:name"]
    script_lb = _parse_xml(odbzip, f"Basic/{name}/script-lb.xml")
    data = script_lb["library:library"]["library:element"]
    read_module = partial(_read_module, odbzip, name)
    return Library(name, mapiflist(read_module, data))


def _read_module(odbzip, library_name,  data) -> Module:
    name = data["@library:name"]
    data = _parse_xml(odbzip, f"Basic/{library_name}/{name}.xml")
    return Module(name, library_name, data["script:module"]["#text"])
