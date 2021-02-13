libreoffice=/tmp/program
python=$(libreoffice)/python
unopkg=$(libreoffice)/unopkg
antlr4=java -jar ../../../../odbinfo/parser/lib/antlr-4.9.1-complete.jar
target=target
dist=$(target)/dist
stage=$(dist)/odbinfo_oxt/
lib=$(stage)/python/pythonpath
build=$(target)/build
test-output=$(build)/test-output
PYTHONPATH=.:$$(pipenv --venv)/lib/python3.7/site-packages

all: clean genparser info check itest


prepare:
	-mkdir -p $(build) $(test-output)
	cp -r test odbinfo data $(build)

.ONESHELL:
info: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m site
	echo PATH=$$PATH
	hugo version

.ONESHELL:
itest: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -svv -m "not endless" test

.ONESHELL:
alltest: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -svv test

.ONESHELL:
single: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -svv test/${SINGLE}


.ONESHELL:
fixture: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -svv test/fixture_reader.py


.ONESHELL:
unit: prepare
	cd $(build)
	-PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -svv -m "not slow" test
	exit 0

.ONESHELL:
quick_view: clean prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m pytest test/test_quick_view.py


test: itest unit

.ONESHELL:
serve:
	cd $(build)/test/resources/testdb/.odbinfo/testdb
	hugo server --layoutDir ../../../../../../../data/hugo-template/layouts

format:
	autopep8 -ri --exclude="odbinfo/parser/sqlite/*,odbinfo/parser/oobasic/*" odbinfo/ main.py

.ONESHELL:
check: format
	PYTHONPATH=$(PYTHONPATH) $(python) -m pylint odbinfo test

clean:
	-@find . -type d -name __pycache__ -exec rm -rf '{}' \;
	-@rm -rf $(target)
	#-@rm -rf src/test/resources/output_dir/graphs
	@echo $(target) was removed

.ONESHELL:
open_test_db: prepare
	cd $(build)
	$(libreoffice)/soffice test/resources/testdb/testdb.odb

.ONESHELL:
open_shell: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) rlwrap $(python) -i odbinfo/reader.py

.ONESHELL:
oxt:
	-mkdir -p $(lib) $(dist) $(build)
	pipenv lock -r > /tmp/requirements.txt
	python -m pip install -r /tmp/requirements.txt \
	--ignore-installed --target $(lib)
	cp main.py $(stage)/python
	cp -r odbinfo data $(lib)
	cp -r oometadata/* $(stage)
	cp LICENSE $(stage)
	cd $(stage)
	zip -r ../odbinfo.oxt .
	unzip -t ../odbinfo.oxt

install_oxt: oxt
	-$(unopkg) remove "com.github.slspeek.ODBInfo"
	$(unopkg) add -s $(dist)/odbinfo.oxt

doc: prepare
	PYTHONPATH=$(PYTHONPATH) $(python) -m pydoc -p 0

.ONESHELL:
unziptestdb:
	rm -rf test/resources/testdb/unzipped
	cd test/resources/testdb && mkdir unzipped
	cd unzipped && unzip ../testdb.odb

.ONESHELL:
genparser:
	-rm -rf odbinfo/parser/sqlite
	cd  odbinfo/parser/grammars/sqlite/ && \
	$(antlr4) -Dlanguage=Python3 -o ../../sqlite -package odbinfo.parser.sqlite \
		 SQLiteLexer.g4 SQLiteParser.g4
	cd -
	-rm -rf odbinfo/parser/oobasic
	cd odbinfo/parser/grammars/oobasic/ && \
		$(antlr4) -Dlanguage=Python3 -o ../../oobasic -package odbinfo.parser.oobasic \
	 	 OOBasic.g4

.ONESHELL:
installantlr:
	-mkdir -p odbinfo/parser/lib
	cd odbinfo/parser/lib
	curl -O https://www.antlr.org/download/antlr-4.9.1-complete.jar
