#!/bin/bash

VENV_PATH="./pdf_venv"

# Activate the virtual environment
if [ -f "$VENV_PATH/bin/activate" ]; then
    source "$VENV_PATH/bin/activate"
else
    echo "Error: Virtual environment activation script not found at $VENV_PATH/bin/activate"
    exit 1
fi

streamlit run pdf_merger.py
