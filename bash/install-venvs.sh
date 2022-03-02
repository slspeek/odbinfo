#!/usr/bin/env bash
set -o errexit
(cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
(cd pipenvconf/pure && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
