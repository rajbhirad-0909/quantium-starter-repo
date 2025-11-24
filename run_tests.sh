#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest

# Return exit code based on pytest result
if [ $? -eq 0 ]; then
    echo "All tests passed successfully."
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi


