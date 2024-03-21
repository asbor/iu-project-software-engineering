import os
import subprocess


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
    subprocess.run(["pandoc", merged_file, "-o", output_file,
                    "--variable=geometry:a4paper", "--variable=geometry:margin=1in",
                    "--pdf-engine=xelatex", "--include-in-header", "preamble.tex",
                    "--base-directory=" + directory])

    # Remove the merged markdown file
    os.remove(merged_file)

    print(f"PDF file created: {output_file}")


def main():
    # Specify the directory containing the markdown files
    markdown_directory = "/home/asbjorn/Nextcloud/repo/iu-project-software-engineering/documents/01-Conception-Phase/chapters"
    outout_file = "../HoppyBrew.pdf"

    # Call the function to merge and convert the files
    merge_and_convert_to_pdf(markdown_directory, outout_file)


if __name__ == "__main__":
    main()
