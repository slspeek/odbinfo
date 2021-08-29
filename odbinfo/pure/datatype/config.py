" Configuration classes "

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class GeneralConfig:
    " General options "
    output_dir: Optional[str]


TYPE_ATTRS = {
    "listbox": {},
    "library": {},
    "textdocument": {},
    "table": {"shape": "cylinder", "fillcolor": "#a7c3eb", "style": "filled"},
    "view": {"shape": "hexagon"},
    "query": {"shape": "ellipse"},
    "embeddedquery": {"shape": "ellipse"},
    "form": {"shape": "rect", "style": "filled", "fillcolor": "#ffcc99"},
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

EXCLUDED_TYPES = ["eventlistener", "metadata", "key", "index",
                  "token", "querycolumn", "column", "pythonlibrary",
                  "pythonmodule", "databasedisplay"]


@dataclass
class GraphConfig:
    " Graph options "
    excludes: List[str]
    type_attrs: dict
    relation_attrs: dict
    collapse_multiple_uses: bool
    relevant_controls: bool


@dataclass
class Configuration:
    " Overall configuration "

    name: Optional[str] = field(init=False)
    general: GeneralConfig
    graph: GraphConfig


def get_configuration() -> Configuration:
    " returns configuration "
    return \
        Configuration(
            GeneralConfig(None),
            GraphConfig(
                EXCLUDED_TYPES,
                TYPE_ATTRS,
                RELATION_ATTRS,
                True,
                True
            )
        )
