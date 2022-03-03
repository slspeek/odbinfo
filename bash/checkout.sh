#!/usr/bin/env bash
set -e
REPO=$(pwd)
cd $(mktemp -d)
git clone $REPO
cd odbinfo
git submodule update --init --recursive
bash/install-venvs.sh
bash/build.sh
