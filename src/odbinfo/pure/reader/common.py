""" shared reading utilities"""
from typing import List, Tuple, Union, cast
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


def elements_from_subdoc(odbzip: ZipFile, href: str,
                         desired_tag: str) -> List[Element]:
    """ Returns the elements with name `element_name` from the subdocument under `href` in `odbzip`
    """
    return document_element(odbzip, f"{href}/{CONTENT_XML}" if href else
                            CONTENT_XML).getElementsByTagName(desired_tag)


def subdocuments_elements(odbzip: ZipFile, specified_by_tag: str,
                          desired_tag: str) -> List[Tuple[str, Element]]:
    """ Reads the subdocuments specified in the main document "content.xml" by
        the <db:component> elements under the `specified_by_tag`.
        It returns a list of tuples of the name of the subdocument and the `desired_tag` from
        the subdocument. (This is used for form and report reading)
    """
    specifying_elements = elements_from_subdoc(odbzip,
                                               "",
                                               desired_tag=specified_by_tag)
    if not specifying_elements:
        # The specifying tag is not present
        return []

    db_component_elements = specifying_elements[0].getElementsByTagName(
        "db:component")

    return \
        [(db_component.getAttribute("db:name"),
          elements_from_subdoc(odbzip=odbzip,
                               href=db_component.getAttribute("xlink:href"),
                               desired_tag=desired_tag)[0])
         for db_component in db_component_elements]
