# Development
It is convienent for development to be on a debian-linux system.

There are two ways to run the tests:
1. Using docker.io, easy but slow.
2. Setting up a local python environment.

But first clone the source from github, navigate into it and
retrieve the submodules:
```bash
git clone https://github.com/slspeek/odbinfo.git
cd odbinfo
git submodule update --init --recursive
```

## Docker build
Install the docker.io package, if you have not already:

```bash
 sudo apt install docker.io
 ```
And add the current unix user to the docker group and
login again.
```bash
 sudo addduser $(whoami) docker
 ```

 Run docker build
(on my box, which not slow, this runs for a small hour when run for the first time).

```bash

docker build .  -t odbinfo-img
```
This produces an image with ```odbinfo.oxt``` on it. 

Run
```bash
docker run odbinfo-img cat /home/build/odbinfo-build/target/dist/odbinfo.oxt > odbinfo.oxt
```
to get it in the current directory.

## Local build
This is the best way if you want to work on this project. 

### Initial setup
Install the building essentials
```bash
sudo bash/install-building-essentials.sh
```
Install the development runtime dependencies
```bash
sudo bash/install-development-runtime.sh
```

Install python 3.7.7 using pyenv
```bash
bash/install-python.sh
```

Create the python environments with pipenv
```bash
bash/install-venvs.sh
```

### Regular build
Get into the pipenv virtual environment
```bash
ln -sf /tmp/program /opt/libreoffice7.0/program
cd pipenv/pure 
pipenv shell -- 'cd ../.. && source bash/env.source'
```
And run a make command like:
```bash
make oxt
```
to produce a installable oxt file for LibreOffice.

Or run
```bash
make travis
```
to run all checks and tests.

You can see a classes and packages diagram with:
```bash
make classdiagram
```


