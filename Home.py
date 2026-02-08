# app.py
import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Amit Kumar — BI & Analytics", 
    layout="wide", 
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Paths
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets"
RESUME_PATH = ASSETS_DIR / "Amit_Kumar_Resume.pdf"
PROFILE_PIC = ASSETS_DIR / "profile-pic.png"

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');

/* Main background */
.main {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

/* Hide default page names and show custom labels */
section[data-testid="stSidebarNav"] li:first-child {
    display: none;
}

section[data-testid="stSidebarNav"]::before {
    content: "Home";
    margin-left: 1rem;
    margin-top: 1rem;
    font-size: 1rem;
    color: #f4c430;
    font-family: 'Space Mono', monospace;
    font-weight: 700;
    display: block;
    padding: 0.5rem;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1729 0%, #141b3d 100%);
}

section[data-testid="stSidebarNav"] a {
    color: #ccd6f6;
    font-family: 'DM Sans', sans-serif;
}

section[data-testid="stSidebarNav"] a:hover {
    color: #f4c430;
}

/* Typography */
div[data-testid="stMarkdownContainer"] h1 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

div[data-testid="stMarkdownContainer"] h2 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
    font-size: 2rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

div[data-testid="stMarkdownContainer"] h3 {
    font-family: 'Space Mono', monospace;
    color: #a8b2d1;
    font-size: 1.3rem;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}

div[data-testid="stMarkdownContainer"] h4 {
    font-family: 'Space Mono', monospace;
    color: #8892b0;
    font-size: 1rem;
    margin-top: 1rem;
}

div[data-testid="stMarkdownContainer"] p {
    font-family: 'DM Sans', sans-serif;
    color: #ccd6f6;
    line-height: 1.8;
    font-size: 1.05rem;
}

/* Metric cards with better colors */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.08) 0%, rgba(20, 27, 61, 0.4) 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid rgba(244, 196, 48, 0.2);
}

div[data-testid="stMetricLabel"] {
    font-family: 'Space Mono', monospace;
    color: #f4c430 !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

div[data-testid="stMetricValue"] {
    font-family: 'Space Mono', monospace;
    color: #ffffff !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricDelta"] {
    font-family: 'DM Sans', sans-serif;
    color: #a8b2d1 !important;
    font-size: 0.85rem !important;
}

/* FIXED: Download button with dark text on yellow background */
.stDownloadButton button {
    background: linear-gradient(135deg, #f4c430 0%, #ffd700 100%);
    color: #0a0e27 !important;
    font-family: 'Space Mono', monospace;
    font-weight: 700 !important;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 8px;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.stDownloadButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(244, 196, 48, 0.4);
    background: #ffd700;
}

.stDownloadButton button p {
    color: #0a0e27 !important;
    font-weight: 700 !important;
}

/* Info box styling */
div[data-testid="stAlert"] {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    border: 1px solid rgba(244, 196, 48, 0.3);
    border-radius: 12px;
    font-family: 'DM Sans', sans-serif;
}

/* Caption styling */
.stCaption {
    font-family: 'Space Mono', monospace;
    color: #8892b0 !important;
}

/* Links */
a {
    color: #f4c430;
    text-decoration: none;
}

a:hover {
    color: #ffd700;
    text-decoration: underline;
}

/* Navigation buttons */
.stButton button {
    background: rgba(244, 196, 48, 0.1);
    color: #f4c430;
    border: 1px solid rgba(244, 196, 48, 0.3);
    font-family: 'Space Mono', monospace;
    font-weight: 600;
    padding: 0.6rem 1.5rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.stButton button:hover {
    background: rgba(244, 196, 48, 0.2);
    border-color: #f4c430;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# Resume download helper
def resume_download_button():
    try:
        with open(RESUME_PATH, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            "Download Resume",
            data=pdf_bytes,
            file_name="Amit_Kumar_Resume.pdf",
            use_container_width=True
        )
    except FileNotFoundError:
        st.warning("Resume file not found. Add Amit_Kumar_Resume.pdf to assets/ directory.")

# Hero Section
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    try:
        from PIL import Image
        img = Image.open(PROFILE_PIC)
        st.image(img, use_column_width=True)
    except:
        st.image("https://via.placeholder.com/400x400/0a0e27/f4c430?text=AK", use_column_width=True)
    
    # Download button under photo
    resume_download_button()

with col2:
    st.markdown("# Amit Kumar")
    st.markdown("### Business Intelligence & Analytics")
    
    st.markdown("""
    Business Intelligence Analyst with 3+ years of experience designing dashboards, automating 
    reporting pipelines, and delivering data-driven insights across financial markets and enterprise 
    operations. Strong expertise in Power BI, SQL, Python, with proven experience translating business 
    requirements into scalable BI solutions.
    """)
    
    st.markdown("#### Core Skills")
    st.write("Power BI | SQL | Python | Excel | ETL | Data Visualization | Automation")
    
    st.markdown("#### Contact")
    st.write("📍 Frankfurt am Main, Germany")
    st.write("✉️ amit.kumar.analytics.eu@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/amit1820) | [GitHub](https://github.com/amit1820)")

st.markdown("---")

# Key Metrics with improved labels
st.markdown("## Professional Impact")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Experience", "3+ Years", "BI & Analytics")

with col2:
    st.metric("Rows Automated", "500K+/month", "Data reconciliation")

with col3:
    st.metric("Time Saved", "20+ hrs/month", "Process automation")

with col4:
    st.metric("Error Reduction", "50%+", "Automation workflows")

st.markdown("---")

# Current Role - Highlight box
st.markdown("## Current Role")

st.info("""
**Intern - Business Analytics** at **Eurex (Deutsche Börse Group)** | January 2026 - Present

Working on Power BI dashboards for commercial sales, automating BAU tasks with Python and VBA, 
and extracting trading data using SQL across derivatives products.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Key Responsibilities")
    st.write("• Designing Power BI dashboards for commercial sales team")
    st.write("• Automating recurring tasks using Python and VBA")
    st.write("• Extracting trading data from StatistiX database using SQL")
    st.write("• Supporting market analytics and pricing analysis")

with col2:
    st.markdown("#### Focus Areas")
    st.write("• Client performance tracking across derivatives products")
    st.write("• Most Liquid Products lists and interactive charts")
    st.write("• Product presentations for TRF, FTSE 100, ESG segments")
    st.write("• Monthly market analytics newsletters")

st.markdown("---")

# Featured Work
st.markdown("## Featured Work")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### Computer Vision Document Verification")
    st.caption("Deutsche Börse AG | July 2025 - Dec 2025")
    st.write("""
    Developed automated verification tool using Python (OpenCV, PyMuPDF) to detect stamps and 
    signatures in 400+ monthly compliance PDFs. Reduced manual review time by 50%+ and flagged 
    exceptions for human review.
    """)
    st.caption("**Tech Stack:** Python, OpenCV, PyMuPDF")
    
    # Metrics for this project
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.metric("Documents", "400+/month", "Automated")
    with subcol2:
        st.metric("Time Saved", "50%+", "Manual review")

with col2:
    st.markdown("### Real-Time Trading Dashboards")
    st.caption("Deutsche Börse AG | July 2025 - Dec 2025")
    st.write("""
    Designed and deployed live Power BI dashboards integrating Scala and Apache Zeppelin data sources. 
    Dashboards replaced ad-hoc report requests and provide traders with self-service analytics that 
    they actually check daily.
    """)
    st.caption("**Tech Stack:** Power BI, Apache Zeppelin, Scala, SQL")
    
    # Metrics for this project
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.metric("Adoption", "Daily", "Trader usage")
    with subcol2:
        st.metric("Requests", "Reduced", "Ad-hoc reports")

st.markdown("---")

# Education
st.markdown("## Education")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### Master of Science in Management")
    st.write("**Frankfurt School of Finance & Management**")
    st.write("CGPA: 2.1/4.0 (German scale) | Sept 2024 - Aug 2026")
    st.caption("Concentration: Digital Business, Technology & Operations (DBTO)")
    st.caption("Relevant Coursework: AI & Operations, Data Science, Financial Analysis")

with col2:
    st.markdown("### Bachelor of Engineering")
    st.write("**Bangalore Institute of Technology, India**")
    st.write("Civil Engineering | CGPA: 8.03/10 | Aug 2017 - Aug 2021")

st.markdown("---")

# Navigation call-to-action
st.markdown("## Explore This Portfolio")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Industry Case Studies")
    st.write("Production work at Deutsche Börse Group and Arcadis")

with col2:
    st.markdown("#### Personal Projects")
    st.write("Independent analytics projects and GitHub repositories")

with col3:
    st.markdown("#### Research")
    st.write("Master's thesis on supply chain ESG performance")

st.markdown("---")

st.caption("Portfolio built with Streamlit | Updated February 2026")
