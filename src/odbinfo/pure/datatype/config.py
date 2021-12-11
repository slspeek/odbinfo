""" Configuration classes """

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from odbinfo.pure.datatype import Metadata
from odbinfo.pure.datatype.base import content_type
from odbinfo.pure.datatype.exec import BasicToken
from odbinfo.pure.datatype.tabular import SQLToken


class ConfigurationAttributeNotSet(Exception):
    """For attributes that need to be there"""

    def __init__(self, attribute: str):
        self.attribute = attribute
        super().__init__(f"Configuration attribute {attribute} was not set")


@dataclass
class GeneralConfig:
    """ General options """
    output_dir: Optional[str]
    base_url: str


PARENT_EDGE_ATTRS = {
    "style": "dashed",
    "color": "#ffcc99",
    "arrowhead": "none",
}

TYPE_ATTRS = {
    "listbox": {},
    "library": {},
    "textdocument": {},
    "table": {"shape": "cylinder", "fillcolor": "#a7c3eb", "style": "filled"},
    "view": {"shape": "hexagon"},
    "query": {"shape": "ellipse"},
    "embeddedquery": {"shape": "ellipse"},
    "eventlistener": {"shape": "ellipse",
                      "style": "filled", "fillcolor": "lightblue"},
    "form": {"shape": "rect", "style": "filled", "fillcolor": "#ffcc99"},
    "key": {},
    "index": {},
    "column": {},
    "querycolumn": {},
    "pythonlibrary": {},
    "pythonmodule": {},
    "databasedisplay": {},
    "report": {"shape": "rectangle"},
    "dialog": {"shape": "trapezium"},
    "module": {"shape": "component"},
    "field": {"shape": "invhouse"},
    "subform": {"shape": "doubleoctagon",
                "style": "filled", "fillcolor": "#d3d3d3"},
    "grid": {"shape": "Mdiamond"},
    "control": {"shape": "octagon", "style": "filled", "fillcolor": "#d3d3d3"},
    "basicfunction": {"shape": "component"}
}

RELATION_ATTRS = {
    ("table", "table"): {},
    ("control", "table"): {"arrowhead": "box", "color": "red"},
    ("control", "query"): {"arrowhead": "dot"},
    ("subform", "table"): {"arrowhead": "box", "color": "red"},
    ("basicfunction", "basicfunction"): {"arrowhead": "dot", "color": "#90EE90"},
    ("form", "table"): {"arrowhead": "box", "color": "red"},
    ("view", "table"): {"arrowhead": "dot"},
    ("form", "view"): {"arrowhead": "dot"},
    ("form", "query"): {"arrowhead": "dot"},
    ("query", "table"): {"arrowhead": "dot"},
    ("query", "query"): {"arrowhead": "dot"}
}

EXCLUDED_TYPES: List[str] = ["key", "index", "eventlistener",
                             "library",
                             "querycolumn", "column", "pythonlibrary",
                             "pythonmodule", "databasedisplay"]

# EXCLUDED_TYPES: List[str] = []

ALWAYS_EXCLUDED = [content_type(clazz)
                   for clazz in [BasicToken, SQLToken, Metadata]]


@dataclass
class TextDocumentsConfig:
    """ Config for the search of textdocuments """
    db_registration_id: Optional[str]
    search_locations: Optional[List[str]]


@dataclass
class GraphConfig:
    """ Graph options """
    user_excludes: List[str]
    type_attrs: dict
    relation_attrs: dict
    parent_edge_attrs: dict
    collapse_multiple_uses: bool
    relevant_controls: bool

    @property
    def excludes(self):
        """property 'excluded' consists off ALWAYS_EXCLUDED and user_excludes"""
        return ALWAYS_EXCLUDED + self.user_excludes


@dataclass
class Configuration:
    """ Overall configuration """

    name: str
    general: GeneralConfig
    graph: GraphConfig
    textdocuments: TextDocumentsConfig

    @property
    def site_path(self) -> Path:
        """returns the path of the hugo site"""
        if self.general.output_dir is None:
            raise ConfigurationAttributeNotSet("general.output_dir")
        return Path(self.general.output_dir) / self.name


def get_configuration(name=None, output_dir=None) -> Configuration:
    """ returns configuration """
    return \
        Configuration(
            name,
            GeneralConfig(output_dir, "http://odbinfo.org/"),
            GraphConfig(
                EXCLUDED_TYPES,
                TYPE_ATTRS,
                RELATION_ATTRS,
                PARENT_EDGE_ATTRS,
                True,
                True
            ),
            TextDocumentsConfig(None, None)
        )
