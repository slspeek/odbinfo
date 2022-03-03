FROM debian:bullseye

ENV DEBIAN_FRONTEND noninteractive

COPY bash/install-building-essentials.sh /install-building-essentials.sh

RUN /install-building-essentials.sh

COPY bash/install-development-runtime.sh /install-development-runtime.sh

RUN /install-development-runtime.sh

RUN useradd -ms /bin/bash build

USER build

ENV LANG en_US.UTF-8

COPY --chown=build:build bash/install-python.sh /home/build/odbinfo-build/bash/install-python.sh

RUN . ~/.profile && cd /home/build/odbinfo-build && bash/install-python.sh

COPY --chown=build:build bash/install-venvs.sh /home/build/odbinfo-build/bash/install-venvs.sh

COPY --chown=build:build pipenvconf /home/build/odbinfo-build/pipenvconf

RUN . ~/.profile && cd /home/build/odbinfo-build && bash/install-venvs.sh

COPY --chown=build:build . /home/build/odbinfo-build

RUN . ~/.profile && cd /home/build/odbinfo-build && bash/build.sh

RUN . ~/.profile && cd /home/build/odbinfo-build && (cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../..   oxt)
