.PHONY: tests clean

PATH_ENVIRONMENT = venv
ACTIVATE_ENVIRONMENT=./$(PATH_ENVIRONMENT)/bin/activate

install: clean
	python3 -m venv $(PATH_ENVIRONMENT)
	source $(ACTIVATE_ENVIRONMENT) && pip install --upgrade pip && pip install -r requirements.txt
tests: install
	source $(ACTIVATE_ENVIRONMENT) && pytest
clean:
	rm -rf $(PATH_ENVIRONMENT)