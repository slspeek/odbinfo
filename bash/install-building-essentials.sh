#!/usr/bin/env bash
# Not needed on travis build service. Localy you need them to build python 3.7.7 using pyenv.
apt-get update -y && apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
    python3-pip default-jre git unzip zip