"""
Clean, minimal sidebar with branding, bio, and social links.
"""

import streamlit as st


def render_sidebar():
    """Render the branded sidebar."""

    # ── Branding ──────────────────────────────────────────────
    st.markdown(
        """
        <div class='sidebar-brand'>
            <p class='sidebar-name'>🔮 WordCloud Pro</p>
            <p class='sidebar-bio'>by Hammad Zahid</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Bio ───────────────────────────────────────────────────
    st.markdown(
        """
        <div style='text-align: center; padding: 16px; 
                    color: #94a3b8; font-size: 0.85rem; line-height: 1.6;'>
            <p>🤖 AI & Data Science Enthusiast</p>
            <p>🐍 Python Developer</p>
            <p>📊 Data Visualization Lover</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ── Social Links ──────────────────────────────────────────
    st.markdown("### 🌐 Connect")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <a href='https://www.linkedin.com/in/hammad-zahid-xyz/' 
               target='_blank' 
               style='text-decoration: none; color: #a78bfa; 
                      font-size: 0.9rem; display: block; padding: 8px; 
                      border-radius: 8px; text-align: center; 
                      background: rgba(139,92,246,0.1); 
                      border: 1px solid rgba(139,92,246,0.2);
                      transition: all 0.3s;'>
                💼 LinkedIn
            </a>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <a href='https://github.com/Hamad-Ansari' 
               target='_blank' 
               style='text-decoration: none; color: #a78bfa; 
                      font-size: 0.9rem; display: block; padding: 8px; 
                      border-radius: 8px; text-align: center; 
                      background: rgba(139,92,246,0.1); 
                      border: 1px solid rgba(139,92,246,0.2);
                      transition: all 0.3s;'>
                🐱 GitHub
            </a>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── App Info ──────────────────────────────────────────────
    st.markdown(
        """
        <div style='text-align: center; padding: 16px; color: #475569; font-size: 0.75rem;'>
            <p>WordCloud Pro v1.0</p>
            <p>© 2025 Hammad Zahid</p>
        </div>
        """,
        unsafe_allow_html=True,
    )