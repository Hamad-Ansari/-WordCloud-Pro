"""
Hero section component with animated title, subtitle,
author name, and professional branding badge.
"""

import streamlit as st


def render_hero():
    """Render the hero section with animations and branding."""

    st.markdown(
        """
        <div class='hero-container'>
            <h1 class='hero-title'>✨ WordCloud Pro</h1>
            <p class='hero-subtitle'>Transform your text into stunning visual art</p>
            <p class='hero-author'>🚀 Built by <b>Hammad Zahid</b></p>
            <span class='hero-badge'>
                🤖 AI & Data Science Enthusiast &nbsp;|&nbsp; 
                🐍 Python Developer
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")