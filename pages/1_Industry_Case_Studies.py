# pages/1_Industry_Case_Studies.py
import streamlit as st

st.set_page_config(page_title="Industry Case Studies", layout="wide", page_icon="💼")

# Custom CSS for professional styling
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
    font-size: 1.5rem;
}

div[data-testid="stMarkdownContainer"] h3 {
    font-family: 'Space Mono', monospace;
    color: #8892b0;
    font-size: 1.1rem;
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

# Page Title
st.title("Industry Case Studies")
st.markdown("""
**Professional work at Deutsche Börse Group and Arcadis**  
Production analytics solutions, automation pipelines, and real-time dashboards deployed in financial markets and enterprise operations.
""")

st.markdown("---")

# Project 1: Computer Vision Document Verification
st.subheader("Computer Vision-Based Document Verification")
st.markdown("**Deutsche Börse AG** | July 2025 - Dec 2025")
st.caption("Python, OpenCV, PyMuPDF")

st.markdown("**Context**")
st.write("""
Compliance team manually verified 400+ regulatory PDFs each month for stamps and signatures. 
Manual process took 2-3 minutes per document and was prone to visual fatigue errors.
""")

st.markdown("**Solution**")
st.write("""
Developed computer vision-based verification tool using Python with OpenCV for stamp detection 
and PyMuPDF for document processing. System automatically detects required elements and flags 
exceptions for manual review.
""")

st.markdown("**Impact**")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Documents/Month", "400+", "Automated")
with col2:
    st.metric("Time Saved", "20+ hrs/month", "50%+ reduction")
with col3:
    st.metric("Error Reduction", "50%+", "Manual errors")

st.markdown("---")

# Project 2: Power Automate Workflows
st.subheader("Power Automate Workflows for Cash Market Operations")
st.markdown("**Deutsche Börse AG** | July 2025 - Dec 2025")
st.caption("Power Automate, AI Builder, Power Query, VBA")

st.markdown("**Context**")
st.write("""
Cash market operations involved manual file processing and data entry across multiple systems. 
Repetitive tasks consumed significant analyst time and introduced manual errors.
""")

st.markdown("**Solution**")
st.write("""
Engineered rule-based automation workflows using Power Automate with AI Builder for content recognition. 
Automated reconciliation of 500K+ rows/month using Power Query and VBA, resolving inconsistent date 
formats and field mappings across upstream trading systems.
""")

st.markdown("**Impact**")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rows Reconciled", "500K+/month", "Automated")
with col2:
    st.metric("Time Saved", "20+ hrs/month", "Workflow automation")
with col3:
    st.metric("Data Defects", "30% reduction", "Quality improvement")

st.markdown("---")

# Project 3: Real-Time Trading Dashboards
st.subheader("Real-Time Trading Analytics Dashboards")
st.markdown("**Deutsche Börse AG** | July 2025 - Dec 2025")
st.caption("Power BI, Apache Zeppelin, Scala, SQL")

st.markdown("**Context**")
st.write("""
Traders relied on static reports and ad-hoc data requests for analytics. No unified view of 
trading KPIs led to information fragmentation and delayed decision-making.
""")

st.markdown("**Solution**")
st.write("""
Designed and deployed live Power BI dashboards integrating Scala and Apache Zeppelin data sources 
for real-time trading analytics. Dashboards replaced ad-hoc report requests and provide traders 
with self-service access to key metrics.
""")

st.markdown("**Impact**")
col1, col2 = st.columns(2)
with col1:
    st.metric("Adoption Rate", "Daily usage", "Traders actually check dashboards")
with col2:
    st.metric("Ad-hoc Requests", "Significant reduction", "Self-service analytics")

st.markdown("---")

# Project 4: Power BI Dashboards at Arcadis
st.subheader("Power BI Dashboards for Project KPI Tracking")
st.markdown("**Arcadis** | Aug 2022 - July 2024")
st.caption("Power BI, Power Apps, Python, VBA")

st.markdown("**Context**")
st.write("""
Project teams needed real-time visibility into KPIs and resource allocation. 
Manual reporting processes created delays in project tracking and decision-making.
""")

st.markdown("**Solution**")
st.write("""
Built Power BI dashboards and Power Apps for real-time project KPI tracking and resource management. 
Automated data validation and transformation pipelines using Python, VBA, and Dynamo.
""")

st.markdown("**Impact**")
col1, col2 = st.columns(2)
with col1:
    st.metric("Processing Time", "60% reduction", "Manual work eliminated")
with col2:
    st.metric("Approval Time", "2 days saved", "Per project")

st.markdown("---")

# Project 5: Current Work at Eurex
st.subheader("Power BI Dashboard for Commercial Sales Team")
st.markdown("**Eurex (Deutsche Börse Group)** | Jan 2026 - Present")
st.caption("Power BI, SQL, Python, VBA")

st.markdown("**Context**")
st.write("""
Commercial sales team tracked client performance using static Excel reports that were rarely updated. 
Manual data extraction from StatistiX database required significant analyst time.
""")

st.markdown("**Solution**")
st.write("""
Designing and deploying Power BI dashboard to track client performance across derivatives products. 
Automating recurring BAU tasks using Python and VBA, including Most Liquid Products lists and 
interactive chart updates. Extracting and structuring trading data using SQL across TRF, FTSE 100, 
and ESG segments.
""")

st.markdown("**Impact**")
st.info("Project in progress - replacing static Excel reports with interactive Power BI dashboards")

st.markdown("---")

st.caption("All projects deployed in production at Deutsche Börse Group and Arcadis")
