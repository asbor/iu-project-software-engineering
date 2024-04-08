install:
	echo "[Info] - Creating virtualenv"; \
	python3 -m venv .venv; \
	echo "[Info] - Activating virtualenv"; \
	. .venv/bin/activate; \
	echo "[Info] - Installing requirements"; \
	pip3 install -r requirements.txt; \
	echo "Done"; \

uninstall:
	echo "[Info] - Removing virtualenv"; \
	rm -rf .venv; \
	echo "Done"; \

reinstall:
	echo "[Info] - Reinstalling project"; \
	make uninstall; \
	make install; \
	echo "Done"; \

upgrade:
	echo "[Info] - Upgrading project"; \
	pip3 install -r requirements.txt --upgrade; \
	echo "Done"; \

freeze:
	echo "[Info] - Backing up requirements"; \
	mkdir -p .backups; \
	cp requirements.txt .backups/requirements.txt; \
	echo "[Info] - Freezing project"; \
	pip3 freeze > requirements.txt; \
	echo "Done"; \

test:
	echo "[Info] - Running tests"; \
	python3 -m unittest discover -s tests -p 'test_*.py'; \

clean:
	echo "[Info] - This command removes the virtual environment folder, the database file, and the log file. if they exist"; \
	if [ -d "venv" ]; then rm -rf .venv; fi; \
	if [ -f "app/data/Python_SQLite.db" ]; then rm app/data/Python_SQLite.db; fi; \
	if [ -f "app.log" ]; then rm app.log; fi; \
	if [ -d "htmlcov" ]; then rm -rf htmlcov; fi; \
	echo "Done"; \
	
run:
	@echo "[Info] - Running project"
	@python3 app/main.py

coverage:
	@echo "[Info] - Running coverage"
	@python3 -m unittest discover -s tests -p 'test_*.py' -v
	@coverage run -m unittest discover -s tests -p 'test_*.py'
	@coverage html --include app/* --omit tests/*
	@echo "Done"

DIRECTORY=documents/docs
BUILDDIR=$(DIRECTORY)/build
FILENAME=$(DIRECTORY)/HoppyBrew.rmd
BIBFILENAME=documents/bibliography.bib
MARKDOWNDIR=$(DIRECTORY)/chapters_markdown



pdf:
	python tools/MarkdownToPdf.py

git:
	git add .
	git commit -m "Update"
	git push

doc: 
	@make pdf
	@make git


all: 
	@echo "[Clean] - Cleaning project"
	@make clean
	@echo "[Install] - Installing project"
	@make install
	@echo "[Test] - Running tests"
	@make test
	@echo "[Coverage] - Running coverage"
	@make coverage
	@echo "[Doc] - Generating documentation"
	@make doc
	@echo "Done"

help:
	@echo "install - install project"
	@echo "test - run tests"
	@echo "clean - clean project"
	@echo "run - run project"
	@echo "coverage - run coverage"
	@echo "doc - generate documentation"
	@echo "all - run all commands"
	@echo "help - show this message and exit"

requirements:
	@echo "[Info] - Installing requirements"
	@pip3 install -r requirements.txt
	@echo "Done"