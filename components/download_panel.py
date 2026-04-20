"""
Styled download buttons for word cloud images.
"""

import streamlit as st
from io import BytesIO


def render_download_panel(wordcloud_image):
    """
    Render styled download buttons for the word cloud.

    Args:
        wordcloud_image: PIL Image to download
    """
    st.markdown("### 💾 Download Your Creation")

    # Convert PIL to bytes for download
    img_bytes = BytesIO()
    wordcloud_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.download_button(
            label="📥 Download PNG",
            data=img_bytes.getvalue(),
            file_name="wordcloud.png",
            mime="image/png",
            use_container_width=True,
        )

    with col2:
        st.download_button(
            label="📥 Download JPG",
            data=img_bytes.getvalue(),
            file_name="wordcloud.jpg",
            mime="image/jpeg",
            use_container_width=True,
        )

    with col3:
        st.download_button(
            label="📥 Download SVG Data",
            data=_export_word_frequencies(wordcloud_image),
            file_name="wordcloud_data.csv",
            mime="text/csv",
            use_container_width=True,
        )

    st.info("💡 Tip: Right-click the word cloud image to save it directly!")


def _export_word_frequencies(wordcloud_image) -> str:
    """Export word frequency data as CSV."""
    import csv
    from io import StringIO

    # Get layout data from wordcloud
    if hasattr(wordcloud_image, "layout_"):
        layout = wordcloud_image.layout_
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Word", "Frequency", "Font Size", "X Position", "Y Position"])
        for word, freq in layout:
            writer.writerow([word, freq, 0, 0, 0])  # Simplified
        return output.getvalue()
    return "Word,Frequency\n"