libreoffice=/tmp/program
python=$(libreoffice)/python
unopkg=$(libreoffice)/unopkg
target=target
dist=$(target)/dist
stage=$(dist)/odbinfo_oxt/
lib=$(stage)/python/pythonpath
build=$(target)/build
test-output=$(build)/test-output
PYTHONPATH=.:$$(pipenv --venv)/lib/python3.7/site-packages:/home/travis/virtualenv/python3.7.1/lib/python3.7/site-packages/

all: clean info check itest unit oxt install_oxt e2etest


prepare:
	-mkdir -p $(build) $(test-output)
	cp -rv test odbinfo data $(build)

.ONESHELL:
info: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m site

.ONESHELL:
itest: prepare
	cd $(build)
	# PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -v test

.ONESHELL:
unit: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -v test

test: itest unit

.ONESHELL:
serve:
	cd $(test-output)/table-site
	jekyll server --watch -l

format:
	autopep8 -ri .

.ONESHELL:
check: format
	PYTHONPATH=$(PYTHONPATH) $(python) -m pylint .

clean:
	-@find . -type d -name __pycache__ -exec rm -rf '{}' \;
	-@rm -rf $(target)
	#-@rm -rf src/test/resources/output_dir/graphs
	@echo $(target) was removed

.ONESHELL:
oxt:
	-mkdir -p $(lib) $(dist) $(build)
	python -m pip install graphviz \
	--ignore-installed --target $(lib)
	cp src/main/python/main.py $(stage)/python
	cp -r src/main/python/bd_to_dot $(lib)
	cp -r src/main/basic/bd_to_dot_ui $(stage)
	cp -r src/main/resources/oometadata/* $(stage)
	cp LICENSE $(stage)
	cd $(stage)
	zip -r ../bd2dot.oxt .
	unzip -t ../bd2dot.oxt

install_oxt:
	-$(unopkg) remove "com.github.slspeek.BaseDocumenter2Dot"
	$(unopkg) add -s $(dist)/bd2dot.oxt

.ONESHELL:
open_test_db: prepare
	cd $(build)
	$(libreoffice)/soffice test/resources/testdb/testdb.odb

.ONESHELL:
open_shell: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) rlwrap $(python) -i odbinfo/reader.py
