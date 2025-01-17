import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from streamlit_sortables import sort_items
import PyPDF2
import io

if __name__ == "__main__":
    st.set_page_config(page_title="PDF merger")
    st.header("📑 PDF Merger")
   
    merger = PyPDF2.PdfMerger()

    files: None | list[UploadedFile] = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=True)
    
    if files is None or not files:
        st.stop()

    db = {}
    for file in files:
        db[file.name] = file
    
    # finished_uploads = st.checkbox("All files uploaded")
    # if not finished_uploads:
    #     st.stop()

    file_names = [f.name for f in files]
    sort_widget = sort_items(file_names, direction="vertical")
   
    sorted_files = [db[s] for s in sort_widget]

    for file in sorted_files:
        merger.append(file)
    
    pdf_buffer = io.BytesIO()
    merger.write(pdf_buffer)
    merger.close()
    pdf_buffer.seek(0)
    
    st.download_button(
        label="📥 Download Merged PDF",
        type="primary",
        data=pdf_buffer,
        file_name="merged.pdf",
        mime="application/pdf"
    )

