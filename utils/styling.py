"""
Custom CSS styling utilities for glassmorphism UI,
animations, and the modern AI dashboard theme.
"""

import streamlit as st


def apply_custom_css():
    """Inject custom CSS for the premium glassmorphism theme."""

    st.markdown(
        """
        <style>
        /* ═══════════════════════════════════════════════════════════
           GLOBAL STYLES — Dark Gradient Theme
           ═══════════════════════════════════════════════════════════ */

        /* Base background gradient */
        .stApp {
            background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 25%,
                                         #0f172a 50%, #0a1628 75%, #0a0a1a 100%);
            background-attachment: fixed;
        }

        /* Remove default Streamlit padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        /* ═══════════════════════════════════════════════════════════
           GLASSMORPHISM CARDS
           ═══════════════════════════════════════════════════════════ */

        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(139, 92, 246, 0.15);
            border-radius: 20px;
            padding: 24px;
            box-shadow:
                0 8px 32px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .glass-card:hover {
            border-color: rgba(139, 92, 246, 0.35);
            box-shadow:
                0 12px 40px rgba(139, 92, 246, 0.15),
                inset 0 1px 0 rgba(255, 255, 255, 0.08);
            transform: translateY(-2px);
        }

        /* ═══════════════════════════════════════════════════════════
           HERO SECTION
           ═══════════════════════════════════════════════════════════ */

        .hero-container {
            text-align: center;
            padding: 60px 20px 40px;
            position: relative;
            overflow: hidden;
        }

        .hero-container::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at center,
                rgba(139, 92, 246, 0.08) 0%,
                transparent 50%);
            animation: heroPulse 6s ease-in-out infinite;
            pointer-events: none;
        }

        @keyframes heroPulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.1); opacity: 1; }
        }

        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 12px;
            letter-spacing: -1px;
            animation: fadeInDown 0.8s ease-out;
            position: relative;
            z-index: 1;
        }

        .hero-subtitle {
            font-size: 1.3rem;
            color: #94a3b8;
            font-weight: 400;
            margin-bottom: 8px;
            animation: fadeInUp 0.8s ease-out 0.2s both;
            position: relative;
            z-index: 1;
        }

        .hero-author {
            font-size: 1.1rem;
            color: #a78bfa;
            font-weight: 600;
            margin-bottom: 20px;
            animation: fadeInUp 0.8s ease-out 0.4s both;
            position: relative;
            z-index: 1;
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 24px;
            background: rgba(139, 92, 246, 0.15);
            border: 1px solid rgba(139, 92, 246, 0.3);
            border-radius: 50px;
            color: #c4b5fd;
            font-size: 0.9rem;
            font-weight: 500;
            animation: fadeInUp 0.8s ease-out 0.6s both;
            position: relative;
            z-index: 1;
        }

        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ═══════════════════════════════════════════════════════════
           METRIC CARDS
           ═══════════════════════════════════════════════════════════ */

        .metric-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(139, 92, 246, 0.12);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s ease;
            animation: metricFadeIn 0.5s ease-out both;
        }

        .metric-card:hover {
            border-color: rgba(139, 92, 246, 0.3);
            transform: translateY(-4px);
            box-shadow: 0 8px 25px rgba(139, 92, 246, 0.15);
        }

        .metric-icon {
            font-size: 2rem;
            margin-bottom: 8px;
        }

        .metric-value {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, #a78bfa, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .metric-label {
            font-size: 0.85rem;
            color: #64748b;
            margin-top: 4px;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 500;
        }

        @keyframes metricFadeIn {
            from { opacity: 0; transform: translateY(20px) scale(0.95); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        /* Stagger metric card animations */
        .metric-card:nth-child(1) { animation-delay: 0.1s; }
        .metric-card:nth-child(2) { animation-delay: 0.2s; }
        .metric-card:nth-child(3) { animation-delay: 0.3s; }
        .metric-card:nth-child(4) { animation-delay: 0.4s; }

        /* ═══════════════════════════════════════════════════════════
           SIDEBAR STYLING
           ═══════════════════════════════════════════════════════════ */

        [data-testid="stSidebar"] {
            background: rgba(10, 10, 26, 0.95);
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(139, 92, 246, 0.1);
        }

        [data-testid="stSidebar"] .sidebar-brand {
            text-align: center;
            padding: 20px 0;
            border-bottom: 1px solid rgba(139, 92, 246, 0.1);
            margin-bottom: 20px;
        }

        [data-testid="stSidebar"] .sidebar-name {
            font-size: 1.2rem;
            font-weight: 700;
            color: #a78bfa;
        }

        [data-testid="stSidebar"] .sidebar-bio {
            font-size: 0.75rem;
            color: #64748b;
            margin-top: 4px;
        }

        /* ═══════════════════════════════════════════════════════════
           BUTTONS
           ═══════════════════════════════════════════════════════════ */

        .stButton > button {
            border-radius: 12px;
            border: 1px solid rgba(139, 92, 246, 0.3);
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.2),
                                         rgba(59, 130, 246, 0.2));
            color: #e2e8f0;
            font-weight: 600;
            padding: 12px 32px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            font-size: 1rem;
            width: 100%;
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.4),
                                         rgba(59, 130, 246, 0.4));
            border-color: rgba(139, 92, 246, 0.6);
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(139, 92, 246, 0.3);
        }

        .stButton > button:active {
            transform: translateY(0);
        }

        /* Primary button override */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #7c3aed, #3b82f6);
            border: none;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
        }

        .stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #8b5cf6, #60a5fa);
            box-shadow: 0 8px 30px rgba(124, 58, 237, 0.5);
        }

        /* ═══════════════════════════════════════════════════════════
           FILE UPLOADER
           ═══════════════════════════════════════════════════════════ */

        .upload-zone {
            border: 2px dashed rgba(139, 92, 246, 0.3);
            border-radius: 16px;
            padding: 40px 20px;
            text-align: center;
            transition: all 0.3s ease;
            background: rgba(139, 92, 246, 0.03);
            cursor: pointer;
        }

        .upload-zone:hover {
            border-color: rgba(139, 92, 246, 0.6);
            background: rgba(139, 92, 246, 0.08);
        }

        /* ═══════════════════════════════════════════════════════════
           HEADERS
           ═══════════════════════════════════════════════════════════ */

        h1, h2, h3 {
            color: #e2e8f0 !important;
            font-weight: 700 !important;
        }

        h2 {
            font-size: 1.5rem !important;
            background: linear-gradient(135deg, #e2e8f0, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        h3 {
            font-size: 1.2rem !important;
            color: #cbd5e1 !important;
        }

        /* ═══════════════════════════════════════════════════════════
           TEXT & PARAGRAPHS
           ═══════════════════════════════════════════════════════════ */

        p {
            color: #94a3b8 !important;
        }

        /* ═══════════════════════════════════════════════════════════
           SELECTBOX & SLIDER
           ═══════════════════════════════════════════════════════════ */

        .stSelectbox > div > div {
            border-radius: 12px !important;
            border: 1px solid rgba(139, 92, 246, 0.2) !important;
            background: rgba(255, 255, 255, 0.05) !important;
            color: #e2e8f0 !important;
            transition: all 0.3s ease;
        }

        .stSelectbox > div > div:hover {
            border-color: rgba(139, 92, 246, 0.4) !important;
        }

        /* Slider styling */
        .stSlider .stSlider > div > div > div {
            background: linear-gradient(90deg, #7c3aed, #3b82f6) !important;
        }

        /* ═══════════════════════════════════════════════════════════
           SUCCESS / INFO MESSAGES
           ═══════════════════════════════════════════════════════════ */

        .stSuccess {
            background: rgba(16, 185, 129, 0.1) !important;
            border: 1px solid rgba(16, 185, 129, 0.3) !important;
            border-radius: 12px !important;
            padding: 12px 16px !important;
        }

        /* ═══════════════════════════════════════════════════════════
           SCROLLBAR
           ═══════════════════════════════════════════════════════════ */

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(10, 10, 26, 0.5);
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(139, 92, 246, 0.3);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(139, 92, 246, 0.5);
        }

        /* ═══════════════════════════════════════════════════════════
           DIVIDER
           ═══════════════════════════════════════════════════════════ */

        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent,
                                        rgba(139, 92, 246, 0.3), transparent);
            margin: 24px 0;
        }

        /* ═══════════════════════════════════════════════════════════
           ANIMATED BACKGROUND PARTICLES
           ═══════════════════════════════════════════════════════════ */

        .floating-particle {
            position: fixed;
            border-radius: 50%;
            pointer-events: none;
            opacity: 0.15;
            animation: float 20s infinite ease-in-out;
        }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) scale(1); }
            25% { transform: translate(100px, -100px) scale(1.1); }
            50% { transform: translate(-50px, -200px) scale(0.9); }
            75% { transform: translate(-150px, -50px) scale(1.05); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_color_palettes() -> dict:
    """Return a dictionary of color palettes for word clouds."""
    return {
        "Neon Purple": [
            "#8B5CF6", "#A78BFA", "#C4B5FD", "#7C3AED", "#6D28D9",
            "#DDD6FE", "#EDE9FE", "#F5F3FF",
        ],
        "Neon Blue": [
            "#3B82F6", "#60A5FA", "#93C5FD", "#2563EB", "#1D4ED8",
            "#BFDBFE", "#DBEAFE", "#EFF6FF",
        ],
        "Neon Green": [
            "#10B981", "#34D399", "#6EE7B7", "#059669", "#047857",
            "#A7F3D0", "#D1FAE5", "#ECFDF5",
        ],
        "Sunset Warm": [
            "#F59E0B", "#F97316", "#EF4444", "#EC4899", "#D946EF",
            "#FDE68A", "#FED7AA", "#FCE7F3", "#FAE8FF",
        ],
        "Ocean Cool": [
            "#06B6D4", "#0EA5E9", "#3B82F6", "#6366F1", "#8B5CF6",
            "#A5F3FC", "#BAE6FD", "#C7D2FE", "#DDD6FE",
        ],
        "Monochrome Dark": [
            "#F8FAFC", "#E2E8F0", "#CBD5E1", "#94A3B8", "#64748B",
            "#475569", "#334155", "#1E293B",
        ],
        "Fire Gradient": [
            "#DC2626", "#EA580C", "#D97706", "#F59E0B", "#FBBF24",
            "#FDE68A", "#FEF3C7", "#FFFBEB",
        ],
        "Aurora Borealis": [
            "#34D399", "#60A5FA", "#A78BFA", "#F472B6", "#38BDF8",
            "#818CF8", "#C084FC", "#FB7185",
        ],
    }