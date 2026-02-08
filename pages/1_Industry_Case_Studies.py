# pages/1_Industry_Case_Studies.py
import streamlit as st

st.set_page_config(page_title="Industry Case Studies", layout="wide")

# Custom CSS - using st.markdown with proper syntax
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
    color: #f4c430;
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
st.title("💼 Industry & Professional Case Studies")
st.markdown("""
Production-ready analytics solutions deployed at Deutsche Börse Group and Arcadis. 
These projects showcase hands-on delivery of automation pipelines, real-time dashboards, 
and data workflows that eliminated manual processes and improved decision-making velocity.
""")

st.markdown("---")

# Project 1: AI Document Verification
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("AI-Powered Document Verification System")
    st.caption("Python · OpenCV · OCR · Computer Vision")
with col2:
    st.success("COMPLETED")

st.markdown("##### Problem")
st.write("""
The compliance team manually verified ~400 regulatory PDFs each month for required stamps, 
signatures, and certifications. This manual process was time-intensive (2-3 minutes per document), 
error-prone due to visual fatigue, and created bottlenecks in regulatory workflows.
""")

st.markdown("##### Solution")
st.write("""
Engineered an automated verification pipeline using OpenCV for stamp detection and Tesseract OCR 
for signature validation. The system processes PDFs in batch, flags exceptions for human review, 
and generates compliance reports. Implemented template matching algorithms with 95%+ accuracy on 
standard document formats.
""")

st.markdown("##### Impact Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="BEFORE", value="40 hrs/month", delta=None)
with col2:
    st.metric(label="AFTER", value="8 hrs/month", delta="-32 hrs", delta_color="normal")
with col3:
    st.metric(label="IMPROVEMENT", value="80% ↓", delta=None)

st.markdown("##### 📈 Impact")
st.write("- Automated validation of 400+ compliance PDFs per month")
st.write("- Reduced manual review effort by 80% (~40 hours/month)")
st.write("- Cut error rate from 8% to <2% through consistent automated checks")
st.write("- Enabled team to focus on complex edge cases requiring human judgment")

st.caption("**Stack:** Python, OpenCV, PyMuPDF, scikit-image, Tesseract OCR, pandas")

st.markdown("---")

# Project 2: Power Automate
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("Power Automate — File Renaming & Ticket Tracking")
    st.caption("Power Automate · AI Builder · Excel · Power Query")
with col2:
    st.success("COMPLETED")

st.markdown("##### Problem")
st.write("""
Operations team processed ~480 financial files daily, each requiring manual renaming based on content 
classification. Additionally, ~20 Jira tickets per day needed manual Excel updates for tracking. 
This consumed 80+ hours monthly and introduced frequent naming inconsistencies.
""")

st.markdown("##### Solution")
st.write("""
Designed intelligent Power Automate flows with AI Builder content recognition for automated file 
classification and rule-based renaming. Built parallel workflow for Jira-to-Excel synchronization 
with error handling and notification triggers. Implemented validation checks to ensure naming consistency.
""")

st.markdown("##### Impact Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="BEFORE", value="480 files", delta=None)
with col2:
    st.metric(label="AFTER", value="Automated", delta="480 files/month", delta_color="normal")
with col3:
    st.metric(label="TIME SAVED", value="80 hrs/month", delta=None)

st.markdown("##### Impact")
st.write("- Automated renaming of 480+ files per month with 98% accuracy")
st.write("- Eliminated 80 hours/month of manual file processing")
st.write("- Reduced naming errors by 85% through standardized automation")
st.write("- Real-time ticket tracking replaced end-of-day manual updates")

st.caption("**Stack:** Power Automate, AI Builder, Excel, Power Query, SharePoint")

st.markdown("---")

# Project 3: Real-Time Dashboards
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("Real-Time Trading Analytics Dashboards")
    st.caption("Power BI · Apache Zeppelin · Scala · SQL Server")
with col2:
    st.success("COMPLETED")

st.markdown("##### Problem")
st.write("""
Traders relied on static, fragmented reports distributed via email twice daily. This created 
information lag, prevented intraday decision-making, and required ad-hoc data requests that 
consumed analyst time. No single source of truth existed for trading KPIs.
""")

st.markdown("##### Solution")
st.write("""
Built interactive Power BI dashboards integrated with Apache Zeppelin notebooks and Scala-based 
data pipelines. Implemented near real-time refresh schedules pulling from trading databases. 
Created role-based views for different trading desks with drill-down capabilities into position 
details and P&L attribution.
""")

st.markdown("##### Impact Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="BEFORE", value="2x daily", delta=None)
with col2:
    st.metric(label="AFTER", value="Live data", delta="<15 min latency", delta_color="normal")
with col3:
    st.metric(label="AD-HOC REQUESTS", value="60% ↓", delta=None)

st.markdown("##### Impact")
st.write("- Live KPI visibility replaced twice-daily static reports")
st.write("- Reduced ad-hoc analyst requests by 60% through self-service analytics")
st.write("- Improved intraday decision-making with <15 minute data latency")
st.write("- Dashboard adoption: 90%+ of trading team uses daily")

st.caption("**Stack:** Power BI, Apache Zeppelin, Scala, SQL Server, DAX")

st.markdown("---")

# Project 4: Excel Reconciliation
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("Excel-Based Data Reconciliation & Validation")
    st.caption("Power Query M · VBA · Data Quality")
with col2:
    st.success("COMPLETED")

st.markdown("##### Problem")
st.write("""
Daily reconciliation of 30+ CSV files across trading databases (~1.9M rows/month total). 
Manual Excel-based process involved copy-paste across files, vlookup chains, and manual exception 
identification. High defect rates (~40% of reconciliations had errors) and 45+ hours monthly effort.
""")

st.markdown("##### Solution")
st.write("""
Built automated reconciliation engine using Power Query for data transformation and VBA for 
orchestration. Standardized validation rules, automated mismatch detection, and generated exception 
reports with root cause categorization. Implemented data quality checks at ingestion and validation stages.
""")

st.markdown("##### Impact Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="BEFORE", value="1.9M rows", delta=None)
with col2:
    st.metric(label="AFTER", value="Automated", delta="Pipeline built", delta_color="normal")
with col3:
    st.metric(label="TIME SAVED", value="45 hrs/month", delta=None)

st.markdown("##### Impact")
st.write("- Automated reconciliation of 1.9M+ rows per month")
st.write("- Reduced reconciliation time by 45 hours/month")
st.write("- Cut data defects by 40% through standardized validation logic")
st.write("- Generated daily exception reports with actionable insights")

st.caption("**Stack:** Excel, Power Query M, VBA, CSV processing")

st.markdown("---")

# Bottom section
st.info("Explore **Personal Projects** in the sidebar to see analytical depth and technical execution.")
st.caption("All metrics based on production deployment at Deutsche Börse Group and Arcadis")
