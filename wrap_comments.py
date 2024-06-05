import os
import textwrap


def wrap_text(text, width=79):
    wrapped_lines = []
    for paragraph in text.split("\n\n"):
        wrapped_lines.extend(textwrap.wrap(paragraph, width=width))
        wrapped_lines.append('')
    return "\n".join(wrapped_lines).strip()


def process_file(file_path, width=79):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    wrapped_lines = []
    inside_docstring = False
    for line in lines:
        stripped_line = line.rstrip()
        if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
            inside_docstring = not inside_docstring
            wrapped_lines.append(line.rstrip())
        elif inside_docstring or stripped_line.startswith('#'):
            wrapped_lines.extend(textwrap.wrap(
                stripped_line, width=width, subsequent_indent='    '))
        else:
            wrapped_lines.append(line.rstrip())
    # Remove unnecessary blank lines
    cleaned_lines = []
    previous_blank = False
    for line in wrapped_lines:
        if line.strip() == '':
            if not previous_blank:
                cleaned_lines.append(line)
            previous_blank = True
        else:
            cleaned_lines.append(line)
            previous_blank = False

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(cleaned_lines).strip() + "\n")


def process_directory(directory, width=79):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                process_file(os.path.join(root, file), width)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='Wrap comments and docstrings in Python files.')
    parser.add_argument('directory', type=str, help='Directory to process.')
    parser.add_argument('--width', type=int, default=79,
                        help='Line width for wrapping.')
    args = parser.parse_args()
    process_directory(args.directory, args.width)
