# pylint: disable=too-many-lines
# pylint: disable=protected-access
""" parser tests """
from functools import partial
from zipfile import ZipFile

import pytest
import xmltodict

from odbinfo.pure.datatype import Module
from odbinfo.pure.parser.basic import get_basic_tokens, scan_basic
from tests.resource import BASEDOCUMENTER


def mapiflist(function, maybelist):
    """ apply `function` on singletonlist `maybelist`
        if `maybelist` is not a list"""
    if not isinstance(maybelist, list):
        maybelist = [maybelist]
    return [function(x) for x in maybelist]


def _parse_xml(odbzip, file):
    return xmltodict.parse(odbzip.read(file))


def _read_module(odbzip, library_name,  data) -> Module:
    name = data["@library:name"]
    data = _parse_xml(odbzip, f"{library_name}/{name}.xba")
    return Module(name, "BaseDocumenter", data["script:module"]["#text"])


@pytest.mark.tooslow
def test_basedocumenter_sources(shared_datadir):
    """ parse all basedocumenter sources """
    with ZipFile((shared_datadir / BASEDOCUMENTER),
                 "r") as based:
        xlb = _parse_xml(based, "BaseDocumenter/script.xlb")
        data = xlb["library:library"]["library:element"]
        read_module = partial(_read_module, based, "BaseDocumenter")
        modules = mapiflist(read_module, data)
        for module in modules:
            print(f"Start parsing {module.name}")
            if module.name == "BD_Utils":
                module.source = module.source.replace(
                    '.setDefaultName(vFile(1)\n',
                    '.setDefaultName(vFile(1))\n')
            if module.name == "BD_Settings":
                module.source = module.source.replace(
                    "Public Sub _BD_SetActualSettings(ByVal plDatabaseID As"
                    " Long, ByRef psDatabaseName As String) As Variant",
                    "Public Sub _BD_SetActualSettings(ByVal plDatabaseID As"
                    " Long, ByRef psDatabaseName As String)")
            if module.name == "BD_Html":
                module.source = module.source.replace(
                    """, _BD_UTF8(Replace(_BD_GetLabel("PREFERENCESTITLE"),"""
                    """ "%0", BaseDocumenterTitle))""",
                    """, _BD_UTF8(Replace(_BD_GetLabel("PREFERENCESTITLE"),"""
                    """ "%0", BaseDocumenterTitle)))"""
                )
            #
            scan_basic(get_basic_tokens(module.source),
                       "BaseDocumenter", module.name)
