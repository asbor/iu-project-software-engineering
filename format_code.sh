#!/bin/bash

# Run black
black --line-length 79 .

# Run autopep8
autopep8 --in-place --aggressive --aggressive --recursive .

# Run docformatter
docformatter --in-place --recursive --wrap-summaries 79 --wrap-descriptions 79 .
