""" Writing out to hugo site format """
import contextlib
import os
import shlex
import shutil
import socket
import subprocess
import time
import webbrowser
from contextlib import closing
from datetime import datetime
from inspect import ismethod
from itertools import count
from pathlib import Path
from typing import Dict, List, Sequence

import toml
import yaml
from graphviz import Digraph

from odbinfo.pure.datatype import Metadata
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.metadata import METADATA_CONTENT
from odbinfo.pure.util import timed

FRONT_MATTER_MARK = "---\n"


class CommandExecutionError(Exception):
    "Describes a failed command"

    def __init__(self, cmd, completed_process):
        self.completed_process = completed_process
        super().__init__(
            f"System command: {cmd} failed (returncode={completed_process.returncode})")


def run_cmd(cmd, check=True):
    " run os `cmd` and raise  if `check` was set"
    # pylint:disable=subprocess-run-check
    completed_process = subprocess.run(shlex.split(cmd),
                                       capture_output=True)
    if completed_process.returncode != 0:
        print("System command: ", cmd,
              "failed (returncode=", completed_process.returncode, ")")
        print("stdout:", completed_process.stdout.decode("utf-8"))
        print("stderr:", completed_process.stderr.decode("utf-8"))
        if check:
            raise CommandExecutionError(cmd, completed_process)


@contextlib.contextmanager
def chdir(dirname=None):
    """ Change directory and back """
    curdir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(curdir)


def localsite(site_path: Path) -> Path:
    "returns the local site_path for `site_path`"
    return site_path.parent / f"{site_path.name}-local"


@timed("Write graphs", indent=4)
def write_graphs(graphs: Sequence[Digraph], output_path: Path):
    "Renders the graphs"
    for graph in graphs:
        graph.save(directory=output_path / "static" / "svg")
        graph.render(format="svg")


def frontmatter(adict: Dict[str, str], out) -> None:
    """ Writes `adict` in yaml to `out` and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(adict, out)
    out.write(FRONT_MATTER_MARK)


def rename_timestamp(directory: Path, date: datetime):
    "rename directory with timestamp"
    timestamp = date.strftime(".bak.%Y-%m-%d--%H-%M-%S-%f")
    if directory.exists():
        directory.rename(directory.parent / f"{directory.name}{timestamp}")


def backup_old_site(site_path: Path, date: datetime = None) -> None:
    " rename previously generated site to timestamped directory if it exits "
    if date is None:
        date = datetime.now()
    rename_timestamp(site_path, date)
    rename_timestamp(localsite(site_path), date)


# We are at odbinfo/pure/writer.py and data resides besides odbinfo
# so we go up three times, and then into 'data/hugo-template'
SITE_SKEL_PATH = Path(__file__).parent.parent.parent / "data" / "hugo-template"


def new_site(site_path: Path) -> None:
    """ Sets up a empty hugo site with odbinfo templates """
    backup_old_site(site_path)
    os.makedirs(site_path.parent, exist_ok=True)
    shutil.copytree(SITE_SKEL_PATH,
                    site_path)


def build_site(site_path: Path) -> None:
    "Run the hugo system command in `working_dir`"
    with chdir(site_path):
        run_cmd("hugo", "unable to build hugo site")


def find_free_port() -> int:
    "returns a free port number"
    # pylint: disable=no-member
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(('', 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return sock.getsockname()[1]


def _is_port_open(port):
    # pylint: disable=no-member
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            return True
        return False


def convert_local(site_path: Path) -> None:
    " Uses wget to rewrite hugo website to locally browsable site"
    localsite_path = localsite(site_path)
    os.makedirs(localsite_path)

    with chdir(site_path):
        port = find_free_port()
        args = shlex.split(
            f"hugo server -p {port} --disableLiveReload --watch=false ")
        # pylint:disable=consider-using-with
        try:
            webserver_proc = subprocess.Popen(args, stderr=subprocess.DEVNULL,
                                              stdout=subprocess.DEVNULL)
            with chdir(".."):
                while not _is_port_open(port):
                    time.sleep(0.1)
                run_cmd("wget  --no-verbose"
                        f" -nH --convert-links -P {localsite_path.name}"
                        " -r --level=100"
                        f" http://localhost:{port}/", check=True)
        finally:
            webserver_proc.kill()


def open_browser(site_dir: Path) -> None:
    "Opens a webbrowser on `site_dir`"
    if os.getenv("ODBINFO_NO_BROWSE", default="0") == "0":
        site_abs_path = site_dir.resolve() / "index.html"
        webbrowser.open(site_abs_path.as_uri())


def write_metadata(config: Configuration, metadata: Metadata):
    "writes out the `metadata` at `site_path`"
    present_content = present_contenttypes(metadata)
    write_config(config,  present_content)
    for content in present_content:
        write_content(metadata, content, config.site_path)


def _get_metadata_attr(metadata: Metadata, attribute: str):
    meta_attribute = getattr(metadata, f"{attribute}_defs")
    if ismethod(meta_attribute):
        meta_attribute = meta_attribute()
    return meta_attribute


def present_contenttypes(metadata: Metadata) -> List[str]:
    "returns the content_types that are present in this `metadata`"
    return [content for content in METADATA_CONTENT
            if len(_get_metadata_attr(metadata, content)) > 0]


def write_config(config: Configuration, present_content: Sequence[str]) -> None:
    " write out Hugo config.toml "
    menus = [{"url": f"/{name}/index.html",
              "name": name,
              "weight": weight}
             for name, weight in
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
def write_content(metadata: Metadata, content_type: str, site_path: Path):
    "writes out `content_type` in subdir of `site_path`"
    contentlist = _get_metadata_attr(metadata, content_type)
    targetpath = site_path / "content" / content_type
    targetpath.mkdir(parents=True, exist_ok=True)
    for content in contentlist:
        with open(targetpath / f"{content.title}.md",
                  "w",
                  encoding='utf-8') as out:
            frontmatter(content.to_dict(), out)


@timed("Write and build hugo site", indent=2)
def make_site(config: Configuration, metadata: Metadata) -> Path:
    """ Builds report in from `metadata` """
    new_site(config.site_path)
    write_metadata(config, metadata)
    write_graphs(metadata.graphs, config.site_path)

    build_site(config.site_path)
    convert_local(config.site_path)
    localsite_path = localsite(config.site_path)
    open_browser(localsite_path)
    return localsite_path
