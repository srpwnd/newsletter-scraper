# Define the virtual environment directory and python version
VENV_DIR=venv
PYTHON=python

# Default command to run the scraper script
run: venv
	@$(VENV_DIR)/bin/$(PYTHON) scraping_pipeline.py

# Create the virtual environment
venv:
	@$(PYTHON) -m venv $(VENV_DIR)
	@$(VENV_DIR)/bin/pip install --upgrade pip
	@$(VENV_DIR)/bin/pip install -r requirements.txt

# Install dependencies from the requirements.txt file
install: venv
	@$(VENV_DIR)/bin/pip install -r requirements.txt

# Freeze current dependencies to requirements.txt
freeze:
	@$(VENV_DIR)/bin/pip freeze > requirements.txt

# Run tests (assuming you have a tests directory with test files)
test:
	@$(VENV_DIR)/bin/python -m unittest discover -s tests

lint:
	@$(VENV_DIR)/bin/python -m ruff check --fix

format:
	@$(VENV_DIR)/bin/python -m ruff format

# Clean up generated files
clean:
	rm -rf __pycache__ *.pyc $(VENV_DIR) *.csv *.parquet _storage _storage_docker

clean-data:
	rm -rf _storage _storage_docker

# Remove virtual environment
clean-venv:
	rm -rf $(VENV_DIR)
