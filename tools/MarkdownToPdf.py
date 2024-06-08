import os
import subprocess
import re

def merge_and_convert_to_pdf(directory, output_file):
    """
    Merge all markdown files in the specified directory into a single file and convert it to PDF.

    Args:
        directory (str): The directory containing the markdown files.
    """

    # Get all markdown files in the directory
    markdown_files = [file for file in os.listdir(directory) if file.endswith(".md")]

    # Sort the files alphabetically
    markdown_files.sort()

    # Merge the markdown files into a single file
    merged_file = os.path.join(directory, "merged.md")
    with open(merged_file, "w") as outfile:
        for file in markdown_files:
            with open(os.path.join(directory, file), "r") as infile:
                outfile.write(infile.read())

    # Convert the merged markdown file to PDF
    output_file = os.path.join(directory, output_file)
    subprocess.run(["pandoc",
                    merged_file,
                    "-o",
                    output_file,
                    "--variable=geometry:a4paper",
                    "--variable=geometry:margin=1in",
                    "--pdf-engine=xelatex",
                    "--include-in-header",
                    "./documents/docs/chapters/preamble.tex",
                    "--bibliography=bibliography.bib",
                    "--number-sections"])

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
        chapter_title = chapter_content.split('\n')[0].replace('# ', '')  # Extract chapter title from header
        chapter_filename = f'{destination}{i:02}_{chapter_title.replace(" ", "_")}.md'

        with open(chapter_filename, 'w', encoding='utf-8') as chapter_file:
            # Re-add header to chapter content
            chapter_file.write('# ' + chapter_content + '\n')  # Add newline character

    print(f'{len(chapters)} chapters split and saved successfully.')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    # Change the working directory to the root of the repository
    print(bcolors.OKCYAN + "Working directory: ", os.getcwd() + bcolors.ENDC)
    # Set the working directory to the root of the repository
    os.system('java -jar tools/plantuml-1.2024.3.jar -tpng documents/docs/00-HoppyBrew.md -o ./images/')

    # Note that the markdown files deriving from the main markdown file are not in same directory as the main markdown file (00-HoppyBrew.md)
    # we will therefore need to change the references in the derived markdown files to point to the correct directory

    # Split the markdown file into chapters
    markdown_file = './documents/docs/00-HoppyBrew.md'
    directory = "./documents/docs/chapters/"
    split_chapters(markdown_file, directory)
    output_file = "HoppyBrew.pdf"

    # Call the function to merge and convert the files
    merge_and_convert_to_pdf(directory, output_file)

if __name__ == "__main__":
    main()
