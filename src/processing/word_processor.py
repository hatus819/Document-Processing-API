from docx import Document
from io import BytesIO

def transcribe_text_from_word_bytes(word_bytes: bytes) -> str:
    """
    Extract text from DOCX bytes using python-docx.

    Args:
        word_bytes (bytes): The raw bytes of the DOCX file.

    Returns:
        str: The extracted text from all paragraphs.
    """
    doc = Document(BytesIO(word_bytes))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()
