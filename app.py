# app.py
import streamlit as st
from pathlib import Path
from PIL import Image

# Page config
st.set_page_config(page_title="Amit Kumar — BI & Analytics", layout="wide", page_icon=":bar_chart:")

# Paths
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets"
RESUME_PATH = ASSETS_DIR / "Amit_Kumar_Resume.pdf"
PROFILE_PIC = ASSETS_DIR / "profile-pic.png"

# Helper: show resume download
def resume_download_button(resume_path):
    try:
        with open(resume_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button("Download Résumé", data=pdf_bytes, file_name="Amit_Kumar_Resume.pdf")
    except FileNotFoundError:
        st.warning("Resume not found in assets/. Add Amit_Kumar_Resume.pdf to enable download.")

# Hero
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            img = Image.open(PROFILE_PIC)
            st.image(img, width=260)
        except Exception:
            st.image("https://via.placeholder.com/260x260.png?text=Profile+Pic", width=260)
    with col2:
        st.markdown("<h1 style='margin-bottom:0.2rem;'>Amit Kumar</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top:0;'>Business Intelligence & Analytics | Data Analyst</h4>", unsafe_allow_html=True)
        st.markdown(
            """
            I design analytics and automation solutions that transform fragmented, manual reporting into decision-ready insights.
            My experience spans financial markets, operational analytics, and BI automation — with a focus on dashboards and data pipelines stakeholders actually use.
            """,
            unsafe_allow_html=True,
        )
        resume_download_button(RESUME_PATH)
        st.markdown(
            "📍 Frankfurt am Main, Germany  •  🔗 [GitHub](https://github.com/amit1820)  •  🔗 [LinkedIn](https://www.linkedin.com/in/amit1820)"
        )

st.markdown("---")
st.markdown(
    """
    **Featured:** production-grade automation for compliance documents, real-time trading dashboards, reconciliation systems.
    Use the left navigation (or the pages menu) to explore Industry Case Studies, Personal Projects, and Research.
    """,
    unsafe_allow_html=True,
)
