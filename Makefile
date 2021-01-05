libreoffice=/tmp/program
python=$(libreoffice)/python
unopkg=$(libreoffice)/unopkg
target=target
dist=$(target)/dist
stage=$(dist)/odbinfo_oxt/
lib=$(stage)/python/pythonpath
build=$(target)/build
test-output=$(build)/test-output
PYTHONPATH=.:$$(pipenv --venv)/lib/python3.7/site-packages

all: clean info check itest


prepare:
	-mkdir -p $(build) $(test-output)
	cp -r test odbinfo data $(build)

.ONESHELL:
info: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m site
	echo PATH=$$(PATH)

.ONESHELL:
itest: prepare
	cd $(build)
	PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -svv test

.ONESHELL:
unit: prepare
	cd $(build)
	-PYTHONPATH=$(PYTHONPATH) $(python) -m pytest -svv -m "not slow" test
	exit 0

test: itest unit

.ONESHELL:
serve:
	cd $(test-output)/table-site
	jekyll server --watch -l

format:
	autopep8 -ri .

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
