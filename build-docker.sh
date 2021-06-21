source ~/virtualenv/python3.7/bin/activate
git clone --depth=50 --branch=main https://github.com/slspeek/odbinfo.git slspeek/odbinfo
cd slspeek/odbinfo
git submodule update --init --recursive
sudo apt-get -y install graphviz
sudo bash ci/linux.bash
pip install pipenv
(cd pipenvconf/oo && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
(cd pipenvconf/pure && PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -d)
(cd pipenvconf/oo && ODBINFO_NO_BROWSE=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../..   travis)
(cd pipenvconf/pure && ODBINFO_NO_BROWSE=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../.. clean coverage)
(cd pipenvconf/pure && ODBINFO_NO_BROWSE=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run make -C ../.. metric mypy)