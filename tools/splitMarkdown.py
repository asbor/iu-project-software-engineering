import re


def split_chapters(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Split content into chapters based on headers
    chapters = re.split(r"\n#\s", content)

    # Remove empty strings and trim whitespace
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    # Write each chapter to separate files
    for i, chapter_content in enumerate(chapters, start=1):
        chapter_title = chapter_content.split("\n")[0].replace(
            "# ", ""
        )  # Extract chapter title from header
        chapter_filename = f'./documents/docs/chapters/{i:02}_{chapter_title.replace(" ", "_")}.md'

        with open(chapter_filename, "w", encoding="utf-8") as chapter_file:
            # Re-add header to chapter content
            chapter_file.write(
                "# " + chapter_content + "\n"
            )  # Add newline character

    print(f"{len(chapters)} chapters split and saved successfully.")


if __name__ == "__main__":
    # Replace with the path to your Markdown file
    markdown_file = "./documents/docs/00-HoppyBrew.md"
    split_chapters(markdown_file)
