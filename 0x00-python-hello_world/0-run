#!/bin/bash
# This script runs a Python script whose filename is stored in the $PYFILE environment variable

# Get the Python script filename from the environment variable
PY_SCRIPT="$PYFILE"

# Check if the filename is provided
if [ -z "$PY_SCRIPT" ]; then
    echo "Error: PYFILE environment variable is not set."
    exit 1
fi

# Check if the file exists
if [ ! -f "$PY_SCRIPT" ]; then
    echo "Error: File $PY_SCRIPT not found."
    exit 1
fi

# Run the Python script
python3 "$PY_SCRIPT"

