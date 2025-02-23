# Activate the virtual environment
$venvPath = ".\pdf_venv\Scripts\Activate"
if (Test-Path $venvPath) {
    & $venvPath
    Write-Output "Virtual environment 'pdf_venv' activated."
} else {
    Write-Host "Virtual environment not found at $venvPath"
    exit 1
}

# Run the Streamlit application
streamlit run pdf_merger.py
