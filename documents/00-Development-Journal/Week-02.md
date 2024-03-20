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

<details>

<summary><strong>Wednesday, 20th of March 2024</strong></summary>

***

### What did I do today?

* Yesterday i noticed that the formatting of the Tables in the `markdown` files deviated substantially from the `pdf` output. I have been looking for a solution to this problem, and i have just found out that the amount of dashes (-) in the table translates to the width of the columns in the `pdf` output. I have now fixed the tables in the `markdown` files.
* Also R tends to be very sensitive to its packages, and i have been trying to resolve several issues with these. As of now, i believe all packages have been correctly installed, updated, upgraded and all the paths between the packages are correct. This tends to be very time consuming, but once it is done, i will be able to focus on the actual development of the project.
* I have finally come to the enevitable conclusion that i will have to put the R Markdown/Bookdown approach to rest. This is the third project where i have been using R Markdown/Bookdown, and allthough i was sucessful in the previouse two projects, it was not without its never ending struggle to debug and fix issues that arose. In retrospect, i believe i have learned a lot from using R Markdown/Bookdown, but i have also come to the conclusion that it is not the right tool for this project. I will now focus on building the documentation in a more straight forward way, and i will use the `markdown` files as a base for the documentation. 

### Which challenges did I encounter?

* I have been struggling with the formatting of the tables in the `markdown` files. I have now fixed this issue.
* I have been struggling with the installation of the R packages, and the paths between them. I have now resolved this issue.

### What did I learn?

* Allthough it is possible to format the tables in the `Rmarkdown` files in such a way that it looks good both the `pdf` and `markdown` output, it appears that Gitbook tends to be ever so slightly more picky about the formatting of the tables and will not render them like the other outputs. This is something i will have to keep in mind when writing the documentation. I guess there is always a trade-off between the different applications, and since i am considering to substitude Gitbook with some form of self-hosted alternative, like [MkDocs](https://www.mkdocs.org/), this might not be a problem in the future.


### What are the tasks for tomorrow?


</details>
