#!/bin/bash

# Define the target directory
TARGET_DIR="services/backend"

# Format Python files with autopep8, ignoring errors if any
find $TARGET_DIR -type f -name "*.py" -exec autopep8 --in-place --aggressive --aggressive {} + || true

# Format Python files with black with a line length of 79
black --line-length 79 $TARGET_DIR
