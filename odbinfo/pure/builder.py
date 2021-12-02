""" builder module: calls gohugo"""
import os
import shlex
import socket
import subprocess
import time
import webbrowser
from contextlib import closing
from pathlib import Path

from odbinfo.pure.util import chdir, run_cmd, timed
from odbinfo.pure.writer import localsite


def run_gohugo(site_path: Path) -> None:
    """Run the hugo system command in `site_path` directory"""
    with chdir(site_path):
        run_cmd("hugo", "unable to build hugo site")


def find_free_port() -> int:
    """returns a free port number"""
    # pylint: disable=no-member
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(('', 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return sock.getsockname()[1]


def is_port_open(port):
    """Returns True if `port` is open, otherwise False"""
    # pylint: disable=no-member
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            return True
        return False


def convert_local(site_path: Path) -> None:
    """ Uses wget to rewrite hugo website to locally browsable site"""
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
                while not is_port_open(port):
                    time.sleep(0.1)
                run_cmd("wget  --no-verbose"
                        f" -nH --convert-links -P {localsite_path.name}"
                        " -r --level=100"
                        f" http://localhost:{port}/", check=True)
        finally:
            webserver_proc.kill()


def open_browser(site_dir: Path) -> None:
    """Opens a webbrowser on `site_dir`"""
    if os.getenv("ODBINFO_NO_BROWSE", default="0") == "0":
        site_abs_path = site_dir.resolve() / "index.html"
        webbrowser.open(site_abs_path.as_uri())


@timed("Build and open hugo site", indent=2)
def build(site_path: Path):
    """builds a written site on `site_path`"""
    run_gohugo(site_path)
    convert_local(site_path)
    open_browser(localsite(site_path))
