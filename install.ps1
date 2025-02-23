# Create a Python virtual environment in the "pdf_venv" directory
python -m venv pdf_venv

# Check if the virtual environment was created successfully
if (!(Test-Path -Path ".\pdf_venv\Scripts\Activate.ps1")) {
    Write-Error "Virtual environment creation failed. Ensure that Python is installed and added to your PATH."
    exit 1
}

# Activate the virtual environment
& .\pdf_venv\Scripts\Activate.ps1

# Upgrade pip (optional but recommended)
pip install --upgrade pip

# Install dependencies from the requirements.txt file
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
} else {
    Write-Warning "requirements.txt not found. Skipping dependency installation."
}

Write-Output "Environment setup complete."
