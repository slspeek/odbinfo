#!/usr/bin/env bash
set -e
git submodule update --init --recursive
./install-venvs.sh
./build.sh
echo Build successfully