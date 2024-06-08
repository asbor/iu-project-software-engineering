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
    markdown_files = [file for file in os.listdir(
        directory) if file.endswith(".md")]
    # Sort the files alphabetically
    markdown_files.sort()
    print("Markdown files to merge:", markdown_files)
    # Merge the markdown files into a single file
    merged_file = os.path.join(directory, "merged.md")
    with open(merged_file, "w") as outfile:
        for file in markdown_files:
            with open(os.path.join(directory, file), "r") as infile:
                outfile.write(infile.read())
    # Convert the merged markdown file to PDF
    output_file = os.path.join(directory, output_file)
    preamble_path = os.path.join(directory, "preamble.tex")
    command = [
        "pandoc",
        merged_file,
        "-o", output_file,
        "--variable=geometry:a4paper",
        "--variable=geometry:margin=1in",
        "--pdf-engine=xelatex",
        "--bibliography=bibliography.bib",
        "--number-sections"
    ]
    if os.path.exists(preamble_path):
        command.extend(["--include-in-header", preamble_path])
    print("Running command:", " ".join(command))
    subprocess.run(command)
    # Remove the merged markdown file
    os.remove(merged_file)
    print(f"PDF file created: {output_file}")


def split_chapters(markdown_file, destination):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()
    # Change references to images to point to the correct directory
    content = content.replace('](images/', '](../images/')
    # Split content into chapters based on headers
    chapters = re.split(r'\n#\s', content)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]
    for i, chapter_content in enumerate(chapters, start=1):
        chapter_title = chapter_content.split('\n')[0].replace('# ', '')
        chapter_filename = f'{destination}{i:02}_{chapter_title.replace(" ", "_")}.md'
        with open(chapter_filename, 'w', encoding='utf-8') as chapter_file:
            chapter_file.write('# ' + chapter_content + '\n')
    print(f'{len(chapters)} chapters split and saved successfully.')


def main():
    print("Working directory: ", os.getcwd())
    os.system(
        'java -jar tools/plantuml-1.2024.3.jar -tpng documents/docs/00-HoppyBrew.md -o ./images/')
    markdown_file = './documents/docs/00-HoppyBrew.md'
    directory = "./documents/docs/chapters/"
    split_chapters(markdown_file, directory)
    output_file = "HoppyBrew.pdf"
    merge_and_convert_to_pdf(directory, output_file)


if __name__ == "__main__":
    main()
