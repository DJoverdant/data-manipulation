VENV ?= .venv
PIP = $(VENV)/bin/pip
PY = $(VENV)/bin/python

.PHONY: init
init: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.yaml

$(VENV):
	python3 -m venv $(VENV)
	touch $@

.PHONY: run
run:
	$(PY) main.py
