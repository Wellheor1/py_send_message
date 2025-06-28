.PHONY: create_env
create_env:
	python3 -m venv .venv

.PHONY: setup_poetry
setup_poetry: create_env
	poetry env use .venv/bin/python

.PHONY: poetry_install
poetry_install: setup_poetry
	poetry install

.PHONY: install
install: create_env setup_poetry poetry_install
