.PHONY: all check

all:

check:
	PYRIGHT_PYTHON_FORCE_VERSION=latest pyright src/dmtest/vdo/
	isort -c src/dmtest/vdo/
	ruff check src/dmtest/vdo/
