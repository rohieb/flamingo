FLAMINGO_SETTINGS=settings.py
FLAMINGO_SERVER_ARGS=--host=localhost --port=8080

PYTHON=python3.6
PYTHON_VENV=env

$(PYTHON_VENV)/.created: REQUIREMENTS.txt
	rm -rf $(PYTHON_VENV) && \
	$(PYTHON) -m venv $(PYTHON_VENV) && \
	. $(PYTHON_VENV)/bin/activate && \
	pip install -r ./REQUIREMENTS.txt && \
	date > $(PYTHON_VENV)/.created

env: $(PYTHON_VENV)/.created

clean:
	rm -rf $(PYTHON_VENV)

html: env
	. $(PYTHON_VENV)/bin/activate && \
	flamingo build $(FLAMINGO_ARGS) -s $(FLAMINGO_SETTINGS)

server: env
	. $(PYTHON_VENV)/bin/activate && \
	flamingo server $(FLAMINGO_ARGS) $(FLAMINGO_SERVER_ARGS) -s $(FLAMINGO_SETTINGS)

shell: env
	. $(PYTHON_VENV)/bin/activate && \
	flamingo shell $(FLAMINGO_ARGS) -s $(FLAMINGO_SETTINGS)
