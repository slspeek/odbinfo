""" tests for ooutil """

from odbinfo.oo import ooutil


def test_path_from_url():
    assert ooutil.path_from_url(
        "file:///home/odbinfo/filename") == "/home/odbinfo/filename"


def test_path_from_url_space():
    assert ooutil.path_from_url("file:///home/odbinfo/filename%20with%20spaces"
                                ) == "/home/odbinfo/filename with spaces"
