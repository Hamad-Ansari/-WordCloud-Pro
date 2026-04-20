"""
File upload component with drag-and-drop style UI,
format validation, and text extraction.
"""

import streamlit as st
from utils.text_processor import extract_text


def render_uploader() -> tuple:
    """
    Render the file uploader UI.

    Returns:
        Tuple of (uploaded_file_object, extracted_text)
    """
    st.markdown(
        """
        <div class='upload-zone'>
            <p style='font-size: 3rem; margin-bottom: 12px;'>📄</p>
            <p style='font-size: 1.1rem; color: #c4b5fd; font-weight: 600; margin-bottom: 8px;'>
                Drop your file here or click to browse
            </p>
            <p style='font-size: 0.85rem; color: #64748b;'>
                Supports: <b>TXT</b>, <b>PDF</b>, <b>DOCX</b> — Max 10MB
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "",
        type=["txt", "pdf", "docx"],
        help="Upload a text file to generate a word cloud",
        label_visibility="collapsed",
    )

    if uploaded_file is not None:
        # Validate file size (10MB limit)
        file_bytes = uploaded_file.getvalue()
        if len(file_bytes) > 10 * 1024 * 1024:
            st.error("❌ File size exceeds 10MB limit")
            return None, ""

        # Extract text
        try:
            text = extract_text(file_bytes, uploaded_file.name)

            if not text.strip():
                st.warning("⚠️ No text could be extracted from this file.")
                return uploaded_file, ""

            # Show file info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📎 File", uploaded_file.name)
            with col2:
                st.metric("📦 Size", f"{len(file_bytes) / 1024:.1f} KB")
            with col3:
                st.metric("📄 Characters", f"{len(text):,}")

            st.success(f"✅ File loaded successfully — {len(text.split()):,} words detected")

            return uploaded_file, text

        except Exception as e:
            st.error(f"❌ Error processing file: {e}")
            return uploaded_file, ""

    return None, ""