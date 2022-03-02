#!/usr/bin/env bash
set -o errexit
source bash/env.source
(cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../..   travis)
(cd pipenvconf/pure &&  ODBINFO_NO_BROWSE=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../.. clean coverage)
(cd pipenvconf/pure &&  PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../.. metric mypy)
