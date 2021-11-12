""" Writing out to hugo site format """
import contextlib
import os
import pathlib
import shlex
import shutil
import socket
import subprocess
import time
import webbrowser
from inspect import ismethod
from itertools import count
from os import path
from pathlib import Path

import toml
import yaml

from odbinfo.pure.datatype import Metadata
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.metadata import METADATA_CONTENT
from odbinfo.pure.util import timed

FRONT_MATTER_MARK = "---\n"


def run_cmd(cmd, check=True, error_mesg=None):
    " run os `cmd` and raise RuntimeError with `error_mesg`, if `check` was set"
    # pylint:disable=subprocess-run-check
    completed_process = subprocess.run(shlex.split(cmd),
                                       capture_output=True)
    if completed_process.returncode != 0:
        print("System command: ", cmd,
              "failed (returncode=", completed_process.returncode, ")")
        print("stdout:", completed_process.stdout.decode("utf-8"))
        print("stderr:", completed_process.stderr.decode("utf-8"))
        if check:
            raise RuntimeError(error_mesg)


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


# We are at odbinfo/pure/writer.py and data resides besides odbinfo
# so we go up three times, and then into 'data'
DATA_DIR = path.join(path.dirname(path.dirname(path.dirname(__file__))),
                     "data")


@timed("Write graphs", indent=4)
def _write_graphs(metadata):
    for graph in metadata.graphs:
        graph.save(directory="static/svg")
        graph.render(format="svg")


def _frontmatter(obj, out):
    """ Writes `adict` to yaml and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(obj, out)
    out.write(FRONT_MATTER_MARK)


def clean_old_site(output_dir: Path, name: str) -> None:
    " remove previous generated site if it exits "

    def rmtree(directory: Path):
        if directory.is_dir() and directory.exists():
            shutil.rmtree(directory)

    rmtree(output_dir / name)
    rmtree(output_dir / f"{name}-local")


def new_site(output_dir: str, name: str) -> None:
    """ Sets up a empty hugo site with odbinfo templates """
    clean_old_site(Path(output_dir), name)
    os.makedirs(Path(output_dir), exist_ok=True)
    shutil.copytree(Path(DATA_DIR) / "hugo-template",
                    Path(output_dir) / name)


@timed("Write and build hugo site", indent=2)
def make_site(config, metadata):
    """ Builds report in `output_dir` with `name` from `metadata` """
    name = config.name
    output_dir = config.general.output_dir
    new_site(output_dir, name)

    with chdir(os.path.join(output_dir, name)):
        _write_metadata(config, metadata)
        _write_graphs(metadata)
        run_cmd("hugo", "unable to build hugo site")
    _convert_local(output_dir, name)
    localsite = f"{output_dir}/{name}-local"
    _open_browser(localsite)
    return localsite


def _write_metadata(config: Configuration, metadata: Metadata):
    write_config(config,  metadata)
    for content in METADATA_CONTENT:
        _write_content(metadata, content)


def _get_metadata_attr(metadata: Metadata, attribute: str):
    meta_attribute = getattr(metadata, f"{attribute}_defs")
    if ismethod(meta_attribute):
        meta_attribute = meta_attribute()
    return meta_attribute


def write_config(config: Configuration, metadata: Metadata) -> None:
    " write out Hugo config.toml "
    present_content = [content for content in METADATA_CONTENT
                       if len(_get_metadata_attr(metadata, content)) > 0]
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

    with open("config.toml", "w", encoding='utf-8') as out:
        toml.dump({"title": config.name,
                   "baseURL": config.general.base_url,
                   "languageCode": "en-us",
                   "theme": "minimal",
                   "menu": {"main": menus,
                            }
                   }, out)


@timed("Write content", indent=4, arg=1, name=False)
def _write_content(metadata: Metadata, name):
    contentlist = _get_metadata_attr(metadata, name)
    if len(contentlist) > 0:
        targetpath = Path("content") / name
        targetpath.mkdir(parents=True, exist_ok=True)
        for content in contentlist:
            with open(targetpath / f"{content.title}.md",
                      "w",
                      encoding='utf-8') as out:
                _frontmatter(content.to_dict(), out)


def _is_port_open(port):
    # pylint: disable=no-member
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            return True
        return False


def _convert_local(output_dir, name):
    result = path.join(output_dir, name)
    with chdir(result):
        port = 1313
        args = shlex.split("hugo server --disableLiveReload --watch=false ")
        # pylint:disable=consider-using-with
        try:
            webserver_proc = subprocess.Popen(args, stderr=subprocess.DEVNULL,
                                              stdout=subprocess.DEVNULL)
            with chdir(".."):
                localsite = f"{name}-local"
                os.makedirs(localsite)
                while not _is_port_open(port):
                    time.sleep(0.1)
                run_cmd("wget  --no-verbose"
                        f" -nH --convert-links -P {localsite}"
                        " -r --level=100"
                        f" http://localhost:{port}/", check=False)
        finally:
            webserver_proc.kill()


def _open_browser(site_dir):
    if os.getenv("ODBINFO_NO_BROWSE", default="0") == "0":
        site_abs_path = path.join(os.getcwd(), site_dir, "index.html")
        site_uri = pathlib.Path(site_abs_path).as_uri()
        webbrowser.open(site_uri)
