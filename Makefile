.PHONY: create_env
create_env:
	python3 -m venv .venv2

.PHONY: activate_env
activate_env:
	source .venv2/bin/activate

.PHONY: poetry_install
poetry_install:
	poetry install

install: create_env activate_env poetry_install
