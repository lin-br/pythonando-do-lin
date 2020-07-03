.PHONY: tests clean

PATH_ENVIRONMENT=environment
ACTIVATE_ENVIRONMENT=./$(PATH_ENVIRONMENT)/bin/activate

install: clean
	@echo 'Creating environment'
	python3 -m venv $(PATH_ENVIRONMENT)
	@echo 'Installing dependencies'
	source $(ACTIVATE_ENVIRONMENT) && pip install --upgrade pip && pip install -r requirements.txt
tests: install
	source $(ACTIVATE_ENVIRONMENT) && pytest
clean:
	@echo 'Cleaning directory from project'
	rm -rf $(PATH_ENVIRONMENT)