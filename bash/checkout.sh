#!/usr/bin/env bash
set -e
REPO=$(pwd)
TEMPDIR=$(mktemp -d)
cd $TEMPDIR
git clone $REPO
cd odbinfo
git submodule update --init --recursive
bash/install-venvs.sh
bash/build.sh
(cd pipenvconf/oo && pipenv --rm)
(cd pipenvconf/pure && pipenv --rm)
cd $REPO
rm -rf $TEMPDIR
