# Home.py
import streamlit as st
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Amit Kumar — BI & Analytics", 
    layout="wide", 
    page_icon="💼",
)

# Paths
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets"
RESUME_PATH = ASSETS_DIR / "Amit_Kumar_Resume.pdf"
PROFILE_PIC = ASSETS_DIR / "profile-pic.png"

# Custom CSS (same as before - keeping your existing styling)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&family=Inter:wght@400;600;700&display=swap');
[data-testid="stSidebar"] { display: none; }
section[data-testid="stSidebarNav"] { display: none; }
.main > div { padding-top: 0rem; }
.main { background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%); }
.stApp { background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%); }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
div[data-testid="stMarkdownContainer"] h1 { font-family: 'Space Mono', monospace; color: #f4c430; font-size: 3rem; margin-bottom: 0.5rem; letter-spacing: -1px; }
div[data-testid="stMarkdownContainer"] h2 { font-family: 'Space Mono', monospace; color: #f4c430; font-size: 2rem; margin-top: 2rem; margin-bottom: 1rem; letter-spacing: -0.5px; }
div[data-testid="stMarkdownContainer"] h3 { font-family: 'Inter', sans-serif; color: #64ffda; font-size: 1.4rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.5rem; }
div[data-testid="stMarkdownContainer"] h4 { font-family: 'Inter', sans-serif; color: #ffd700; font-size: 1.1rem; font-weight: 600; margin-top: 1rem; }
div[data-testid="stMarkdownContainer"] p { font-family: 'DM Sans', sans-serif; color: #ccd6f6; line-height: 1.8; font-size: 1.05rem; }
div[data-testid="stMetric"] { background: linear-gradient(135deg, rgba(244, 196, 48, 0.08) 0%, rgba(20, 27, 61, 0.4) 100%); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(244, 196, 48, 0.2); }
div[data-testid="stMetricLabel"] { font-family: 'Space Mono', monospace; color: #f4c430 !important; font-size: 0.9rem !important; font-weight: 700 !important; text-transform: uppercase; letter-spacing: 1px; }
div[data-testid="stMetricValue"] { font-family: 'Space Mono', monospace; color: #ffffff !important; font-size: 2rem !important; font-weight: 700 !important; }
div[data-testid="stMetricDelta"] { font-family: 'DM Sans', sans-serif; color: #a8b2d1 !important; font-size: 0.85rem !important; }
.stDownloadButton button { background: linear-gradient(135deg, #f4c430 0%, #ffd700 100%); color: #0a0e27 !important; font-family: 'Space Mono', monospace; font-weight: 700 !important; border: none; padding: 0.75rem 2rem; border-radius: 8px; font-size: 1rem; transition: all 0.3s ease; }
.stDownloadButton button:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(244, 196, 48, 0.4); background: #ffd700; }
.stDownloadButton button p { color: #0a0e27 !important; font-weight: 700 !important; }
.stButton button { background: transparent; color: #ccd6f6; border: none; font-family: 'DM Sans', sans-serif; font-size: 1rem; font-weight: 500; padding: 0.6rem 1.5rem; border-radius: 6px; transition: all 0.3s ease; position: relative; }
.stButton button:hover { color: #f4c430; background: rgba(244, 196, 48, 0.1); transform: translateY(-2px); }
div[data-testid="stAlert"] { background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%); border: 1px solid rgba(244, 196, 48, 0.3); border-radius: 12px; font-family: 'DM Sans', sans-serif; }
.stCaption { font-family: 'Inter', sans-serif; color: #8892b0 !important; font-size: 0.9rem !important; }
a { color: #64ffda; text-decoration: none; }
a:hover { color: #ffd700; text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

# Top Navigation
nav_cols = st.columns(5)
with nav_cols[0]:
    if st.button("Home", key="nav0", use_container_width=True):
        st.switch_page("Home.py")
with nav_cols[1]:
    if st.button("Industry Cases", key="nav1", use_container_width=True):
        st.switch_page("pages/1_Industry_Case_Studies.py")
with nav_cols[2]:
    if st.button("Projects", key="nav2", use_container_width=True):
        st.switch_page("pages/2_Personal_Projects.py")
with nav_cols[3]:
    if st.button("Research", key="nav3", use_container_width=True):
        st.switch_page("pages/3_Research.py")
with nav_cols[4]:
    if st.button("Contact", key="nav4", use_container_width=True):
        st.switch_page("pages/4_Contact.py")

st.markdown("<div style='margin: 1rem 0;'></div>", unsafe_allow_html=True)

# Resume download
def resume_download_button():
    try:
        with open(RESUME_PATH, "rb") as f:
            st.download_button("Download Resume", f.read(), "Amit_Kumar_Resume.pdf", use_container_width=True)
    except:
        st.warning("Resume not found")

# Hero Section — smaller photo column
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    try:
        from PIL import Image
        st.image(Image.open(PROFILE_PIC), use_column_width=True)
    except:
        st.image("https://via.placeholder.com/400x400/0a0e27/f4c430?text=AK", use_column_width=True)
    resume_download_button()

with col2:
    st.markdown("# Amit Kumar")
    st.markdown("## Data & BI Analyst | Pipelines · Dashboards · Automation")
    st.markdown("""
    Data and BI Analyst with 2.5 years of full-time professional experience plus current analytics 
    roles at Deutsche Börse Group. PL-300 certified, building production Power BI dashboards, 
    statistical models, and Python automation for executive stakeholders across financial services 
    and infrastructure. **Available full-time from May 2026.**
    """)
    st.markdown("#### Core Skills")
    st.write("Power BI (PL-300) | SQL | Python | Databricks | R | Excel | ETL | Automation")
    st.markdown("#### Certifications")
    st.write("PL-300 Power BI Data Analyst Assocaite | Databricks Certified Data Engineer Associate | AZ-900 Azure | AB-730 AI Business Professional")
    st.markdown("#### Contact")
    st.write("📍 Frankfurt am Main, Germany — Open to relocation anywhere in Germany")
    st.write("✉️ amit.kumar.analytics.eu@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/amit1820) | [GitHub](https://github.com/amit1820)")

st.markdown("---")

st.markdown("## Professional Impact")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Clearing Members", "200+", "Across 22 countries")
with col2:
    st.metric("Rows Automated", "500K+/month", "Data reconciliation")
with col3:
    st.metric("Time Saved", "20+ hrs/month", "Process automation")
with col4:
    st.metric("Error Reduction", "50%+", "Automation workflows")

st.markdown("---")

st.markdown("## Current Role")
st.info("""
**Business Analytics, Market & Liquidity Analytics (Internship)** at **Eurex Clearing AG (Deutsche Börse Group)** | January 2026 - Present

Designing Power BI dashboards for 200+ clearing members, developing statistical outlier detection models,
building centralized Databricks data models, and producing published market intelligence reports.
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Key Projects")
    st.write("• Interactive Power BI dashboards for 200+ clearing members across 22 countries")
    st.write("• Python-based outlier detection model on live HDFS data for collateral fee analysis")
    st.write("• Centralized Databricks data models as single-source analytics layer")
    st.write("• Monthly derivatives performance report for Eurex sales team")
with col2:
    st.markdown("#### Focus Areas")
    st.write("• KPI frameworks for derivatives performance tracking across 10+ product categories")
    st.write("• Market intelligence reports published on Eurex website")
    st.write("• Statistical modelling for collateral fee trend analysis")
    st.write("• Data pipeline automation using Python, SQL, and VBA")

st.markdown("---")

st.markdown("## Career Journey")

timeline_data = [
    ("Jan 2026 - Present", "Eurex Clearing AG (Deutsche Börse Group)", "Business Analytics, Market & Liquidity Analytics (Internship)", "Power BI dashboards for 200+ members, outlier detection model, Databricks data models, published market intelligence"),
    ("July 2025 - Dec 2025", "Deutsche Börse AG", "Data Analytics, Cash Market Services (Working Student)", "Real-time trading dashboards, Power Automate workflows, 500K+ row reconciliation, computer vision verification tool"),
    ("Aug 2022 - July 2024", "Arcadis", "Data & Analytics Consultant, BIM Analytics", "Power BI dashboards for HS2 (UK £100B+ rail programme), Python automation, cross-functional reporting"),
    ("Feb 2022 - July 2022", "Alliant Advisory", "Associate, Cost Segregation Analytics", "Financial data analysis, Excel automation, standardized reporting"),
    ("Jan 2021 - Jan 2022", "Atal Incubation Centre", "Program Associate, Entrepreneurship Cell (Internship)", "MySQL databases, SQL workflows, data quality improvement"),
]

for period, company, role, highlights in timeline_data:
    with st.expander(f"**{company}** — {role}"):
        st.caption(period)
        st.write(highlights)

st.markdown("---")

st.markdown("## Featured Work")
col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown("#### Statistical Outlier Detection Model")
    st.caption("Eurex Clearing AG | Jan 2026 - Present")
    st.write("""
    Developing Python-based outlier detection model (SciPy, Statsmodels) on live HDFS data to 
    identify anomalous collateral fee trends across 200+ Eurex clearing members — analyzing 
    securities collateral and add-on fee patterns to surface key drivers behind fee changes.
    """)
    st.caption("**Tech Stack:** Python, SciPy, Statsmodels, HDFS, Apache Zeppelin")

with col2:
    st.markdown("#### Computer Vision Document Verification")
    st.caption("Deutsche Börse AG | July 2025 - Dec 2025")
    st.write("""
    Developed automated verification tool using Python (OpenCV, PyMuPDF) to detect stamps and 
    signatures in 400+ monthly compliance PDFs. Reduced manual review effort significantly.
    """)
    st.caption("**Tech Stack:** Python, OpenCV, PyMuPDF")

st.markdown("---")

st.markdown("## Education")
col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown("#### Master of Science in Management")
    st.write("**Frankfurt School of Finance & Management**")
    st.write("Sept 2024 - Aug 2026 | Grade: 2.0 (German Scale, 1.0 = Best)")
    st.caption("Concentration: Digital Business, Technology & Operations (DBTO)")
    st.caption("Thesis: Climate Policy Reversal and Global Equity Markets — Cross-Country Event Study in R")
with col2:
    st.markdown("#### Bachelor of Engineering")
    st.write("**Bangalore Institute of Technology, India**")
    st.write("Civil Engineering | Aug 2017 - Aug 2021")
    st.caption("Grade: 8.03/10 ≈ 2.0 (German equivalent)")

st.markdown("---")

st.markdown("## Leadership & Activities")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### FS Quant Data Science – Trader Team")
    st.caption("Frankfurt School | Aug 2025 - Present")
    st.write("Researching markets, developing trading strategies, and practicing risk-aware execution")

with col2:
    st.markdown("#### FS Blockchain – Tokenized Assets Team")
    st.caption("Frankfurt School | Apr 2025 - Present")
    st.write("Contributing to research on blockchain innovation and tokenized asset markets")

st.markdown("---")
st.caption("Portfolio built with Streamlit | Updated April 2026")
