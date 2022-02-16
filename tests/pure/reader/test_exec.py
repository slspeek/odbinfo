""" test reding of libraries """
from unittest.mock import Mock

import pytest

from odbinfo.pure.reader.exec import (has_libraries, manifest_fileentries,
                                      read_libraries, read_library,
                                      read_module, read_python_libraries,
                                      read_python_library, read_python_module)
from tests.pure.reader.test_common import ZipFileMock

# pylint: disable=line-too-long
MANIFEST_DOC = """<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.2" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0">
 <manifest:file-entry manifest:full-path="Scripts/python/pymodule.py" manifest:media-type=""/>
 <manifest:file-entry manifest:full-path="Scripts/python/Bibliotheek/Module.py" manifest:media-type=""/>
 <manifest:file-entry manifest:full-path="Scripts/python/Bibliotheek/" manifest:media-type="application/binary"/>
 <manifest:file-entry manifest:full-path="Scripts/python/" manifest:media-type="application/binary"/>
 <manifest:file-entry manifest:full-path="Scripts/" manifest:media-type="application/binary"/>
 <manifest:file-entry manifest:full-path="Basic/Standard/Module1.xml" manifest:media-type="text/xml"/>
 <manifest:file-entry manifest:full-path="Basic/Standard/script-lb.xml" manifest:media-type="text/xml"/>
 <manifest:file-entry manifest:full-path="Basic/Standard/Module2.xml" manifest:media-type="text/xml"/>
 <manifest:file-entry manifest:full-path="Basic/script-lc.xml" manifest:media-type="text/xml"/>
 <manifest:file-entry manifest:full-path="Basic/Library1/Module1.xml" manifest:media-type="text/xml"/>
 <manifest:file-entry manifest:full-path="Basic/Library1/Module2.xml" manifest:media-type="text/xml"/>
 <manifest:file-entry manifest:full-path="Basic/Library1/script-lb.xml" manifest:media-type="text/xml"/>
</manifest:manifest>
"""


def test_manifest_fileentries():
    fakezip = ZipFileMock()
    fakezip.read = Mock(return_value=MANIFEST_DOC)
    assert len(manifest_fileentries(fakezip)) == 12


#pylint: disable=line-too-long
MODULE_FILE = b"""# coding: utf-8
from __future__ import unicode_literals


def script():
    print("Hello")
"""


def test_read_python_module():
    fakezip = ZipFileMock()

    def read(fullpath):
        return {"Scripts/python/Bibliotheek/Module.py": MODULE_FILE}[fullpath]

    fakezip.read = read
    module = read_python_module(fakezip,
                                "Scripts/python/Bibliotheek/Module.py",
                                "Bibliotheek")

    assert module.name == "Module.py"
    assert module.library == "Bibliotheek"
    assert module.source == MODULE_FILE.decode()


def test_read_python_library():
    fakezip = ZipFileMock()

    def read(fullpath):
        return {
            "META-INF/manifest.xml": MANIFEST_DOC,
            "Scripts/python/Bibliotheek/Module.py": MODULE_FILE
        }[fullpath]

    fakezip.read = read
    library = read_python_library(fakezip, "Scripts/python/Bibliotheek/")

    assert library.name == "Bibliotheek"
    assert len(library.modules) == 1


SECOND_MODULE = b"""# coding: utf-8

def main():
    print("Hello from testdb.odb")
"""


def test_read_python_libraries():
    fakezip = ZipFileMock()

    def read(fullpath):
        return {
            "META-INF/manifest.xml": MANIFEST_DOC,
            "Scripts/python/Bibliotheek/Module.py": MODULE_FILE,
            "Scripts/python/pymodule.py": SECOND_MODULE
        }[fullpath]

    fakezip.read = read
    libraries = read_python_libraries(fakezip)

    assert len(libraries) == 2


def test_has_libraries_true():
    fakezip = ZipFileMock()
    fakezip.read = Mock(return_value=MANIFEST_DOC)
    assert has_libraries(fakezip)


def test_has_libraries_false():
    fakezip = ZipFileMock()
    fakezip.read = Mock(return_value="<empty/>")
    assert not has_libraries(fakezip)


# pylint: disable=line-too-long
# noinspection PyPep8
BASIC_MODULE = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="Module1" script:language="StarBasic" script:moduleType="normal">REM  *****  BASIC  *****

Sub Main
	Error &quot;Mijn fout&quot;
End Sub

</script:module>"""


def test_read_module():
    fakezip = ZipFileMock()

    def read(fullpath):
        return {"Basic/Library1/Module1.xml": BASIC_MODULE}[fullpath]

    fakezip.read = read
    module = read_module(fakezip, "Library1", "Module1")
    assert module.library == "Library1"
    assert module.name == "Module1"
    assert module.source.count("Mijn fout") > 0


SCRIPT_LB = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:library PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "library.dtd">
<library:library xmlns:library="http://openoffice.org/2000/library" library:name="Library1" library:readonly="false" library:passwordprotected="false">
 <library:element library:name="Module1"/>
</library:library>"""


def test_read_library():
    fakezip = ZipFileMock()

    def read(fullpath):
        return {
            "Basic/Library1/Module1.xml": BASIC_MODULE,
            "Basic/Library1/script-lb.xml": SCRIPT_LB
        }[fullpath]

    fakezip.read = read
    library = read_library(fakezip, "Library1")
    assert library.name == "Library1"
    assert len(library.modules) == 1


SCRIPT_LC = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:libraries PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "libraries.dtd">
<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">
 <library:library library:name="Library1" library:link="false"/>
</library:libraries>"""


def test_read_libraries():
    fakezip = ZipFileMock()

    def read(fullpath):
        return {
            "Basic/Library1/Module1.xml": BASIC_MODULE,
            "Basic/Library1/script-lb.xml": SCRIPT_LB,
            "Basic/script-lc.xml": SCRIPT_LC,
            "META-INF/manifest.xml": MANIFEST_DOC
        }[fullpath]

    fakezip.read = read
    libraries = read_libraries(fakezip)
    library = libraries[0]
    assert library.name == "Library1"
    assert len(library.modules) == 1


def test_read_libraries_empty():
    fakezip = ZipFileMock()

    def read(fullpath):
        return {
            "Basic/Library1/Module1.xml": BASIC_MODULE,
            "Basic/Library1/script-lb.xml": SCRIPT_LB,
            "Basic/script-lc.xml": SCRIPT_LC,
            "META-INF/manifest.xml": "<empty/>"
        }[fullpath]

    fakezip.read = read

    libraries = read_libraries(fakezip)
    assert len(libraries) == 0


@pytest.mark.slow
def test_libraries_empty(empty_odbzip):
    """ no libraries  """
    read_libraries(empty_odbzip)


@pytest.mark.slow
def test_libraries(odbzip):
    """ libraries """
    read_libraries(odbzip)


@pytest.mark.slow
def test_pylibraries(odbzip):
    """ libraries """
    libs = read_python_libraries(odbzip)
    # print(libs)
    assert len(libs) == 2
    assert len(libs[0].modules) == 1
    assert len(libs[1].modules) == 1
