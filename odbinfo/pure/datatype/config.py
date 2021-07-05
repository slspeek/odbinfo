" Configuration classes "

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class GeneralConfig:
    " General options "
    output_dir: Optional[str]


TYPE_ATTRS = {
    "Table": {"shape": "cylinder", "fillcolor": "#a7c3eb", "style": "filled"},
    "View": {"shape": "hexagon"},
    "Query": {"shape": "ellipse"},
    "Form": {"shape": "rect", "style": "filled", "fillcolor": "#ffcc99"},
    "Report": {"shape": "rectangle"},
    "Dialog": {"shape": "trapezium"},
    "Module": {"shape": "component"},
    "Field": {"shape": "invhouse"},
    "SubForm": {"shape": "doubleoctagon",
                "style": "filled", "fillcolor": "#d3d3d3"},
    "Grid": {"shape": "Mdiamond"},
    "Control": {"shape": "octagon", "style": "filled", "fillcolor": "#d3d3d3"},
    "BasicFunction": {"shape": "component"}
}

RELATION_ATTRS = {
    ("Table", "Table"): {},
    ("Control", "Table"): {"arrowhead": "box", "color": "red"},
    ("Control", "Query"): {"arrowhead": "dot"},
    ("SubForm", "Table"): {"arrowhead": "box", "color": "red"},
    ("BasicFunction", "BasicFunction"): {"arrowhead": "dot", "color": "#90EE90"},
    ("Form", "Table"): {"arrowhead": "box", "color": "red"},
    ("View", "Table"): {"arrowhead": "dot"},
    ("Form", "View"): {"arrowhead": "dot"},
    ("Form", "Query"): {"arrowhead": "dot"},
    ("Query", "Table"): {"arrowhead": "dot"},
    ("Query", "Query"): {"arrowhead": "dot"}
}

TYPE_HREF = {
    "Table": "tables",
    "View": "views",
    "Query": "Queries",
    "Form": "ControlsByForm",
    "Report": "FullIndex",
    "Dialog": "FullIndex",
    "Module": "Modules",
    "Field": "FullIndex",
    "SubForm": "FullIndex",
    "Grid": "FullIndex",
    "Control": "ControlsByForm",
    "BasicFunction": "ProceduresByModule"
}

EXCLUDED_TYPES = ["Metadata", "QueryColumn", "Column", "PythonLibrary",
                  "PythonModule"]


@dataclass
class GraphConfig:
    " Graph options "
    excludes: List[str]
    type_attrs: dict
    relation_attrs: dict
    type_href: Dict[str, str]


@dataclass
class Configuration:
    " Overall configuration "
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
                TYPE_HREF
            )
        )
