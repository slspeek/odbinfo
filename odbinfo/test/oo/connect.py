""" LibreOffice starter and connecter test utilities """
import logging
import os
import shlex
import subprocess
import time

import uno
from pytest import fixture

from odbinfo.test.resource import DEFAULT_TESTDB, EMPTYDB

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)

# time out in seconds
OFFICE_TIME_OUT = 20
SOFFICE_CMD = '/tmp/program/soffice '\
              '--accept="socket,host=localhost,port=2002;urp;" '\
              '--norestore --nologo --nodefault  --headless'\
              ' {}'


@fixture(scope="function")
def libreoffice():
    """ A libreoffice running on a test database """
    testdb = os.getenv("ODBINFO_TESTDB", DEFAULT_TESTDB)
    office_proc = start_office(testdb)
    yield office_proc
    office_proc.terminate()
    logger.debug("LibreOffice killed")


@fixture(scope="function")
def empty_libreoffice():
    """ A libreoffice running on a empty database """
    office_proc = start_office(EMPTYDB)
    yield office_proc
    office_proc.terminate()
    logger.debug("LibreOffice killed")


def start_office(file):
    """ Start LibreOffice on `file`. Returns the process """
    args = shlex.split(SOFFICE_CMD.format(file))
    # pylint:disable=consider-using-with
    office_proc = subprocess.Popen(args, shell=False)
    logger.debug("LibreOffice started with %s ", file)
    return office_proc


def get_context():
    """ Retrieves a remote context """
    local_context = uno.getComponentContext()

    # create the UnoUrlResolver
    resolver = local_context.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_context
    )

    i = 0
    while i < OFFICE_TIME_OUT * 10:
        try:
            # connect to the running office
            ctx = resolver.resolve(
                "uno:socket,host=localhost,port=2002;"
                "urp;StarOffice.ComponentContext"
            )
            break
        except Exception:  # pylint: disable=broad-except
            i += 1
            logger.debug(
                "waiting on uno connection for %0.1f seconds", float(i)/10)
            time.sleep(0.1)
    else:
        raise Exception("Gave up waiting for libreoffice after {} seconds"
                        .format(OFFICE_TIME_OUT))
    return ctx


def smgr():
    """ Returns a ServiceManager """
    return get_context().ServiceManager


def desktop():
    """ Returns a Desktop """
    return smgr().createInstance("com.sun.star.frame.Desktop")


def datasource():
    """ Returns the datasource from the active window """
    return desktop().CurrentComponent.CurrentController.DataSource


def oodocument():
    """ Returns the document from the active window """
    return desktop().CurrentComponent
