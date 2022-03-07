"""Utilities"""
import contextlib
import logging
import os
import shlex
import subprocess
import time
from functools import wraps
from typing import Optional


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


def timed(mesg: str,
          indent: int = 0,
          arg: Optional[int] = None,
          name: bool = True):
    """Timing decorator
    if `arg` is not None, a single line afterwards is logged with the argument pointed
    out by `arg`. That is "{msg} on {args[arg]} finished in {seconds}.".
    If arg is None no argument is logged. Before the call "Starting {msg}" and
    after "Finished {msg} in {seconds}" is logged.

    `indent` specifies the number of spaces to prepend to the message
    `arg` if not None, is used as index the args list to pick the argument to log
    `name` if set to True it logs the name attribute of the arg to log
        else it logs str(args[arg]) (only used when arg is set)
    """

    def decorate(func):

        def message(args):
            result = indent * " " + mesg
            if arg is not None:
                result += " on "
                if name:
                    result += args[arg].name
                else:
                    result += str(args[arg])
            return result

        @wraps(func)
        def wrapper(*args, **kwargs):
            if arg is None:
                # pylint:disable=logging-not-lazy
                logging.info(message(args) + ' started ')
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            # pylint:disable=logging-not-lazy
            logging.info(
                message(args) +
                f' finished in {(end_time - start_time):.2f} seconds ')

            return result

        return wrapper

    return decorate


def run_cmd(cmd, check=True):
    """ run os `cmd`.
    If command succeeds nothing is logged nor printed to stdout nor to stderr.
    If however the command fails a warning is
    logged with the captured stdout and stderr of the command.
    If the command fails and `check` is True an exception is raised.
    """
    try:
        subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as error:
        logging.warning("System command: %s failed (returncode=%s)", cmd,
                        error.returncode)
        logging.warning("Output: %s", error.output.decode("utf-8"))
        if check:
            raise error
