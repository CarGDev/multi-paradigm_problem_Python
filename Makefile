PYTHON := .venv/bin/python

.PHONY: run

run:
ifndef CSV
	$(error Usage: make run CSV=path/to/file.csv)
endif
	$(PYTHON) src/main.py $(CSV)
