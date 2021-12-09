""" Writing out to hugo site format """
import os
import shutil
from datetime import datetime
from itertools import count
from pathlib import Path
from typing import Dict, List, Sequence

import toml
import yaml
from graphviz import Digraph

from odbinfo.pure.datatype import Metadata
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.metadata import TopLevelDisplayedContent
from odbinfo.pure.util import timed

FRONT_MATTER_MARK = "---\n"


def localsite(site_path: Path) -> Path:
    """returns the local site_path for `site_path`"""
    return site_path.parent / f"{site_path.name}-local"


@timed("Write graphs", indent=4)
def write_graphs(graphs: Sequence[Digraph], site_path: Path):
    """Renders the graphs"""
    for graph in graphs:
        graph.save(directory=site_path / "static" / "svg")
        graph.render(format="svg")


def frontmatter(adict: Dict[str, str], out) -> None:
    """ Writes `adict` in yaml to `out` and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(adict, out)
    out.write(FRONT_MATTER_MARK)


def rename_timestamp(directory: Path, date: datetime):
    """rename directory with timestamp"""
    timestamp = date.strftime(".bak.%Y-%m-%d--%H-%M-%S-%f")
    if directory.exists():
        directory.rename(directory.parent / f"{directory.name}{timestamp}")


def backup_old_site(site_path: Path, date: datetime = None) -> None:
    """ rename previously generated site to timestamped directory if it exits """
    if date is None:
        date = datetime.now()
    rename_timestamp(site_path, date)
    rename_timestamp(localsite(site_path), date)


# We are at odbinfo/pure/writer.py and data resides besides odbinfo
# so we go up three times, and then into 'data/hugo-template'
SITE_SKEL_PATH = Path(__file__).parent.parent.parent / "hugo-template"


def new_site(site_path: Path) -> None:
    """ Sets up a empty hugo site with odbinfo templates """
    backup_old_site(site_path)
    os.makedirs(site_path.parent, exist_ok=True)
    shutil.copytree(SITE_SKEL_PATH,
                    site_path)

    (site_path / "themes" / "minimal" / ".git").unlink()


def write_metadata(config: Configuration, metadata: Metadata):
    """writes out the `metadata` at `site_path`"""
    present_content = present_contenttypes(metadata)
    write_config(config,  present_content)
    (config.site_path / "content").mkdir()
    for content in present_content:
        write_content(metadata, content, config.site_path)


def present_contenttypes(metadata: Metadata) -> List[TopLevelDisplayedContent]:
    """returns the content_types that are present in this `metadata`"""
    return [content for content in TopLevelDisplayedContent
            if len(metadata.get_definitions(content)) > 0]


def write_config(config: Configuration,
                 present_content: Sequence[TopLevelDisplayedContent]) -> None:
    """ write out Hugo config.toml """
    menus = [{"url": f"/{content.value}/index.html",
              "name": content.value,
              "weight": weight}
             for content, weight in
             zip(present_content, count(3))]

    menus.append({"url": "/",
                  "name": "home",
                  "weight": 1})
    menus.append({"url": f"/svg/{config.name}.gv.svg",
                  "name": "picture",
                  "weight": 2})

    with open(config.site_path / "config.toml", "w", encoding='utf-8') as out:
        toml.dump({"title": config.name,
                   "baseURL": config.general.base_url,
                   "languageCode": "en-us",
                   "theme": "minimal",
                   "menu": {"main": menus,
                            }
                   }, out)


@timed("Write content", indent=4, arg=1, name=False)
def write_content(metadata: Metadata, content_type: TopLevelDisplayedContent, site_path: Path):
    """writes out `content_type` in subdir of `site_path`"""
    contentlist = metadata.get_definitions(content_type)
    targetpath = site_path / "content" / content_type.value
    targetpath.mkdir(parents=True, exist_ok=True)
    for content in contentlist:
        with open(targetpath / f"{content.title}.md",
                  "w",
                  encoding='utf-8') as out:
            frontmatter(content.to_dict(), out)


@timed("Write hugo site", indent=2)
def write_site(config: Configuration, metadata: Metadata) -> None:
    """ Writes hugo site from `metadata` """
    new_site(config.site_path)
    write_metadata(config, metadata)
    write_graphs(metadata.graphs, config.site_path)