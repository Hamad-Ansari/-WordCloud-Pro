"""
╔══════════════════════════════════════════════════════════════╗
║        🔮 Premium Word Cloud Generator — by Hammad Zahid    ║
║        AI & Data Science Enthusiast | Python Developer       ║
╚══════════════════════════════════════════════════════════════╝

A SaaS-level Word Cloud Generator built with Streamlit.
Features: Glassmorphism UI, real-time preview, Plotly charts,
customizable themes, shape masks, and professional branding.
"""

import streamlit as st
import sys
import os

# ── Add project root to path ──────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components.hero import render_hero
from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.uploader import render_uploader
from components.wordcloud_viz import render_wordcloud
from components.frequency_chart import render_frequency_chart
from components.download_panel import render_download_panel
from utils.styling import apply_custom_css, get_color_palettes
from utils.wordcloud_engine import generate_wordcloud_image
from utils.text_processor import extract_text, get_word_stats


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  PAGE CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.set_page_config(
    page_title="WordCloud Pro — Hammad Zahid",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SESSION STATE INITIALIZATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def init_session_state():
    """Initialize all session state variables."""
    defaults = {
        "text": "",
        "word_freq": {},
        "wordcloud_image": None,
        "uploaded_file": None,
        "file_name": None,
        "processing": False,
        "processed": False,
        "metrics": {
            "total_words": 0,
            "unique_words": 0,
            "most_frequent": ("", 0),
            "least_frequent": ("", 0),
        },
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  APPLY GLOBAL STYLING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
apply_custom_css()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  SIDEBAR (renders first — minimal & branded)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with st.sidebar:
    render_sidebar()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  HERO SECTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
render_hero()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN CONTENT — TWO COLUMN LAYOUT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
col_left, col_right = st.columns([1, 1.2], gap="medium")

# ── LEFT COLUMN: Upload + Controls ────────────────────────────
with col_left:
    st.markdown("### 📁 Upload & Configure")
    uploaded_file, file_text = render_uploader()

    if uploaded_file and file_text:
        st.markdown("---")
        st.markdown("### 🎨 Customize Your Cloud")

        # Color palette selector
        palettes = get_color_palettes()
        selected_palette = st.selectbox(
            "Color Palette",
            options=list(palettes.keys()),
            index=0,
            format_func=lambda x: f"{'🎨' if 'Neon' in x else '🌈' if 'Gradient' in x else '🔥' if 'Warm' in x else '❄️' if 'Cool' in x else '💎'} {x}",
        )

        # Background theme
        bg_theme = st.radio(
            "Background Theme",
            options=["Dark", "Light", "Custom Color"],
            horizontal=True,
            index=0,
        )

        if bg_theme == "Custom Color":
            custom_bg = st.color_picker("Pick Background", "#0a0a1a")
        else:
            custom_bg = "#0a0a1a" if bg_theme == "Dark" else "#f0f2f6"

        # Shape mask
        shape_options = ["Circle", "Square", "Rounded Square", "Diamond", "Custom"]
        selected_shape = st.selectbox("Shape Mask", shape_options, index=0)

        # Max words slider
        max_words = st.slider(
            "Max Words",
            min_value=20,
            max_value=300,
            value=100,
            step=10,
            help="Maximum number of words to display",
        )

        # Font size range
        col_fs1, col_fs2 = st.columns(2)
        with col_fs1:
            min_font = st.slider("Min Font Size", 10, 40, 14)
        with col_fs2:
            max_font = st.slider("Max Font Size", 40, 120, 80)

        # Generate button
        generate_clicked = st.button(
            "✨ Generate Word Cloud",
            type="primary",
            use_container_width=True,
        )

        # ── Process on button click ─────────────────────────────
        if generate_clicked:
            with st.spinner("🎨 Crafting your word cloud..."):
                try:
                    # Extract word stats
                    stats = get_word_stats(file_text, max_words=max_words)
                    st.session_state.word_freq = stats["frequency"]
                    st.session_state.metrics = {
                        "total_words": stats["total"],
                        "unique_words": stats["unique"],
                        "most_frequent": stats["top_word"],
                        "least_frequent": stats["bottom_word"],
                    }

                    # Generate word cloud
                    wc_image = generate_wordcloud_image(
                        text=file_text,
                        palette=palettes[selected_palette],
                        bg_color=custom_bg,
                        shape=selected_shape.lower(),
                        max_words=max_words,
                        min_font=min_font,
                        max_font=max_font,
                    )
                    st.session_state.wordcloud_image = wc_image
                    st.session_state.processed = True
                    st.session_state.processing = False
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error generating word cloud: {e}")
                    st.session_state.processing = False


# ── RIGHT COLUMN: Visualizations ──────────────────────────────
with col_right:
    # ── Metrics Cards ──────────────────────────────────────────
    if st.session_state.processed:
        render_metrics(st.session_state.metrics)

    # ── Word Cloud Display ─────────────────────────────────────
    st.markdown("### 🖼️ Word Cloud Preview")
    if st.session_state.wordcloud_image is not None:
        st.image(
            st.session_state.wordcloud_image,
            use_container_width=True,
            caption="Generated Word Cloud",
        )
    else:
        with st.container():
            st.markdown(
                """
                <div style='text-align: center; padding: 60px 20px; 
                            border: 2px dashed rgba(139, 92, 246, 0.3); 
                            border-radius: 16px; background: rgba(139, 92, 246, 0.05);'>
                    <p style='font-size: 48px; margin-bottom: 16px;'>☁️</p>
                    <p style='font-size: 18px; color: #a78bfa; font-weight: 500;'>
                        Upload a file and click Generate
                    </p>
                    <p style='font-size: 14px; color: #6b7280; margin-top: 8px;'>
                        Supports .txt, .pdf, .docx
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ── Frequency Chart ────────────────────────────────────────
    if st.session_state.word_freq:
        render_frequency_chart(st.session_state.word_freq)

    # ── Download Panel ─────────────────────────────────────────
    if st.session_state.processed:
        st.markdown("---")
        render_download_panel(st.session_state.wordcloud_image)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  FOOTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px; color: #6b7280; font-size: 13px;'>
        <p>
            Built with 💜 by <b style='color: #a78bfa;'>Hammad Zahid</b> — 
            AI & Data Science Enthusiast | Python Developer
        </p>
        <p style='margin-top: 4px;'>WordCloud Pro © 2026 — All rights reserved</p>
    </div>
    """,
    unsafe_allow_html=True,
)