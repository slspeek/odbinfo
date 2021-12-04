SHELL=/bin/bash
libreoffice=/tmp/program
python=$(libreoffice)/python
unopkg=$(libreoffice)/unopkg
antlr4version=4.9.3
antlr4jar=antlr-$(antlr4version)-complete.jar
antlr4=java -jar ../../../../../../$(antlrlocation)/$(antlr4jar)
target=target
testloc=tests
srcloc=src
fixtureloc=$(testloc)/oo/data
puretestloc=$(testloc)/pure
ootestloc=$(testloc)/oo
dist=$(target)/dist
stage=$(dist)/odbinfo_oxt
lib=$(stage)/python/pythonpath
build=$(target)/build
test-output=$(build)/test-output
report=$(build)/report
classdiagram=$(report)/classdiagram
oo=pipenvconf/oo
pure=pipenvconf/pure
SOURCE_ROOTS=$(srcloc):$(testloc)
OOPYTHONPATH=$(SOURCE_ROOTS):$$(cd $(oo) && pipenv --venv)/lib/python3.7/site-packages
PUREPYTHONPATH=$(SOURCE_ROOTS):$$(cd $(pure) && pipenv --venv)/lib/python3.7/site-packages
parserlocation=$(srcloc)/odbinfo/pure/parser
antlrlocation=$(parserlocation)/lib
pythonsources=$$(find $(srcloc) $(testloc) -name \*.py -and $\
-not -ipath $(testloc)/pure/test_writer_templates/\* -and $\
-not -ipath $(testloc)/oo/test_core/\* -and $\
-not -ipath $(testloc)/pure/test_template_regression/\* -and $\
-not -ipath $(testloc)/pure/test_convert_local_regression/\* -and $\
-not -ipath $(testloc)/pure/data\* -and $\
-not -ipath $(testloc)/oo/data\* -and $\
-not -ipath ./target/\* -and $\
-not -ipath $(srcloc)/odbinfo/pure/parser/oobasic/\* -and $\
-not -ipath $(srcloc)/odbinfo/pure/parser/sqlite/\* )
benchmarking=--benchmark-only --benchmark-autosave --benchmark-enable
unit=-m "not slow and not veryslow and not tooslow"
itests=-m "slow"
OOPYTHON=PYTHONPATH=$(OOPYTHONPATH) $(python)
OOPYTEST=$(OOPYTHON) -m pytest ${PYTESTOPTS} --benchmark-disable
PUREPYTEST=$(PUREPYTHON) -m pytest ${PYTESTOPTS} --benchmark-disable
PUREPYTHON=PYTHONPATH=$(PUREPYTHONPATH) python

build: mypy metric unitcoverage

travis: installantlr post_checkout precommit

precommit:  clean genparser info check alltest

all: ctags mypy metric precommit install_oxt

prepare:
	@echo prepare start
	@-mkdir -p $(build) $(test-output) $(classdiagram)
	@echo prepare done

.ONESHELL:
info:
	@echo --------------------------------------
	@echo "|           Build information         |"
	@echo --------------------------------------
	@echo python -m site
	@$(OOPYTHON) -m site
	@echo
	@echo PATH=$$PATH
	@echo
	@hugo version
	@echo
	@dot -V|head -1
	@echo

classdiagram: prepare
	PYTHONPATH=$(OOPYTHONPATH) pyreverse -d $(classdiagram) -o svg odbinfo
	test -n "${ODBINFO_NO_BROWSE}" || x-www-browser $(classdiagram)/classes.svg $(classdiagram)/packages.svg

coverage: clean prepare
	ODBINFO_NO_BROWSE=1 $(PUREPYTEST)  --cov --cov-branch --cov-fail-under=96 --cov-config=./.coveragerc --cov-report html -m "not veryslow and not tooslow" $(puretestloc)
	test -n "${ODBINFO_NO_BROWSE}" || x-www-browser htmlcov/index.html

unitcoverage:
	$(PUREPYTHON) -m pytest ${PYTESTOPTS} --benchmark-disable --cov --cov-branch --cov-fail-under=90 --cov-config=./.coveragerc --cov-report html:unitcov $(unit) $(puretestloc)
	test -n "${ODBINFO_NO_BROWSE}" || x-www-browser unitcov/index.html

itest: clean prepare
	$(OOPYTEST) $(itests) $(testloc)

single: prepare
	$(OOPYTEST) $(testloc)/${SINGLE}

run: clean prepare
	$(OOPYTEST) $(testloc)/oo/test_core.py::test_generate_report

metadata_fixture: prepare
	$(OOPYTEST) --force-regen $(ootestloc)/test_reader_regression.py ||$\
	$(OOPYTEST) --force-regen $(ootestloc)/test_reader_regression.py ||$\
	$(OOPYTEST) $(ootestloc)/test_reader_regression.py
	cp -v $(ootestloc)/test_reader_regression/*.pickle $(fixtureloc)

processor_fixture: metadata_fixture
	$(OOPYTEST) --force-regen $(puretestloc)/test_processor_regression.py ||$\
	$(OOPYTEST) --force-regen $(puretestloc)/test_processor_regression.py ||$\
	$(OOPYTEST) --force-regen $(puretestloc)/test_processor_regression.py
	cp -v $(puretestloc)/test_processor_regression/*.pickle $(fixtureloc)


write_site_fixture: processor_fixture
	$(OOPYTEST)  --force-regen $(puretestloc)/test_write_site_regression.py || $\
	($(OOPYTEST)  --force-regen $(puretestloc)/test_write_site_regression.py && $\
	(rm -rf $(fixtureloc)/fixtures/template_regression_input || true) && $\
	cp -r $(puretestloc)/test_write_site_regression $(fixtureloc)/fixtures/template_regression_input)


template_fixture: write_site_fixture
	$(OOPYTEST)  --force-regen $(puretestloc)/test_template_regression.py || $\
	($(OOPYTEST)  --force-regen $(puretestloc)/test_template_regression.py && $\
	(rm -rf $(fixtureloc)/fixtures/convert_local_input || true) && $\
	cp -r $(puretestloc)/test_template_regression/test_template_regression $(fixtureloc)/fixtures/convert_local_input)

convert_local_fixture: template_fixture
	$(OOPYTEST)  --force-regen $(puretestloc)/test_convert_local_regression.py || $\
	$(OOPYTEST)  --force-regen $(puretestloc)/test_convert_local_regression.py

fixtures: clean convert_local_fixture
	$(OOPYTEST) --force-regen -m "not tooslow" $(testloc)

unit:
	$(OOPYTEST) $(unit) $(testloc)

benchmark:
	ODBINFO_NO_BROWSE=1 $(OOPYTEST) $(benchmarking) $(testloc)

histogram:
	# PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest $ $(testloc) --benchmark-histogram --benchmark-compare=\*
	py.test-benchmark compare --histogram=benchmarks/histogram --group-by=func --sort=name
	py.test-benchmark compare --histogram=benchmarks/histogram

alltest: clean
	$(OOPYTEST) $(testloc)

.ONESHELL:
serve: run
	cd $(test-output)/test_core/testdb
	x-www-browser http://localhost:1313/ &
	hugo server --disableFastRender --layoutDir ../../../../../data/hugo-template/layouts

.ONESHELL:
qserve:
	cd $(test-output)/test_core/testdb
	hugo server --disableFastRender --layoutDir ../../../../../data/hugo-template/layouts

format:
	$(PUREPYTHON) -m isort --sg="$(parserlocation)/sqlite/*,$(parserlocation)/oobasic/*" $(srcloc) $(testloc)
	$(PUREPYTHON) -m autopep8 -ri --exclude="$(parserlocation)/sqlite/*,$(parserlocation)/oobasic/*" $(srcloc) $(testloc)

pycompile: # Compiles the sources
	$(OOPYTHON) -m py_compile $(srcloc)/**/**.py $(testloc)/**/*.py

check: pycompile check_main check_test

check_main: pycompile format
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pylint --ignore="$(parserlocation)/oobasic,$(parserlocation)/sqlite" $(srcloc)

check_test: pycompile format
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pylint --load-plugins=pylint_pytest -dC0116,C0115,R0201,W0201 $(testloc)

.PHONY:
clean:
	-@if [ -f wily-report.html ]; then rm wily-report.html; fi
	-@if [ -d htmlcov ]; then rm -rf htmlcov; fi
	-@if [ -f logje ]; then rm logje; fi
	-@find . -type d -name __pycache__ -exec rm -rf '{}' \;
	-@rm -rf $(target)
	@echo $(target) was removed

open_shell: prepare
	PYTHONPATH=$(OOPYTHONPATH) rlwrap $(python) -i $(puretestloc)/conftest.py

.ONESHELL:
oxt:
	-mkdir -p $(lib) $(dist) $(build)
	(cd pipenvconf/oo && pipenv lock -r > /tmp/requirements.txt)
	$(PUREPYTHON) -m pip install -r /tmp/requirements.txt \
	--ignore-installed --target $(lib)
	cp $(srcloc)/main.py $(stage)/python
	cp -r $(srcloc)/*  $(lib)
	rm $(lib)/main.py
	cp -r oometadata/* $(stage)
	cp LICENSE $(stage)
	cd $(stage)
	zip -r ../odbinfo.oxt .
	unzip -t ../odbinfo.oxt

install_oxt: oxt
	-$(unopkg) remove "com.github.slspeek.ODBInfo"
	$(unopkg) add -s $(dist)/odbinfo.oxt

doc: prepare
	$(OOPYTHON) -m pydoc -p 0

.ONESHELL:
unziptestdb:
	-rm -rf $(ootestloc)/data/databases/unzipped
	cd $(ootestloc)/data/databases && mkdir unzipped && mkdir unzipped_doc
	cd unzipped && unzip ../testdb.odb
	cd ../unzipped_doc && unzip ../Untitled.odt

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
	$(PUREPYTHON) -m xenon -b A -m A -a A  $(pythonsources)

mypy_report:
	$(PUREPYTHON) -m mypy --show-error-codes --disable-error-code  import --html-report mypy-report $(pythonsources)

mypy:
	$(PUREPYTHON) -m mypy --show-error-codes --disable-error-code  import $(pythonsources)

post_checkout:
	-mkdir $(fixtureloc)/fixtures/template_regression_input/test_write_site_empty/content
	-mkdir $(puretestloc)/test_writemetadata_regression/test_writemetadata_empty/content
	-mkdir $(puretestloc)/test_write_site_regression/test_write_site_empty/content
	-mkdir -p $(puretestloc)/test_template_regression/test_template_regression_empty/resources/_gen/{assets,images}
	-mkdir -p $(puretestloc)/test_template_regression/test_template_regression/resources/_gen/{assets,images}
	-mkdir $(puretestloc)/test_template_regression/test_template_regression_empty/content



