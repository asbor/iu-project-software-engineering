# Week 2

<details>

<summary><strong>Tuesday, 19th of March 2024</strong></summary>

***

### What did I do today?

* Built the overall documentation structure.
* Created placeholders for the chapters in the Conception Phase.
* Created `makefile` to build the documentation as `pdf` and `markdown` files.
* Created the first development journal entry.

### Which challenges did I encounter?

1. My previous `makefile` failed to function as intended, necessitating a complete rewrite from the ground up. Additionally, the conventional method of executing `make pdf` proved ineffective, prompting a complete overhaul of my approach. The revised strategy now employs the following command:

    ```bash
    Rscript -e "rmarkdown::render('documents/01-Conception-Phase.md', output_format = 'pdf_document')"
    ```

2. I encountered a minor issue with organizing the folder structure for the documentation, since Gitbook apparently requires a specific format. I resolved this by reverse-engineering the structure of the Gitbook documentation and adapting my own to match.

3. I have been struggling with building a overall documentation structure which fits this project. I have been looking at the [Arc42](https://arc42.org/) template, and i am considering to use it as a base for the documentation.

### What did I learn?

* I have expanded my knowledge of the `markdown` language.
* I have expanded my knowledge of the `make` tool and its shortcomings.
* I have learned how to use `Rscript` to render `markdown` files as `pdf` documents.
* Gitbook has a specific folder structure that must be adhered to.

### What are the tasks for tomorrow?

* I will continue to work on the Conception Phase, and aim to complete the first chapter.

</details>
