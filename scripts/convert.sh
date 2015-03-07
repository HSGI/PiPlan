#!/bin/bash

# Prequisites:
# - poppler-utils

# Function:
# Converts the PDF-file given as argument 1 into a JSON-file
# with its name given by argument 2.

# Usage:
# convert.sh <input file> <output file>

if [ -z "$1" ] || [ -z "$2" ] ; then
	echo "Usage: $0 <input file> <output file>"
	exit 1
else
	$tmpfile=$(mktemp)
	pdftotext -layout $1 $tmpfile
	python input.py $tmpfile $2
	rm $tmpfile
fi
