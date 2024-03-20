import os
import subprocess


def merge_and_convert_to_pdf(directory):
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
    output_file = os.path.join(directory, "merged.pdf")
    # subprocess.run(["pandoc", merged_file, "-o", output_file])
    # subprocess.run(["pandoc", merged_file, "-o", output_file, "--variable=geometry:a4paper", "--variable=geometry:margin=1in"])
    # subprocess.run(["pandoc", merged_file, "-o", output_file,
    #                "--variable=geometry:a4paper", "--variable=geometry:margin=1in",
    #                "--pdf-engine=xelatex", "--include-in-header", "preamble.tex"])
    subprocess.run(["pandoc", merged_file, "-o", output_file,
                    "--variable=geometry:a4paper", "--variable=geometry:margin=1in",
                    "--pdf-engine=xelatex", "--include-in-header", "preamble.tex"])

    # Remove the merged markdown file
    os.remove(merged_file)

    print(f"PDF file created: {output_file}")


# Specify the directory containing the markdown files
markdown_directory = "/home/asbjorn/Nextcloud/repo/iu-project-software-engineering/documents/01-Conception-Phase/chapters_markdown"

# Call the function to merge and convert the files
merge_and_convert_to_pdf(markdown_directory)
