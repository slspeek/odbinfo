libreoffice=/tmp/program
python=$(libreoffice)/python
unopkg=$(libreoffice)/unopkg
antlr4=java -jar ../../../../../$(antlrlocation)/antlr-4.9.1-complete.jar
target=target
testloc=odbinfo/test
puretestloc=odbinfo/test/pure
ootestloc=odbinfo/test/oo
dist=$(target)/dist
stage=$(dist)/odbinfo_oxt/
lib=$(stage)/python/pythonpath
build=$(target)/build
test-output=$(build)/test-output
metadata=$(test-output)/metadata.pickle
oo=pipenvconf/oo
pure=pipenvconf/pure
OOPYTHONPATH=.:$$(cd ../../$(oo) 2> /dev/null || cd $(oo) && pipenv --venv)/lib/python3.7/site-packages
PUREPYTHONPATH=.:$$(cd ../../$(pure) 2> /dev/null || cd $(pure) && pipenv --venv)/lib/python3.7/site-packages
parserlocation=odbinfo/pure/parser
antlrlocation=$(parserlocation)/lib

all: clean genparser info check itest

prepare:
	@echo prepare start
	@-mkdir -p $(build) $(test-output)
	@cp -r odbinfo data $(build)
	@echo prepare done

.ONESHELL:
info: prepare
	@cd $(build)
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
	@dot -V
	@echo

.ONESHELL:
coverage: clean prepare
	cd $(build)
	python -m pytest -svv --cov --cov-branch --cov-fail-under=96 --cov-config=../../.coveragerc --cov-report html $(puretestloc)
	test "${ODBINFO_NO_BROWSE}" -ne "0" || x-www-browser htmlcov/index.html

.ONESHELL:
itest: prepare
	cd $(build)
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest -svv $(testloc)

.ONESHELL:
single: prepare
	cd $(build)
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest -svv $(testloc)/${SINGLE}


.ONESHELL:
fixture: prepare
	cd $(build)
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest -svv $(ootestloc)/fixture_writer.py
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest -svv $(puretestloc)/fixture_writer.py
	cd -
	test -f $(metadata)


.ONESHELL:
unit: prepare
	cd $(build)
	-PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest -svv -m "not slow" $(testloc)
	exit 0

.ONESHELL:
quick_view: clean prepare
	cd $(build)
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pytest $(puretestloc)/test_quick_view.py


test: itest unit

.ONESHELL:
serve: prepare
	cd $(build)/$(testloc)/resources/testdb/.$(testloc)db
	hugo server --layoutDir ../../../../../../../../data/hugo-template/layouts

format:
	isort --sg="$(parserlocation)/sqlite/*,$(parserlocation)/oobasic/*" odbinfo/ main.py
	autopep8 -ri --exclude="$(parserlocation)/sqlite/*,$(parserlocation)/oobasic/*" odbinfo/ main.py

.ONESHELL:
check: format
	PYTHONPATH=$(OOPYTHONPATH) $(python) -m pylint odbinfo

clean:
	-@find . -type d -name __pycache__ -exec rm -rf '{}' \;
	-@rm -rf $(target)
	#-@rm -rf src/test/resources/output_dir/graphs
	@echo $(target) was removed

.ONESHELL:
open_test_db: prepare
	cd $(build)
	$(libreoffice)/soffice $(testloc)/resources/testdb/testdb.odb

.ONESHELL:
open_shell: prepare
	cd $(build)
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
	rm -rf $(testloc)/resources/testdb/unzipped
	cd $(testloc)/resources/testdb && mkdir unzipped
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
	curl -O https://www.antlr.org/download/antlr-4.9.1-complete.jar

ctags:
	ctags -R odbinfo

metric: clean
	find -name \*.py -and -not -ipath ./odbinfo/pure/parser/oobasic/\* -and -not -ipath ./odbinfo/pure/parser/sqlite/\* |xargs python -m radon cc -s -nb


