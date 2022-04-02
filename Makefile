PATH_REPO?=$(shell pwd)
PATH_VIRTUALENV?=$(PATH_REPO)/env
PORT?=8888

PKG_NAME:=src

help:
	@echo "Make targets:"
	@echo "  build            install dependencies and prepare environment"
	@echo "  clean            remove *.pyc files and __pycache__ directory"
	@echo "  distclean        remove virtual environment"
	@echo "  run              run jupyter lab (default port $(PORT))"
	@echo "  format           format python code (black and isort)"
	@echo "  activate-vim     activate vim key bindings for jupyter"
	@echo "  deactivate-vim   deactivate vim key bindings for jupyter"
	@echo "Check the Makefile for details"

build:
	virtualenv $(PATH_VIRTUALENV); \
	source $(PATH_VIRTUALENV)/bin/activate; \
	pip install --upgrade pip; \
	pip install -U -r requirements.txt; \
	pip install -e .; \
	jupyter serverextension enable --py jupyterlab_code_formatter

activate-vim:
	source $(PATH_VIRTUALENV)/bin/activate; \
	pip uninstall --yes jupyterlab-vim; \
	pip install --no-input jupyterlab-vim

deactivate-vim:
	source $(PATH_VIRTUALENV)/bin/activate; \
	pip uninstall --yes jupyterlab-vim;

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name '*.egg-info' -type d | xargs rm -fr
	find . -name '.ipynb_checkpoints' -type d | xargs rm -fr

distclean: clean
	rm -rf $(VIRTUALENV)

format:
	source $(PATH_VIRTUALENV)/bin/activate; \
	python -m black $(PKG_NAME); \
	python -m isort $(PKG_NAME)

run:
	source $(PATH_VIRTUALENV)/bin/activate; \
	jupyter lab --no-browser --port=$(PORT)

