import os
import subprocess
import re


def merge_and_convert_to_pdf(directory, output_file):
    markdown_files = [file for file in os.listdir(
        directory) if file.endswith(".md")]
    markdown_files.sort()
    merged_file = os.path.join(directory, "merged.md")
    with open(merged_file, "w") as outfile:
        for file in markdown_files:
            with open(os.path.join(directory, file), "r") as infile:
                outfile.write(infile.read())
    print(f"Markdown files to merge: {markdown_files}")
    output_file = os.path.join(directory, output_file)
    cmd = [
        "pandoc", merged_file, "-o", output_file,
        "--variable=geometry:a4paper", "--variable=geometry:margin=1in",
        "--pdf-engine=xelatex",
        "--bibliography=bibliography.bib", "--number-sections",
        # Corrected path to preamble.tex
        "--include-in-header", "documents/docs/preamble.tex"
    ]
    print(f"Running command: {' '.join(cmd)}")
    subprocess.run(cmd)
    os.remove(merged_file)
    print(f"PDF file created: {output_file}")


def split_chapters(markdown_file, destination):
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('](images/', '](../images/')
    chapters = re.split(r'\n#\s', content)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]
    for i, chapter_content in enumerate(chapters, start=1):
        chapter_title = chapter_content.split('\n')[0].replace('# ', '')
        chapter_filename = f'{destination}{i:02}_{chapter_title.replace(" ", "_")}.md'
        with open(chapter_filename, 'w', encoding='utf-8') as chapter_file:
            chapter_file.write('# ' + chapter_content + '\n')
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
    print(bcolors.OKCYAN + "Working directory: ", os.getcwd() + bcolors.ENDC)
    os.system(
        'java -jar tools/plantuml-1.2024.3.jar -tpng documents/docs/00-HoppyBrew.md -o ./images/')
    markdown_file = './documents/docs/00-HoppyBrew.md'
    directory = "./documents/docs/chapters/"
    split_chapters(markdown_file, directory)
    output_file = "HoppyBrew.pdf"
    merge_and_convert_to_pdf(directory, output_file)


if __name__ == "__main__":
    main()
