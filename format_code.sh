#!/bin/bash

# Specify the backend directory
BACKEND_DIR="services/backend"

# Run black
black --line-length 79 $BACKEND_DIR

# Run autopep8
autopep8 --in-place --aggressive --aggressive --recursive $BACKEND_DIR

# Run docformatter
docformatter --in-place --recursive --wrap-summaries 79 --wrap-descriptions 79 $BACKEND_DIR

# Run custom wrap comments script
python wrap_comments.py $BACKEND_DIR --width 79
