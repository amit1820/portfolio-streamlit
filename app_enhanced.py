# app_enhanced.py
import streamlit as st
from pathlib import Path
from PIL import Image

# Page config
st.set_page_config(
    page_title="Amit Kumar — BI & Analytics Portfolio", 
    layout="wide", 
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Paths
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets"
RESUME_PATH = ASSETS_DIR / "Amit_Kumar_Resume.pdf"
PROFILE_PIC = ASSETS_DIR / "profile-pic.png"

# Load custom CSS
def load_css():
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');
    
    /* Global Styles */
    .main {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
    }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #141b3d 0%, #0f1729 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        border: 1px solid rgba(244, 196, 48, 0.2);
        box-shadow: 0 8px 32px rgba(244, 196, 48, 0.1);
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-family: 'Space Mono', monospace;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #f4c430 0%, #ffd700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -2px;
    }
    
    .hero-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.4rem;
        color: #a8b2d1;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    
    .hero-description {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.1rem;
        line-height: 1.8;
        color: #8892b0;
        max-width: 800px;
        margin-bottom: 2rem;
    }
    
    /* Stats Cards */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: rgba(244, 196, 48, 0.05);
        border: 1px solid rgba(244, 196, 48, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(244, 196, 48, 0.2);
        border-color: #f4c430;
    }
    
    .stat-number {
        font-family: 'Space Mono', monospace;
        font-size: 2.5rem;
        font-weight: 700;
        color: #f4c430;
        display: block;
    }
    
    .stat-label {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.9rem;
        color: #a8b2d1;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.5rem;
    }
    
    /* Feature Badges */
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin: 1.5rem 0;
    }
    
    .skill-badge {
        font-family: 'Space Mono', monospace;
        background: rgba(244, 196, 48, 0.1);
        color: #f4c430;
        padding: 0.5rem 1.2rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid rgba(244, 196, 48, 0.3);
        transition: all 0.3s ease;
    }
    
    .skill-badge:hover {
        background: rgba(244, 196, 48, 0.2);
        transform: scale(1.05);
    }
    
    /* CTA Buttons */
    .cta-container {
        display: flex;
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .cta-primary {
        font-family: 'DM Sans', sans-serif;
        background: #f4c430;
        color: #0a0e27;
        padding: 1rem 2rem;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    
    .cta-primary:hover {
        background: #ffd700;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(244, 196, 48, 0.4);
    }
    
    .cta-secondary {
        font-family: 'DM Sans', sans-serif;
        background: transparent;
        color: #f4c430;
        padding: 1rem 2rem;
        border-radius: 8px;
        font-weight: 700;
        border: 2px solid #f4c430;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .cta-secondary:hover {
        background: rgba(244, 196, 48, 0.1);
        transform: translateY(-2px);
    }
    
    /* Contact Links */
    .contact-link {
        color: #8892b0;
        text-decoration: none;
        transition: color 0.3s ease;
        font-family: 'DM Sans', sans-serif;
    }
    
    .contact-link:hover {
        color: #f4c430;
    }
    
    /* Highlight Section */
    .highlight-box {
        background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(244, 196, 48, 0.05) 100%);
        border-left: 4px solid #f4c430;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 2rem 0;
    }
    
    .highlight-text {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.1rem;
        color: #ccd6f6;
        line-height: 1.6;
    }
    
    /* Animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate-in {
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1729 0%, #141b3d 100%);
    }
    
    /* Remove default Streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Helper: show resume download
def resume_download_button(resume_path):
    try:
        with open(resume_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            "📄 Download Resume",
            data=pdf_bytes,
            file_name="Amit_Kumar_Resume.pdf",
            use_container_width=True
        )
    except FileNotFoundError:
        st.warning("Resume not found in assets/. Add Amit_Kumar_Resume.pdf to enable download.")

# Load CSS
load_css()

# Hero Section
st.markdown('<div class="hero-container animate-in">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    try:
        img = Image.open(PROFILE_PIC)
        st.image(img, use_column_width=True)
    except Exception:
        st.image("https://via.placeholder.com/400x400/0a0e27/f4c430?text=AK", use_column_width=True)

with col2:
    st.markdown('<h1 class="hero-title">Amit Kumar</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Business Intelligence & Analytics Engineer</p>', unsafe_allow_html=True)
    
    st.markdown('''
    <p class="hero-description">
    I transform fragmented data into decision-ready insights through automation and analytics. 
    Currently at Deutsche Börse Group, building real-time dashboards and automating workflows 
    that stakeholders actually use — replacing static reports with interactive, actionable intelligence.
    </p>
    ''', unsafe_allow_html=True)
    
    # Key skills badges
    st.markdown('<div class="badge-container">', unsafe_allow_html=True)
    skills = ["Power BI", "Python", "SQL", "ETL", "Automation", "Dashboard Design"]
    for skill in skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # CTA Buttons
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        resume_download_button(RESUME_PATH)
    with col_btn2:
        st.markdown(
            '<a href="mailto:amit.kumar.analytics.eu@gmail.com" class="cta-secondary" style="display: block; text-align: center; padding: 0.75rem;">💬 Get in Touch</a>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# Stats Section
st.markdown('<div class="stats-container">', unsafe_allow_html=True)

stats = [
    {"number": "3+", "label": "Years Experience"},
    {"number": "80%", "label": "Time Saved via Automation"},
    {"number": "500K+", "label": "Rows Reconciled Monthly"},
    {"number": "20+", "label": "Hours Saved/Month"}
]

cols = st.columns(4)
for i, stat in enumerate(stats):
    with cols[i]:
        st.markdown(f'''
        <div class="stat-card">
            <span class="stat-number">{stat["number"]}</span>
            <span class="stat-label">{stat["label"]}</span>
        </div>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Highlight Section
st.markdown('''
<div class="highlight-box">
    <p class="highlight-text">
    <strong>🎯 Current Focus:</strong> Building production-grade BI solutions at Eurex (Deutsche Börse Group) — 
    Power BI dashboards for commercial teams, automated analytics pipelines, and data transformation workflows 
    that eliminate manual Excel extraction across multiple trading systems.
    </p>
</div>
''', unsafe_allow_html=True)

# Featured Projects Preview
st.markdown("---")
st.markdown("## 🚀 Featured Work")

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    <div style="background: rgba(244, 196, 48, 0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(244, 196, 48, 0.2);">
        <h3 style="color: #f4c430; font-family: 'Space Mono', monospace;">🤖 AI Document Verification</h3>
        <p style="color: #8892b0; font-family: 'DM Sans', sans-serif;">Automated validation of 400+ compliance PDFs/month using OpenCV and OCR — reduced manual review by 80%.</p>
        <p style="color: #f4c430; font-family: 'Space Mono', monospace; font-size: 0.9rem;">Python • OpenCV • Tesseract</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div style="background: rgba(244, 196, 48, 0.05); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(244, 196, 48, 0.2);">
        <h3 style="color: #f4c430; font-family: 'Space Mono', monospace;">📊 Real-Time Trading Dashboards</h3>
        <p style="color: #8892b0; font-family: 'DM Sans', sans-serif;">Live Power BI dashboards with Apache Zeppelin integration — dashboards traders actually check daily.</p>
        <p style="color: #f4c430; font-family: 'Space Mono', monospace; font-size: 0.9rem;">Power BI • Scala • SQL</p>
    </div>
    ''', unsafe_allow_html=True)

# Navigation
st.markdown("---")
st.markdown('''
<div style="text-align: center; padding: 2rem;">
    <p style="font-family: 'DM Sans', sans-serif; font-size: 1.1rem; color: #a8b2d1;">
    👈 <strong>Explore the sidebar</strong> to dive into Industry Case Studies, Personal Projects, Research, and Contact information.
    </p>
</div>
''', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('''
<div style="text-align: center; padding: 1rem;">
    <p style="font-family: 'DM Sans', sans-serif; color: #8892b0;">
    📍 Frankfurt am Main, Germany | 
    <a href="https://github.com/amit1820" class="contact-link">GitHub</a> | 
    <a href="https://www.linkedin.com/in/amit1820" class="contact-link">LinkedIn</a> | 
    <a href="mailto:amit.kumar.analytics.eu@gmail.com" class="contact-link">Email</a>
    </p>
</div>
''', unsafe_allow_html=True)
