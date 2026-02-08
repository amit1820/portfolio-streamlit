# app.py
import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Amit Kumar — BI & Analytics Portfolio", 
    layout="wide", 
    page_icon="📊"
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

.main {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

div[data-testid="stMarkdownContainer"] h1 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
}

div[data-testid="stMarkdownContainer"] h2 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
}

div[data-testid="stMarkdownContainer"] h3 {
    font-family: 'Space Mono', monospace;
    color: #8892b0;
}

div[data-testid="stMarkdownContainer"] p {
    font-family: 'DM Sans', sans-serif;
    color: #ccd6f6;
    line-height: 1.7;
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
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
col1, col2 = st.columns([1, 2])

with col1:
    try:
        from PIL import Image
        img = Image.open(PROFILE_PIC)
        st.image(img, width=280)
    except:
        st.image("https://via.placeholder.com/280x280/0a0e27/f4c430?text=AK", width=280)

with col2:
    st.title("Amit Kumar")
    st.subheader("Business Intelligence & Analytics")
    
    st.markdown("""
    Business Intelligence Analyst with 3+ years of experience designing dashboards, automating 
    reporting pipelines, and delivering data-driven insights across financial markets and enterprise 
    operations. Strong expertise in Power BI, SQL, Python, with proven experience translating business 
    requirements into scalable BI solutions.
    """)
    
    # Skills
    st.markdown("**Core Skills**")
    st.write("Power BI | SQL | Python | Excel | ETL | Data Visualization | Automation")
    
    # Resume download
    resume_download_button()
    
    st.markdown("**Contact**")
    st.write("📍 Frankfurt am Main, Germany")
    st.write("✉️ amit.kumar.analytics.eu@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/amit1820) | [GitHub](https://github.com/amit1820)")

st.markdown("---")

# Key Metrics
st.subheader("Professional Impact")

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

# Current Role
st.subheader("Current Role")
st.markdown("**Intern - Business Analytics** | Eurex (Deutsche Börse Group) | Jan 2026 - Present")

st.write("""
- Designing and deploying Power BI dashboard for commercial sales team to track client performance 
  across derivatives products
- Automating recurring BAU tasks using Python and VBA, including Most Liquid Products lists and 
  interactive chart updates
- Extracting and structuring trading data from StatistiX database using SQL for product presentations 
  across TRF, FTSE 100, and ESG segments
- Supporting ad-hoc market analytics and pricing analysis for Market Maker schemes
- Producing monthly market analytics newsletters and client reporting deliverables
""")

st.markdown("---")

# Featured Work
st.subheader("Featured Work")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Computer Vision Document Verification**")
    st.caption("Deutsche Börse AG")
    st.write("""
    Developed automated verification tool using Python (OpenCV, PyMuPDF) to detect stamps and 
    signatures in 400+ monthly compliance PDFs. Reduced manual review time by 50%+ and flagged 
    exceptions for human review.
    """)
    st.caption("Python, OpenCV, PyMuPDF")

with col2:
    st.markdown("**Real-Time Trading Dashboards**")
    st.caption("Deutsche Börse AG")
    st.write("""
    Designed and deployed live Power BI dashboards integrating Scala and Apache Zeppelin data sources. 
    Dashboards replaced ad-hoc report requests and provide traders with self-service analytics that 
    they actually check daily.
    """)
    st.caption("Power BI, Apache Zeppelin, Scala, SQL")

st.markdown("---")

# Education
st.subheader("Education")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Master of Science in Management**")
    st.write("Frankfurt School of Finance & Management")
    st.write("CGPA: 2.1/4.0 | Sept 2024 - Aug 2026")
    st.caption("Concentration: Digital Business, Technology & Operations")

with col2:
    st.markdown("**Bachelor of Engineering in Civil Engineering**")
    st.write("Bangalore Institute of Technology")
    st.write("CGPA: 8.03/10 | Aug 2017 - Aug 2021")

st.markdown("---")

# Navigation
st.info("""
**Explore this portfolio:**  
Use the sidebar to navigate to Industry Case Studies, Personal Projects, Research, and Contact pages.
""")

st.markdown("---")

st.caption("Portfolio built with Streamlit | Updated February 2026")
