FROM debian:bullseye

ENV DEBIAN_FRONTEND noninteractive

COPY install-building-essentials.sh /install-building-essentials.sh

RUN /install-building-essentials.sh

COPY ci /ci

RUN bash /ci/linux.bash

RUN useradd -ms /bin/bash build

USER build

ENV LANG en_US.UTF-8

COPY install-python.sh /home/build/odbinfo-build/install-python.sh

RUN . ~/.profile && cd /home/build/odbinfo-build && ./install-python.sh

RUN pip install pipenv

COPY --chown=build:build . /home/build/odbinfo-build

RUN . ~/.profile && cd /home/build/odbinfo-build && ./bootstrap.sh && ./build.sh

RUN . ~/.profile && cd /home/build/odbinfo-build && (cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../..   oxt)
