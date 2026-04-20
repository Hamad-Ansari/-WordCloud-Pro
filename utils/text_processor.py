"""
Text processing utilities: extract text from various file formats
and compute word frequency statistics.
"""

import re
from collections import Counter
from typing import Tuple, Dict


def extract_text(file_bytes: bytes, file_name: str) -> str:
    """
    Extract plain text from uploaded file bytes.

    Supports: .txt, .pdf, .docx

    Args:
        file_bytes: Raw bytes of the uploaded file
        file_name: Original filename for format detection

    Returns:
        Extracted plain text string
    """
    ext = file_name.lower().rsplit(".", 1)[-1] if "." in file_name else ""

    if ext == "txt":
        return _extract_txt(file_bytes)
    elif ext == "pdf":
        return _extract_pdf(file_bytes)
    elif ext == "docx":
        return _extract_docx(file_bytes)
    else:
        raise ValueError(f"Unsupported file format: .{ext}")


def _extract_txt(file_bytes: bytes) -> str:
    """Extract text from .txt files."""
    try:
        return file_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return file_bytes.decode("latin-1")


def _extract_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF files using PyPDF2."""
    try:
        from PyPDF2 import PdfReader

        reader = PdfReader(file_bytes)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except ImportError:
        raise ImportError("PyPDF2 is required for PDF support. Install it via: pip install PyPDF2")
    except Exception as e:
        raise RuntimeError(f"PDF extraction failed: {e}")


def _extract_docx(file_bytes: bytes) -> str:
    """Extract text from DOCX files using python-docx."""
    try:
        from docx import Document
        import io

        doc = Document(io.BytesIO(file_bytes))
        paragraphs = [p.text for p in doc.paragraphs]
        return "\n".join(paragraphs)
    except ImportError:
        raise ImportError(
            "python-docx is required for DOCX support. "
            "Install it via: pip install python-docx"
        )
    except Exception as e:
        raise RuntimeError(f"DOCX extraction failed: {e}")


def clean_text(text: str) -> str:
    """
    Clean and normalize text for word cloud generation.

    Removes excessive whitespace, special characters, and normalizes case.
    """
    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)
    # Remove special characters but keep apostrophes and hyphens in words
    text = re.sub(r"[^\w\s'-]", " ", text)
    # Normalize to lowercase
    text = text.lower()
    return text.strip()


def get_word_stats(text: str, max_words: int = 100) -> Dict:
    """
    Compute word frequency statistics.

    Args:
        text: Input text string
        max_words: Maximum number of top words to return

    Returns:
        Dictionary containing frequency data and metrics
    """
    cleaned = clean_text(text)
    words = cleaned.split()

    # Filter out very short words and common stopwords
    stopwords = {
        "the", "and", "is", "in", "to", "of", "a", "an", "for", "on",
        "with", "at", "by", "from", "it", "as", "be", "are", "was",
        "were", "has", "have", "had", "but", "not", "or", "this",
        "that", "you", "he", "she", "we", "they", "i", "my", "your",
    }

    filtered = [w for w in words if len(w) > 2 and w not in stopwords]

    if not filtered:
        # If everything was filtered, use all words
        filtered = [w for w in words if len(w) > 1]

    counter = Counter(filtered)
    frequency = dict(counter.most_common(max_words))

    total = len(words)
    unique = len(counter)

    if frequency:
        top_word = max(frequency.items(), key=lambda x: x[1])
        bottom_word = min(frequency.items(), key=lambda x: x[1])
    else:
        top_word = ("N/A", 0)
        bottom_word = ("N/A", 0)

    return {
        "frequency": frequency,
        "total": total,
        "unique": unique,
        "top_word": top_word,
        "bottom_word": bottom_word,
    }