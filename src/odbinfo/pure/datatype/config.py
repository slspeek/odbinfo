""" Configuration classes """

from pathlib import Path
from typing import List, Optional

import yaml
from pydantic import BaseModel


class ConfigurationAttributeNotSet(Exception):
    """For attributes that need to be there"""

    def __init__(self, attribute: str):
        self.attribute = attribute
        super().__init__(f"Configuration attribute {attribute} was not set")


class GeneralConfig(BaseModel):
    """ General options """

    output_dir: Optional[str] = None
    base_url: str = "http://odbinfo.org/"


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

ALWAYS_EXCLUDED = ["metadata", "basictoken", "sqltoken"]


class TextDocumentsConfig(BaseModel):
    """ Config for the search of textdocuments """

    db_registration_id: Optional[str] = None
    search_locations: Optional[List[str]] = None


class GraphConfig(BaseModel):
    """ Graph options """
    user_excludes: List[str] = EXCLUDED_TYPES
    type_attrs: dict = TYPE_ATTRS
    relation_attrs: dict = RELATION_ATTRS
    parent_edge_attrs: dict = PARENT_EDGE_ATTRS
    collapse_multiple_uses: bool = True
    relevant_controls: bool = True

    @property
    def excludes(self):
        """property 'excluded' consists off ALWAYS_EXCLUDED and user_excludes"""
        return ALWAYS_EXCLUDED + self.user_excludes


class Configuration(BaseModel):
    """ Overall configuration """

    name: str = ""
    general: GeneralConfig = GeneralConfig()
    graph: GraphConfig = GraphConfig()
    textdocuments: TextDocumentsConfig = TextDocumentsConfig()

    @property
    def site_path(self) -> Path:
        """returns the path of the hugo site"""
        if self.general.output_dir is None:
            raise ConfigurationAttributeNotSet("general.output_dir")
        return Path(self.general.output_dir) / self.name


def create_configuration(name="", output_dir=None) -> Configuration:
    """ returns configuration """
    return \
        Configuration(name=name, general={"output_dir": output_dir})


def set_configuration_defaults(config: Configuration, odbpath: Path):
    """ sets sensible defaults """
    config.name = odbpath.stem
    if not config.general.output_dir:
        config.general.output_dir = str(odbpath.parent / ".odbinfo")
    if not config.textdocuments.db_registration_id:
        config.textdocuments.db_registration_id = config.name
    if config.textdocuments.search_locations is None:
        config.textdocuments.search_locations = [str(odbpath.parent)]


def default_config_path() -> Path:
    """ returns the default location of the configuration file """
    return Path.home() / ".odbinfo" / "config.yaml"


def load_configuration(config_path: Path) -> Configuration:
    """ Loads configuration from file `config_path`"""
    with config_path.open(encoding='utf-8') as file:
        return Configuration(**yaml.load(file, Loader=yaml.Loader))


def write_configuration(config: Configuration, config_path: Path) -> None:
    """ Writes `config` to `config_path` in YAML format"""
    with config_path.open(mode='w', encoding='utf-8') as output_file:
        yaml.dump(config.dict(), output_file)


def get_configuration(config_path: Path = default_config_path()) -> Configuration:
    """ reads configuration from `config_path` if exits "\
        " otherwise a default configuration is written in `config_path`"""
    if not config_path.exists():
        if not config_path.parent.exists():
            config_path.parent.mkdir()
        config = create_configuration()
        write_configuration(config, config_path)
        return config
    return load_configuration(config_path)
