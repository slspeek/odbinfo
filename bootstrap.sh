#!/usr/bin/env bash
set -e
git submodule update --init --recursive
(cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
(cd pipenvconf/pure && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
ODBINFO_NO_BROWSE=1 make travis
ODBINFO_NO_BROWSE=1 make clean coverage
make metric mypy
echo Build successfully