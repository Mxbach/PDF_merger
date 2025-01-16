import streamlit as st
import PyPDF2
import io

if __name__ == "__main__":
    st.set_page_config(page_title="PDF merger")
    st.header("📑 PDF Merger")
   
    merger = PyPDF2.PdfMerger()

    files = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=True)

    if files is None:
        st.stop()
    
    finished_uploads = st.checkbox("All files uploaded")
    if not finished_uploads:
        st.stop()

    for file in files:
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

