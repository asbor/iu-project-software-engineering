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

DIRECTORY=documents/01-Conception-Phase
BUILDDIR=$(DIRECTORY)/build
FILENAME=$(DIRECTORY)/HoppyBrew.rmd
BIBFILENAME=documents/bibliography.bib
MARKDOWNDIR=$(DIRECTORY)/chapters_markdown

md:
	mkdir -p $(MARKDOWNDIR)
	# Use shell loop to iterate over all *.Rmd files in the directory
	for file in $(DIRECTORY)/chapters/*.Rmd; do \
		pandoc $$file \
		--filter pandoc-citeproc \
		--from=markdown+tex_math_single_backslash+tex_math_dollars \
		--to=gfm \
		--output=$(MARKDOWNDIR)/$$(basename $$file .Rmd).md \
		--bibliography=$(BIBFILENAME) \
		--atx-headers \
		--wrap=none \
		--preserve-tabs \
		--reference-links; \
	done

pdf:
	mkdir -p $(BUILDDIR)
	pandoc $(FILENAME) \
	--filter pandoc-citeproc \
	--from=markdown+tex_math_single_backslash+tex_math_dollars+raw_tex \
	--to=latex \
	--output=$(BUILDDIR)/$(notdir $(basename $(FILENAME))).pdf \
	--pdf-engine=pdflatex \
	--bibliography=$(BIBFILENAME)

pdf2:
	mkdir -p $(BUILDDIR)
	Rscript -e "rmarkdown::render('$(FILENAME)', output_dir = '$(BUILDDIR)', output_format = 'pdf_document', output_file = '$(BUILDDIR)/$(notdir $(basename $(FILENAME))).pdf', params = list(bibfile = '$(BIBFILENAME)'), envir = new.env())"

HTML_OUTPUT_OPTIONS = "highlight=tango lightbox=true self_contained=true theme=readable code_folding=show toc_float=true"

html_downcute:
	mkdir -p $(BUILDDIR)
	Rscript -e "rmarkdown::render('documents/$(FILENAME)', output_dir = '$(BUILDDIR)', output_format = 'rmdformats::downcute', output_file = '$(FILENAME).html', params = list(bibfile = '$(BIBFILENAME)), output_options = c($(subst ",\",$(HTML_OUTPUT_OPTIONS))), envir = new.env())"


html:
	mkdir -p $(BUILDDIR)
	pandoc documents/$(FILENAME) \
	--filter pandoc-citeproc \
	--from=markdown+tex_math_single_backslash+tex_math_dollars \
	--to=html5 \
	--output=$(BUILDDIR)/$(FILENAME).html \
	--mathjax \
	--self-contained \
	--bibliography=$(BIBFILENAME)

git:
	git add .
	git commit -m "Update"
	git push

git2:
	@make md 
	git add .
	git commit -m "Update"
	git push

doc: 
	@make md 
	@make pdf2
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