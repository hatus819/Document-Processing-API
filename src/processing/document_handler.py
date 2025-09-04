from typing import Optional
from src.processing.pdf_processor import transcribe_text_from_pdf_bytes
from src.processing.word_processor import transcribe_text_from_word_bytes

def process_document(filename: str, file_bytes: bytes) -> str:
    """
    Process a document based on its file extension and extract text.

    Args:
        filename (str): The name of the file.
        file_bytes (bytes): The raw bytes of the file.

    Returns:
        str: The extracted text content.

    Raises:
        ValueError: If the file extension is unsupported.
    """
    if filename.lower().endswith(".pdf"):
        return transcribe_text_from_pdf_bytes(file_bytes)
    elif filename.lower().endswith(".docx"):
        return transcribe_text_from_word_bytes(file_bytes)
    else:
        raise ValueError(f"Unsupported file extension for file: {filename}")
