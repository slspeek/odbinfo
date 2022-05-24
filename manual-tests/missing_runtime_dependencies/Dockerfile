FROM debian:bullseye

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get install -y libreoffice

RUN apt-get install -y firefox-esr

RUN useradd -ms /bin/bash manual

COPY --chown=manual:manual ./target/dist/odbinfo.oxt /home/manual

COPY --chown=manual:manual ./tests/oo/data/databases/testdb.odb /home/manual

USER manual

RUN echo "soffice ~/testdb.odb" > /home/manual/.bash_history

RUN . ~/.profile && cd /home/manual && unopkg add --suppress-license odbinfo.oxt
