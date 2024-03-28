import os
import subprocess
import re


def merge_and_convert_to_pdf(directory, outout_file):
    """
    Merge all markdown files in the specified directory into a single file and convert it to PDF.

    Args:
        directory (str): The directory containing the markdown files.
    """

    # Get all markdown files in the directory
    markdown_files = [file for file in os.listdir(
        directory) if file.endswith(".md")]

    # Sort the files alphabetically
    markdown_files.sort()

    # Merge the markdown files into a single file
    merged_file = os.path.join(directory, "merged.md")
    with open(merged_file, "w") as outfile:
        for file in markdown_files:
            with open(os.path.join(directory, file), "r") as infile:
                outfile.write(infile.read())

    # Convert the merged markdown file to PDF
    output_file = os.path.join(directory, outout_file)
    # subprocess.run(["pandoc", merged_file, "-o", output_file,
    #                "--variable=geometry:a4paper", "--variable=geometry:margin=1in",
    #                "--pdf-engine=xelatex", "--include-in-header", "preamble.tex",
    #                "--bibliography=bibliography.bib", "--number-sections"])
    # Define Pandoc template file

    # Run Pandoc with the necessary options, including the template
    subprocess.run([
        "pandoc", merged_file, "-o", output_file,
        "--from=markdown",  # Specify input format as Markdown
        "--to=pdf",  # Specify output format as PDF
        "--variable=geometry:a4paper",
        "--variable=geometry:margin=1in",
        "--pdf-engine=xelatex",
        "--number-sections"
    ])
    # Remove the merged markdown file
    os.remove(merged_file)

    print(f"PDF file created: {output_file}")


def split_chapters(markdown_file, destination):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Change references to images to point to the correct directory (../images/) instead of (images/)
    content = content.replace('](images/', '](../images/')

    # Split content into chapters based on headers
    chapters = re.split(r'\n#\s', content)

    # Remove empty strings and trim whitespace
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    # Write each chapter to separate files
    for i, chapter_content in enumerate(chapters, start=1):
        chapter_title = chapter_content.split('\n')[0].replace(
            '# ', '')  # Extract chapter title from header
        chapter_filename = f'{destination}{i:02}_{chapter_title.replace(" ", "_")}.md'

        with open(chapter_filename, 'w', encoding='utf-8') as chapter_file:
            # Re-add header to chapter content
            chapter_file.write('# ' + chapter_content +
                               '\n')  # Add newline character

    print(f'{len(chapters)} chapters split and saved successfully.')


def main():
    # Runn bash command
    #
    # os.system(
    #    'bash plantuml -tpng documents/01-Conception-Phase/00-HoppyBrew.md -o images/')
    # the new approach is like this
    # java -jar plantuml-1.2024.3.jar -tpng ../documents/01-Conception-Phase/plantuml/04-white-box-overall-system.puml

    # Set the working directory to the root of the repository
    os.chdir('/home/asbjorn/Nextcloud/repo/iu-project-software-engineering')
    os.system(
        'java -jar tools/plantuml-1.2024.3.jar -tpng documents/01-Conception-Phase/00-HoppyBrew.md -o ./images/')

    # Set the working directory to the 01-Conception-Phase directory
    os.chdir('./documents/01-Conception-Phase')

    # Note that the markdown files deriving from the main markdown file are not in same directory as the main markdown file (00-HoppyBrew.md)
    # we will therefore need to change the references in the derived markdown files to point to the correct directory

    # Split the markdown file into chapters
    markdown_file = '00-HoppyBrew.md'
    destination = './chapters/'
    split_chapters(markdown_file, destination)

    # Set the working directory to the 01-Conception-Phase/chapters directory so th

    # Specify the directory containing the markdown files
    directory = "/home/asbjorn/Nextcloud/repo/iu-project-software-engineering/documents/01-Conception-Phase/chapters"
    outout_file = "../HoppyBrew.pdf"

    # Change the working directory to the directory containing markdown files
    os.chdir(directory)

    # Call the function to merge and convert the files
    merge_and_convert_to_pdf(directory, outout_file)


if __name__ == "__main__":
    main()
