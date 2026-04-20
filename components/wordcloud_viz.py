"""
Word cloud visualization component with real-time preview.
"""

import streamlit as st
from utils.wordcloud_engine import generate_wordcloud_image, add_glow_effect


def render_wordcloud(wordcloud_image):
    """
    Render the word cloud image with styled container.

    Args:
        wordcloud_image: PIL Image from the word cloud engine
    """
    # Add subtle glow effect
    glowed = add_glow_effect(wordcloud_image, intensity=15)

    st.markdown(
        """
        <div style='
            background: rgba(255,255,255,0.02);
            border-radius: 20px;
            padding: 16px;
            border: 1px solid rgba(139,92,246,0.1);
        '>
        """,
        unsafe_allow_html=True,
    )

    st.image(
        glowed,
        use_container_width=True,
        caption="✨ Generated Word Cloud",
    )

    st.markdown("</div>", unsafe_allow_html=True)