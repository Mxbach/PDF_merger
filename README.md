# PDF Merger

A simple and lightweight tool to merge PDF files.  
Currently, a **Streamlit frontend** is under development to provide a user-friendly interface.

## Installation

It is recommended to use a virtual environment to keep dependencies isolated.

### 1. Create and activate a virtual environment

#### Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (cmd):
```cmd
python -m venv venv
venv\Scripts\activate
```

To deactivate the virtual environment:
```bash
deactivate
```

### 2. Install dependencies
Ensure you have **Python 3.x** installed, then run:
```bash
pip install -r requirements.txt
```

## Usage

After setting up the environment, you can merge all PDFs from a directory:

```bash
python merge_from_dir.py
```

### Example
If the `input_pdfs/` directory contains:
```
document1.pdf
document2.pdf
document3.pdf
```
Running the script will merge them into a single `merged.pdf` file.

## Streamlit Frontend

A graphical user interface (GUI) is being developed using **Streamlit**.  
You can start the frontend with:

```bash
streamlit run pdf_merger.py
```