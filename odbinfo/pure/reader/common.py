" shared reading utilities"
from typing import List, cast
from xml.dom.minidom import Element, Node, parseString
from zipfile import ZipFile


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


def attr_default(elem: Element, attr: str, def_value: str):
    "return `def_value` if `elem` has no attribute `attr` else the attribute value"
    value = elem.getAttribute(attr)
    if value == "":
        return def_value
    return value
