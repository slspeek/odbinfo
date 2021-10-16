" shared reading utilities"
from typing import List, cast
from xml.dom.minidom import Element, Node, parseString
from zipfile import ZipFile

import xmltodict


def document_element(source) -> Element:
    " returns the root element of parsed `source` dom tree"
    return parseString(source).documentElement


def document(oozip: ZipFile, path: str) -> Element:
    " return dom.Document with contents of `path` in `oozip`"
    return document_element(oozip.read(path))


def child_elements(elem: Element) -> List[Element]:
    " return direct-child-elements of `elem`"
    return \
        [cast(Element, child)
         for child in elem.childNodes if child.nodeType == Node.ELEMENT_NODE]


def child_elements_by_tagname(elem: Element, tagname: str) -> List[Element]:
    " direct-child-elements by tagName"
    return [child for child in child_elements(elem) if child.tagName == tagname]


def mapiflist(function, maybelist):
    """ apply `function` on singletonlist `maybelist`
        if `maybelist` is not a list"""
    if not isinstance(maybelist, list):
        maybelist = [maybelist]
    return list(map(function, maybelist))


def _office_body(info):
    return info["office:document-content"]["office:body"]


def _parse_xml(odbzip, file):
    return xmltodict.parse(odbzip.read(file))


def _collect_attribute(data, attribute):

    def collect_attr(info):
        values = []
        if not info:
            return values
        if not hasattr(info, "items"):
            return values
        for key, value in info.items():
            if key == attribute:
                values.append(value)
                continue
            if key.startswith("@"):
                continue
            values.extend(_collect_attribute(value, attribute))
        return values
    return sum(mapiflist(collect_attr, data), [])


def _body_elem(oozip, path):
    content = _parse_xml(oozip, path)
    return _office_body(content)


def attr_default(elem: Element, attr: str, def_value: str):
    "return `def_value` if `elem` has no attribute `attr` else the attribute value"
    value = elem.getAttribute(attr)
    if value == "":
        return def_value
    return value
