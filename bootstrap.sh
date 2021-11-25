#!/usr/bin/env bash
set -e
git submodule update --init --recursive
(cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
(cd pipenvconf/pure && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
(cd pipenvconf/oo && ODBINFO_NO_BROWSE=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../..   travis)
(cd pipenvconf/pure && ODBINFO_NO_BROWSE=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../.. clean coverage)
(cd pipenvconf/pure && ODBINFO_NO_BROWSE=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../.. metric mypy)