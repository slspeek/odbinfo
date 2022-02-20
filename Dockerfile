FROM debian:bullseye

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
    python3-pip default-jre git unzip zip

COPY ci /ci

RUN bash /ci/linux.bash

RUN useradd -ms /bin/bash build

USER build

RUN cd ~ && git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    cd ~/.pyenv && src/configure && make -C src

RUN ~/.pyenv/bin/pyenv install 3.7.7

RUN pip install pipenv

COPY --chown=build:build . /home/build/odbinfo-build

RUN . ~/.profile && cd /home/build/odbinfo-build && bash bootstrap.sh

RUN . ~/.profile && cd /home/build/odbinfo-build && (cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../..   oxt)
