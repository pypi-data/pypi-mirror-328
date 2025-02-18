#!/bin/bash

# Activate virtual environment if it exists, create if it doesn't
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate

# Install the library in development mode
echo "Installing dynamixel-async in development mode..."
pip install -e .

# Run the basic control example
echo "Running basic control example..."
python3 examples/basic_control.py

# Deactivate virtual environment
deactivate 