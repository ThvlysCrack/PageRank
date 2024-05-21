# Variables
PYTHON = python3
PIP = pip
SRC = main.py
REQUIREMENTS = requirement.txt

# Cibles par défaut
.DEFAULT_GOAL := run

setup: $(REQUIREMENTS)
	$(PIP) install -r $(REQUIREMENTS)

run: setup
	$(PYTHON) $(SRC)

clean:
	rm -rf __pycache__

.PHONY: run clean setup
