""" Writing out to hugo site format """
import contextlib
import dataclasses
import os
import pathlib
import shlex
import socket
import subprocess
import time
import webbrowser
from functools import partial
from inspect import ismethod
from os import path

import toml
import yaml

from odbinfo.pure.datatype import Metadata

FRONT_MATTER_MARK = "---\n"


def run_checked(cmd, error_mesg):
    " run os `cmd` and raise RuntimeError with `error_mesg`"
    exit_code = os.system(cmd)
    if exit_code != 0:
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


METADATA_CONTENT = ["tables",
                    "queries",
                    "views",
                    "forms",
                    "reports",
                    "libraries",
                    "modules",
                    "callables",
                    "pylibs",
                    "pymodules",
                    "documents"]


def _frontmatter(adict, out):
    """ Writes `adict` to yaml and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(adict, out)
    out.write(FRONT_MATTER_MARK)


def new_site(output_dir, name):
    """ Sets up a empty hugo site with odbinfo templates """
    os.makedirs(output_dir, exist_ok=True)
    with chdir(output_dir):
        run_checked(f"hugo new site {name} > /dev/null",
                    f"hugo new site failed to create site: {name}")
        run_checked(f"cp -r {DATA_DIR}/hugo-template/* {name}",
                    f"unable to copy additional site sources from {DATA_DIR}")


def make_site(output_dir, name, metadata):
    """ Builds report in `output_dir` with `name` from `metadata` """
    new_site(output_dir, name)

    with chdir(os.path.join(output_dir, name)):
        _write_metadata(name, metadata)
        run_checked("hugo", "unable to build hugo site")
    _convert_local(output_dir, name)
    localsite = f"{output_dir}/{name}-local"
    _open_browser(localsite, os.getcwd())


def _write_metadata(name, metadata: Metadata):
    _write_config(name, metadata)
    list(map(partial(_write_content, metadata), METADATA_CONTENT))


def _get_metadata_attr(metadata: Metadata, attribute: str):
    meta_attribute = getattr(metadata, attribute)
    if ismethod(meta_attribute):
        meta_attribute = meta_attribute()
    return meta_attribute


def _write_config(site_name, metadata):
    def _menu(pairs):
        name, weight = pairs
        meta_attribute = _get_metadata_attr(metadata, name)
        if len(meta_attribute) > 0:
            return {"url": f"/{name}/index.html",
                    "name": name,
                    "weight": weight}
        return None
    menus_defs = list(
        zip(METADATA_CONTENT, range(2, len(METADATA_CONTENT) + 2)))
    menus = list(filter(lambda x: x is not None, map(_menu, menus_defs)))
    menus.append({"url": "/",
                  "name": "home",
                  "weight": 1})
    with open("config.toml", "w") as cfg:
        toml.dump({"title": site_name,
                   "baseURL": "http://example.com/",
                   "languageCode": "en-us",
                   "theme": "minimal",
                   "menu": {"main": menus,
                            }
                   }, cfg)


def _write_content(metadata: Metadata, name):
    contentlist = _get_metadata_attr(metadata, name)
    if len(contentlist) > 0:
        targetpath = f"content/{name}"
        os.makedirs(targetpath, exist_ok=True)
        for content in contentlist:
            with open(f"{targetpath}/{content.title}.md", "w") as out:
                _frontmatter(dataclasses.asdict(content), out)


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
        args = shlex.split("hugo server --disableLiveReload --watch=false "
                           "  2> /dev/null 1>&2")
        # pylint:disable=consider-using-with
        webserver_proc = subprocess.Popen(args)
        with chdir(".."):
            localsite = f"{name}-local"
            os.makedirs(localsite)
            while not _is_port_open(port):
                time.sleep(0.1)
            os.system(f"wget -nH --convert-links -P {localsite} -r"
                      f" http://localhost:{port}/ > /dev/null 2>&1")

            webserver_proc.kill()
            #_open_browser(localsite, os.getcwd())


def _open_browser(site_dir,
                  cwd,
                  open_browser=webbrowser.open,
                  env_info=os.getenv("ODBINFO_NO_BROWSE", default="0")
                  ):
    if env_info == "0":
        site_abs_path = path.join(cwd, site_dir, "index.html")
        site_uri = pathlib.Path(site_abs_path).as_uri()
        open_browser(site_uri)
