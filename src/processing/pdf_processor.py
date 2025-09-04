import fitz  # PyMuPDF

def transcribe_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    """
    Extract text from PDF bytes using PyMuPDF.

    Args:
        pdf_bytes (bytes): The raw bytes of the PDF file.

    Returns:
        str: The extracted text from all pages.
    """
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
