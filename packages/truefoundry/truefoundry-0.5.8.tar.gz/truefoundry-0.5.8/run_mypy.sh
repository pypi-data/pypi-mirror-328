#!/bin/bash

set -e

mypy --strict --no-color-output 2>.mypy-errors.txt || true
echo "Count for all error types"

echo "===================================================================="
grep -oE '\[([a-z-]+)\]$' .mypy-errors.txt | grep -oE '[a-z-]+' | sort | uniq -c | sort -nr || true
echo "===================================================================="

echo "Checking for errors that require fixing"

echo "===================================================================="
if grep -E '\[(call-arg|valid-type)\]$' .mypy-errors.txt; then
    echo "Found the above errors. Please fix them"
    echo "===================================================================="
    exit 1
else
    echo "No errors that require fixing"
    echo "===================================================================="
fi

rm -rf .mypy-errors.txt
