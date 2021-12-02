"""Utilities"""
import contextlib
import os
import shlex
import subprocess
import time
from functools import wraps


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


def timed(mesg, indent=0, arg=None, name=True):
    """Timing decorator"""
    def decorate(func):

        def message(args):
            result = indent * " " + mesg
            if not arg is None:
                result += " on "
                if name:
                    result += args[arg].name
                else:
                    result += args[arg]
            return result

        @wraps(func)
        def wrapper(*args, **kwargs):
            if arg is None:
                print(message(args) + ' started ')
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(message(args) + f' finished in {(end_time-start_time):.2f} seconds '
                  )

            return result
        return wrapper
    return decorate


class CommandExecutionError(Exception):
    """Describes a failed command"""

    def __init__(self, cmd, completed_process):
        self.completed_process = completed_process
        super().__init__(
            f"System command: {cmd} failed (returncode={completed_process.returncode})")


def run_cmd(cmd, check=True):
    """ run os `cmd` and raise  if `check` was set"""
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
