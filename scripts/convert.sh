#!/bin/bash

# Prequisites:
# - poppler-utils

# Function:
# Converts the .pdf file given with argument 1 into a
# .txt file readable by the Python script.

# Usage:
# convert.sh <file to convert>

pdftotext -layout $1