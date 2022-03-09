""" shared reading utilities"""
from typing import List, Union, cast
from xml.dom.minidom import Element, Node, parseString
from zipfile import ZipFile

CONTENT_XML = "content.xml"


def document_element_from_string(source: Union[bytes, str]) -> Element:
    """ returns the root element of parsed `source` dom tree"""
    return parseString(source).documentElement


def document_element(oozip: ZipFile, path: str) -> Element:
    """ returns the document element obtained
        by parsing the contents of `path` in `oozip`"""
    return document_element_from_string(oozip.read(path))


def child_elements(element: Element) -> List[Element]:
    """ returns direct-child-elements of `element`"""
    return \
        [cast(Element, child)
         for child in element.childNodes if child.nodeType == Node.ELEMENT_NODE]


def child_elements_by_tagname(element: Element, tagname: str) -> List[Element]:
    """ returns the direct-child elements of `element` that match the
        tag name `tagName`
     """
    return [
        child for child in child_elements(element) if child.tagName == tagname
    ]


def attr_default(element: Element, attribute_name: str, default_value: str):
    """Returns `def_value` if `elem` has no attribute `attr` else the attribute value"""
    value = element.getAttribute(attribute_name)
    if value == "":
        return default_value
    return value


def get_elements_from_href(odbzip: ZipFile, href: str,
                           element_name: str) -> List[Element]:
    """ Returns the elements with name `element_name` from the subdocument under `href` in `odbzip`
    """
    return document_element(odbzip, f"{href}/{CONTENT_XML}" if href else
                            CONTENT_XML).getElementsByTagName(element_name)
