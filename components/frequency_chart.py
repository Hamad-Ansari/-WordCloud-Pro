"""
Animated Plotly bar chart showing top word frequencies.
"""

import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


def render_frequency_chart(word_freq: dict, top_n: int = 20):
    """
    Render an animated Plotly horizontal bar chart of word frequencies.

    Args:
        word_freq: Dictionary of {word: count}
        top_n: Number of top words to display
    """
    # Sort and get top N
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words = [w[0] for w in sorted_words]
    counts = [w[1] for w in sorted_words]

    # Create color gradient based on frequency
    colors = px.colors.sequential.Plasma_r

    fig = go.Figure(
        go.Bar(
            x=counts,
            y=words,
            orientation="h",
            marker=dict(
                color=counts,
                colorscale=colors,
                line=dict(color="rgba(139, 92, 246, 0.3)", width=1),
            ),
            text=[f"{c}" for c in counts],
            textposition="outside",
            textfont=dict(size=11, color="#94a3b8"),
            hovertemplate="<b>%{y}</b><br>Frequency: %{x}<extra></extra>",
        )
    )

    fig.update_layout(
        title=dict(
            text="📊 Top Word Frequencies",
            font=dict(size=18, color="#e2e8f0", family="Inter, sans-serif"),
        ),
        xaxis=dict(
            title="Frequency",
            gridcolor="rgba(139, 92, 246, 0.1)",
            zerolinecolor="rgba(139, 92, 246, 0.1)",
            tickfont=dict(color="#64748b"),
        ),
        yaxis=dict(
            tickfont=dict(color="#94a3b8", size=12),
            automargin=True,
        ),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20),
        height=max(300, len(words) * 28),
        bargap=0.2,
        font=dict(family="Inter, sans-serif"),
    )

    st.plotly_chart(fig, use_container_width=True)