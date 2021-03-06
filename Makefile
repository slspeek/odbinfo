SHELL=/bin/bash
libreoffice=/tmp/program
python=$(libreoffice)/python
unopkg=$(libreoffice)/unopkg
antlr4jar=antlr-4.9.2-complete.jar
antlr4=java -jar ../../../../../$(antlrlocation)/$(antlr4jar)
target=target
testloc=odbinfo/test
fixtureloc=$(testloc)/oo/data
puretestloc=odbinfo/test/pure
ootestloc=odbinfo/test/oo
dist=$(target)/dist
stage=$(dist)/odbinfo_oxt
lib=$(stage)/python/pythonpath
build=$(target)/build
test-output=$(build)/test-output
metadata=$(test-output)/metadata.pickle
oo=pipenvconf/oo
pure=pipenvconf/pure
OOPYTHONPATH=.:$$(cd $(oo) && pipenv --venv)/lib/python3.7/site-packages
PUREPYTHONPATH=.:$$(cd $(pure) && pipenv --venv)/lib/python3.7/site-packages
parserlocation=odbinfo/pure/parser
antlrlocation=$(parserlocation)/lib
pythonsources=$$(find -name \*.py -and -not -ipath ./target/\* -and -not -ipath ./odbinfo/pure/parser/oobasic/\* -and -not -ipath ./odbinfo/pure/parser/sqlite/\* )
benchmarking=--benchmark-only --benchmark-autosave

build: mypy metric itest

travis: installantlr clean genparser info check alltest

all: travis install_oxt fixtures mypy_report metric

prepare:
	@echo prepare start
	if [ ! -d odbinfo/test/pure/data ]; then (cd odbinfo/test/pure && ln -s ../oo/data) fi
	@-mkdir -p $(build) $(test-output)
	@echo prepare done

.ONESHELL:
info:
	echo --------------------------------------
	echo "|           Build information         |"
	echo --------------------------------------
	echo python -m site
	@PYTHONPATH=$(OOPYTHONPATH) $(python) -m site
	@echo
	@echo PATH=$$PATH
	@echo
	@hugo version
	@echo
	@dot -V|head -1
	@echo

coverage: clean prepare
	ODBINFO_NO_BROWSE=1 python -m pytest ${PYTESTOPTS} --benchmark-disable --cov --cov-branch --cov-fail-under=96 --cov-config=./.coveragerc --cov-report html -m "not veryslow" $(puretestloc)
	test -n "${ODBINFO_NO_BROWSE}" || x-www-browser htmlcov/index.html

itest: clean prepare
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest ${PYTESTOPTS} --benchmark-disable -m "not veryslow" $(testloc)

single: prepare
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest ${PYTESTOPTS} --benchmark-disable $(testloc)/${SINGLE}

metadata_fixture: prepare
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable --force-regen $(ootestloc)/test_reader_regression.py ||$\
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable --force-regen $(ootestloc)/test_reader_regression.py ||$\
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable  $(ootestloc)/test_reader_regression.py
	cp -v odbinfo/test/oo/test_reader_regression/*.pickle odbinfo/test/oo/data

processor_fixture: metadata_fixture
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable --force-regen $(puretestloc)/test_processor_regression.py ||$\
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable --force-regen $(puretestloc)/test_processor_regression.py ||$\
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable --force-regen $(puretestloc)/test_processor_regression.py
	cp -v odbinfo/test/pure/test_processor_regression/*.pickle odbinfo/test/oo/data

writer_fixture: processor_fixture
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable $(puretestloc)/test_writer_regression.py ||$\
	(rm -rf $(fixtureloc)/writer_fixtures/* &&$\
	cp -rv $(test-output)/test_writer_regression/emptydb $(fixtureloc)/writer_fixtures/ &&$\
	cp -rv $(test-output)/test_writer_regression/testdb $(fixtureloc)/writer_fixtures/  &&$\
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest --benchmark-disable $(puretestloc)/test_writer_regression.py )

fixtures: writer_fixture

unit:
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest ${PYTESTOPTS} --benchmark-disable -m "not slow" $(testloc)

benchmark:
	ODBINFO_NO_BROWSE=1 PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest ${PYTESTOPTS} $(benchmarking) $(testloc)

histogram:
	# PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest $ $(testloc) --benchmark-histogram --benchmark-compare=\*
	py.test-benchmark compare --histogram=benchmarks/histogram --group-by=func --sort=name
	py.test-benchmark compare --histogram=benchmarks/histogram

alltest: prepare
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest ${PYTESTOPTS} --benchmark-disable  $(testloc)

.ONESHELL:
serve: clean prepare
	ODBINFO_NO_BROWSE=1 SINGLE=oo/test_core.py::test_generate_report make single
	cd $(test-output)/test_core/testdb
	x-www-browser http://localhost:1313/ &
	hugo server --disableFastRender --layoutDir ../../../../../data/hugo-template/layouts

format:
	isort --sg="$(parserlocation)/sqlite/*,$(parserlocation)/oobasic/*" odbinfo/ main.py
	autopep8 -ri --exclude="$(parserlocation)/sqlite/*,$(parserlocation)/oobasic/*" odbinfo/ main.py

pycompile:
	 python -m py_compile odbinfo/**/**.py odbinfo/test/**/*.py

check: pycompile check_main check_test

check_main: pycompile format
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pylint --ignore="odbinfo/test/pure,odbinfo/test/oo" odbinfo

check_test: pycompile format
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pylint --load-plugins=pylint_pytest odbinfo/test

.PHONY:
clean:
	-@if [ -f wily-report.html ]; then rm wily-report.html; fi
	-@if [ -d htmlcov ]; then rm -rf htmlcov; fi
	-@if [ -f logje ]; then rm logje; fi
	-@find . -type d -name __pycache__ -exec rm -rf '{}' \;
	-@rm -rf $(target)
	#-@rm -rf src/test/resources/output_dir/graphs
	@echo $(target) was removed

open_shell: prepare
	PYTHONPATH=$(OOPYTHONPATH) rlwrap $(python) -i odbinfo/test/pure/fixtures.py

.ONESHELL:
oxt:
	-mkdir -p $(lib) $(dist) $(build)
	(cd pipenvconf/oo && pipenv lock -r > /tmp/requirements.txt)
	python -m pip install -r /tmp/requirements.txt \
	--ignore-installed --target $(lib)
	cp main.py $(stage)/python
	cp -r odbinfo data $(lib)
	rm -rf $(lib)/odbinfo/test
	cp -r oometadata/* $(stage)
	cp LICENSE $(stage)
	cd $(stage)
	zip -r ../odbinfo.oxt .
	unzip -t ../odbinfo.oxt

install_oxt: oxt
	-$(unopkg) remove "com.github.slspeek.ODBInfo"
	$(unopkg) add -s $(dist)/odbinfo.oxt

doc: prepare
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pydoc -p 0

.ONESHELL:
unziptestdb:
	-rm -rf $(ootestloc)/data/databases/unzipped
	cd $(ootestloc)/data/databases && mkdir unzipped
	cd unzipped && unzip ../testdb.odb

.ONESHELL:
genparser:
	-rm -rf $(parserlocation)/sqlite
	cd  $(parserlocation)/grammars/sqlite/ && \
	$(antlr4) -Dlanguage=Python3 -o ../../sqlite -package odbinfo.parser.sqlite \
		 SQLiteLexer.g4 SQLiteParser.g4
	cd -
	-rm -rf $(parserlocation)/oobasic
	cd $(parserlocation)/grammars/oobasic/ && \
		$(antlr4) -Dlanguage=Python3 -o ../../oobasic -package odbinfo.parser.oobasic \
	 	 OOBasic.g4

.ONESHELL:
installantlr:
	-mkdir -p $(antlrlocation)
	cd $(antlrlocation)
	curl -O https://www.antlr.org/download/$(antlr4jar)

ctags:
	ctags -R odbinfo

metric: clean
	python -m xenon -b A -m A -a A  $(pythonsources)

mypy_report:
	mypy --show-error-codes --disable-error-code  import --html-report mypy-report $(pythonsources)


mypy:
		mypy --show-error-codes --disable-error-code  import $(pythonsources)

