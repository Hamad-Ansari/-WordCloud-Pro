"""
Animated metric cards showing word statistics.
"""

import streamlit as st


def render_metrics(metrics: dict):
    """
    Render animated metric cards.

    Args:
        metrics: Dictionary with total_words, unique_words, 
                 most_frequent, least_frequent
    """
    col1, col2, col3, col4 = st.columns(4, gap="small")

    with col1:
        st.markdown(
            f"""
            <div class='metric-card'>
                <div class='metric-icon'>📝</div>
                <div class='metric-value'>{metrics['total_words']:,}</div>
                <div class='metric-label'>Total Words</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class='metric-card'>
                <div class='metric-icon'>🔤</div>
                <div class='metric-value'>{metrics['unique_words']:,}</div>
                <div class='metric-label'>Unique Words</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        top_word, top_count = metrics["most_frequent"]
        st.markdown(
            f"""
            <div class='metric-card'>
                <div class='metric-icon'>👑</div>
                <div class='metric-value' style='font-size: 1.2rem;'>{top_word}</div>
                <div class='metric-label'>Top Word ({top_count}×)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        bottom_word, bottom_count = metrics["least_frequent"]
        st.markdown(
            f"""
            <div class='metric-card'>
                <div class='metric-icon'>📉</div>
                <div class='metric-value' style='font-size: 1.2rem;'>{bottom_word}</div>
                <div class='metric-label'>Rarest ({bottom_count}×)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )