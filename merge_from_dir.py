from pathlib import Path
import PyPDF2

merger = PyPDF2.PdfMerger()

files_dir = Path("./files")  # Define the directory as a Path object

for file in files_dir.glob("*.pdf"):  # Use pathlib's glob method to find PDF files
    merger.append(str(file))  # Convert Path object to string when passing to PyPDF2

merger.write("merged.pdf")
merger.close()  # Close the merger to free resources

print("Done")