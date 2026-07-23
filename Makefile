.PHONY: all check

all:

check:
	PYRIGHT_PYTHON_FORCE_VERSION=latest pyright src/dmtest/vdo/
