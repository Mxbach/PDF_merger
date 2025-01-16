from pathlib import Path
import PyPDF2

merger = PyPDF2.PdfMerger()

files_dir = Path("./input_pdfs")

for file in files_dir.glob("*.pdf"):
    merger.append(str(file))

merger.write("merged.pdf")
merger.close()

print("Done")