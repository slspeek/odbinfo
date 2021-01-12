""" Writing out to jekyll site format """
import os
from os import path
import shlex
import socket
import subprocess
import time
import contextlib
import dataclasses
import webbrowser
import pathlib

import yaml
import toml

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


def write_dict(adict, out):
    """ Writes `adict` to yaml and marks it as frontmatter """
    out.write(FRONT_MATTER_MARK)
    yaml.dump(adict, out)
    out.write(FRONT_MATTER_MARK)


def new_site(output_dir, name):
    """ Sets up a empty hugo site """
    workingdir = output_dir
    os.makedirs(workingdir, exist_ok=True)
    with chdir(workingdir):
        exitcode = os.system(f"hugo new site {name}")
        if exitcode != 0:
            raise RuntimeError(f"hugo new site failed to create site: {name}")
        datapath = path.join(path.dirname(path.dirname(__file__)), "data")
        exitcode = os.system(f"cp -r {datapath}/hugo-template/* {name}")
        if exitcode != 0:
            raise RuntimeError("unable to copy additional site sources")
        sitedir = os.path.join(workingdir, name)
    return sitedir


def _make_site(output_dir, name, tables):
    with chdir(new_site(output_dir, name)):
        with open("config.toml", "w") as cfg:
            toml.dump({"title": name,
                       "baseURL": "http://example.com/",
                       "languageCode": "en-us",
                       "theme": "minimal",
                       "menu": {"main": [{"url": "/tables/index.html",
                                          "name": "tables",
                                          "weight": 2},
                                         {"url": "/",
                                          "name": "home",
                                          "weight": 1}]}}, cfg)
        targetpath = "content/tables"
        os.makedirs(targetpath, exist_ok=True)
        for tbl in tables:
            with open(f"{targetpath}/{tbl.name}.md", "w") as out:
                write_dict(dataclasses.asdict(tbl), out)
        exitcode = os.system("hugo")
        if exitcode != 0:
            raise RuntimeError("unable to build hugo site")
    return _convert_local(output_dir, name)


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
        args = shlex.split("hugo server --disableLiveReload")
        webserver_proc = subprocess.Popen(args, shell=False)
        with chdir(".."):
            localsite = f"{name}-local"
            os.makedirs(localsite)
            while not _is_port_open(1313):
                time.sleep(0.1)
            os.system(f"wget -nH --convert-links -P {localsite} -r"
                      f" http://localhost:{port}/")

            webserver_proc.kill()
            if os.getenv("ODBINFO_NO_BROWSE", default="0") == "0":
                pwd = path.join(os.getcwd(), localsite)
                uri = pathlib.Path(pwd).as_uri()
                webbrowser.open(f"{uri}/index.html")
    return f"{result}-local"
