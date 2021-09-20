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
from os import path
from pathlib import Path
from typing import Dict

import toml
import yaml

from odbinfo.pure.datatype import (BasicFunction, Metadata, Module, Token,
                                   content_type)
from odbinfo.pure.datatype.config import Configuration
from odbinfo.pure.datatype.metadata import METADATA_CONTENT
from odbinfo.pure.util import timed

FRONT_MATTER_MARK = "---\n"


def run_quiet(cmd):
    " run os `cmd`. Returns the CompletedProcess"
    #pylint: disable=subprocess-run-check
    return subprocess.run(shlex.split(cmd),
                          stderr=subprocess.DEVNULL,
                          stdout=subprocess.DEVNULL)


def run_checked(cmd, error_mesg):
    " run os `cmd` and raise RuntimeError with `error_mesg`"
    completed_process = run_quiet(cmd)
    if completed_process.returncode != 0:
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


def clean_old_site(output_dir: Path, name: str):
    " remove previous generated site if it exits "

    def rmtree(directory: Path):
        if directory.is_dir() and directory.exists():
            shutil.rmtree(directory)

    rmtree(output_dir / name)
    rmtree(output_dir / f"{name}-local")


def new_site(output_dir: str, name: str):
    """ Sets up a empty hugo site with odbinfo templates """
    clean_old_site(Path(output_dir), name)
    os.makedirs(Path(output_dir), exist_ok=True)
    shutil.copytree(Path(DATA_DIR) / "hugo-template",
                    Path(output_dir) / name)


def preprocess_metadata(metadata):
    " clear some fields for speed "
    for obj in metadata.all_objects():
        obj.parent = None
        del obj.parent
    _cleanup_tokens(metadata)


def _cleanup_tokens(metadata):
    def clean_token(token):
        del token.hidden

        if not token.link:
            token.obj_id = None
            del token.obj_id
            token.title = None
            del token.title
            token.link = None
            del token.link
        if not token.cls:
            token.cls = None
            del token.cls

    def replace_qtoken(token: Token) -> Dict:
        del token.index
        clean_token(token)
        return token.__dict__

    def replace_bftoken(token: Token) -> Dict:
        clean_token(token)
        return token.__dict__

    for query in (list(metadata.embeddedquery_defs())
                  + metadata.query_defs + metadata.view_defs):
        query.tokens = list(map(replace_qtoken, query.tokens))
        query.table_tokens = []

    for module in metadata.module_defs():
        del module.source
        module.tokens = list(map(replace_bftoken, module.tokens))

    for function in metadata.basicfunction_defs():
        del function.body_tokens
        del function.calls
        function.tokens = list(map(replace_bftoken, function.tokens))
        del function.strings


@timed("Write and build hugo site", indent=2)
def make_site(config, metadata):
    """ Builds report in `output_dir` with `name` from `metadata` """
    name = config.name
    output_dir = config.general.output_dir
    new_site(output_dir, name)

    with chdir(os.path.join(output_dir, name)):
        _write_metadata(config, metadata)
        _write_graphs(metadata)
        run_checked("hugo", "unable to build hugo site")
    _convert_local(output_dir, name)
    localsite = f"{output_dir}/{name}-local"
    _open_browser(localsite, os.getcwd())
    return localsite


def clear_fields_after(metadata: Metadata, acontent_type: str) -> None:
    " clear tokens after basicfunctions were written "
    if acontent_type == content_type(BasicFunction):
        for func in metadata.basicfunction_defs():
            func.tokens = []
    if acontent_type == content_type(Module):
        for module in metadata.module_defs():
            module.tokens = []


def _write_metadata(config: Configuration, metadata: Metadata):
    preprocess_metadata(metadata)
    _write_config(config, config.name, metadata)
    for content in METADATA_CONTENT:
        _write_content(metadata, content)
        clear_fields_after(metadata, content)


def _get_metadata_attr(metadata: Metadata, attribute: str):
    meta_attribute = getattr(metadata, f"{attribute}_defs")
    if ismethod(meta_attribute):
        meta_attribute = meta_attribute()
    return meta_attribute


def _write_config(config, site_name, metadata):
    def _menu(pairs):
        name, weight = pairs
        meta_attribute = _get_metadata_attr(metadata, name)
        if len(meta_attribute) > 0:
            return {"url": f"/{name}/index.html",
                    "name": name,
                    "weight": weight}
        return None
    menus_defs = list(
        zip(METADATA_CONTENT, range(3, len(METADATA_CONTENT) + 3)))
    menus = list(filter(lambda x: x is not None, map(_menu, menus_defs)))
    menus.append({"url": "/",
                  "name": "home",
                  "weight": 1})
    menus.append({"url": f"/svg/{site_name}.gv.svg",
                  "name": "picture",
                  "weight": 2})

    with open("config.toml", "w") as cfg:
        toml.dump({"title": site_name,
                   "baseURL": config.general.base_url,
                   "languageCode": "en-us",
                   "theme": "minimal",
                   "menu": {"main": menus,
                            }
                   }, cfg)


@timed("Write content", indent=4, arg=1, name=False)
def _write_content(metadata: Metadata, name):
    contentlist = _get_metadata_attr(metadata, name)
    if len(contentlist) > 0:
        targetpath = Path("content") / name
        targetpath.mkdir(parents=True, exist_ok=True)
        for content in contentlist:
            with open(targetpath / f"{content.title}.md", "w") as out:
                _frontmatter(content, out)


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
                run_quiet(f"wget  -nH --convert-links -P {localsite} -r"
                          f" http://localhost:{port}/ ")
        finally:
            webserver_proc.kill()


def _open_browser(site_dir,
                  cwd,
                  open_browser=webbrowser.open,
                  env_info=os.getenv("ODBINFO_NO_BROWSE", default="0")
                  ):
    if env_info == "0":
        site_abs_path = path.join(cwd, site_dir, "index.html")
        site_uri = pathlib.Path(site_abs_path).as_uri()
        open_browser(site_uri)
