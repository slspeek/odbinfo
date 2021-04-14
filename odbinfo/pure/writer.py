""" Writing out to jekyll site format """
import contextlib
import dataclasses
import os
import pathlib
import shlex
import socket
import subprocess
import time
import webbrowser
from os import path

import toml
import yaml

FRONT_MATTER_MARK = "---\n"


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
DATA_DIR = path.join(path.dirname(
    path.dirname(path.dirname(__file__))), "data")


def _frontmatter(adict, out):
    """ Writes `adict` to yaml and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(adict, out)
    out.write(FRONT_MATTER_MARK)


def new_site(output_dir, name):
    """ Sets up a empty hugo site with odbinfo templates """
    os.makedirs(output_dir, exist_ok=True)
    with chdir(output_dir):
        exitcode = os.system(f"hugo new site {name} > /dev/null")
        if exitcode != 0:
            raise RuntimeError(f"hugo new site failed to create site: {name}")
        exitcode = os.system(f"cp -r {DATA_DIR}/hugo-template/* {name}")
        if exitcode != 0:
            raise RuntimeError("unable to copy additional site sources from "
                               f"{DATA_DIR}")
        sitedir = os.path.join(output_dir, name)
    return sitedir


def make_site(output_dir, name, metadata):
    """ Builds report in `output_dir` with `name` from `metadata` """
    with chdir(new_site(output_dir, name)):
        _write_config(name)
        _write_content("tables", metadata.tables)
        _write_content("views", metadata.views)
        _write_content("queries", metadata.queries)
        _write_content("libraries", metadata.libraries)
        _write_content("modules", metadata.modules())
        _write_content("macros", metadata.callables())
        _write_content("pylibs", metadata.pythonlibraries)
        _write_content("pymodules", metadata.pymodules())
        _write_content("reports", metadata.reports)

        exitcode = os.system("hugo")
        if exitcode != 0:
            raise RuntimeError("unable to build hugo site")
    return _convert_local(output_dir, name)


def _menu(pairs):
    name, weight = pairs
    return \
        {"url": f"/{name}/index.html",
         "name": name,
         "weight": weight}


def _write_config(name):
    menus_defs = [
        ("tables", 2),
        ("queries", 3),
        ("views", 4),
        ("reports", 6),
        ("libraries", 8),
        ("modules", 9),
        ("macros", 10),
        ("pylibs", 11),
        ("pymodules", 12)
    ]
    menus = list(map(_menu, menus_defs))
    menus.append({"url": "/",
                  "name": "home",
                  "weight": 1})
    with open("config.toml", "w") as cfg:
        toml.dump({"title": name,
                   "baseURL": "http://example.com/",
                   "languageCode": "en-us",
                   "theme": "minimal",
                   "menu": {"main": menus,
                            }
                   }, cfg)


def _write_content(name, contentlist):
    def basename(content):
        if hasattr(content, "title"):
            return content.title
        return content.name

    targetpath = f"content/{name}"
    os.makedirs(targetpath, exist_ok=True)
    for content in contentlist:
        with open(f"{targetpath}/{basename(content)}.md", "w") as out:
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
        webserver_proc = subprocess.Popen(args)
        with chdir(".."):
            localsite = f"{name}-local"
            os.makedirs(localsite)
            while not _is_port_open(port):
                time.sleep(0.1)
            os.system(f"wget -nH --convert-links -P {localsite} -r"
                      f" http://localhost:{port}/ > /dev/null 2>&1")

            webserver_proc.kill()
            if os.getenv("ODBINFO_NO_BROWSE", default="0") == "0":
                pwd = path.join(os.getcwd(), localsite)
                uri = pathlib.Path(pwd).as_uri()
                webbrowser.open(f"{uri}/index.html")
    return f"{result}-local"
