#!/usr/bin/env bash
cd ~ && git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    cd ~/.pyenv && src/configure && make -C src

~/.pyenv/bin/pyenv install 3.7.7