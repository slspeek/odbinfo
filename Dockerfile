FROM debian:bullseye

ENV DEBIAN_FRONTEND noninteractive
RUN apt update -y && apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
    graphviz python3-pip

COPY ci /ci

RUN bash /ci/linux.bash

RUN apt install -y default-jre

RUN apt install -y git

RUN useradd -ms /bin/bash build

USER build