# pages/2_Personal_Projects.py
import streamlit as st

st.set_page_config(page_title="Personal Projects", layout="wide", page_icon="🔬")

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

st.title("Personal Analytics Projects")
st.markdown("""
**Independent work demonstrating analytical thinking and technical execution**  
Projects built to explore data transformation, visualization, and pipeline design.
""")

st.markdown("---")

# Project 1
st.subheader("Interactive BI Analytics Dashboard")
st.caption("Streamlit, Pandas, Plotly")
st.markdown("**Status:** In Progress")

st.markdown("**Purpose**")
st.write("""
Reusable dashboard template for rapid analytics deployment. Designed to be stakeholder-friendly 
with interactive filters and export capabilities.
""")

st.markdown("**Approach**")
st.write("""
Built with Streamlit for UI, pandas for data processing, and Plotly for visualizations. 
Implements KPI cards, time-series charts, dynamic filters, and CSV export functionality. 
Mobile-responsive design following dashboard best practices.
""")

st.markdown("**Technical Focus**")
st.write("- Interactive data exploration with dynamic filters")
st.write("- Clean UI/UX for non-technical users")
st.write("- Export functionality for deeper analysis")
st.write("- Zero licensing costs, deployable via Streamlit Cloud")

if st.button("View Code - Interactive BI App", key="proj1"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/interactive-bi-analytics-app)")

st.markdown("---")

# Project 2
st.subheader("End-to-End Analytics Pipeline")
st.caption("Python, Pandas, Pytest")
st.markdown("**Status:** In Progress")

st.markdown("**Purpose**")
st.write("""
Demonstrate production-grade ETL pipeline with proper engineering practices. 
Most portfolios show outputs but not the engineering behind them.
""")

st.markdown("**Approach**")
st.write("""
Modular pipeline with separation of concerns: ingestion, transformation, validation, aggregation, output. 
Includes pytest for data quality tests, structured logging, and configuration management.
""")

st.markdown("**Technical Focus**")
st.write("- Reproducible pipeline with clear folder structure")
st.write("- Data quality tests prevent bad data downstream")
st.write("- Logging enables debugging and audit trails")
st.write("- Software engineering practices for analytics")

if st.button("View Code - Analytics Pipeline", key="proj2"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/end-to-end-analytics-pipeline)")

st.markdown("---")

# Project 3
st.subheader("Data Cleaning and Preparation")
st.caption("Python, Pandas")
st.markdown("**Status:** Completed")

st.markdown("**Purpose**")
st.write("""
Practical data wrangling demonstration. Real-world data is rarely clean - this project 
addresses common issues encountered in BI work.
""")

st.markdown("**Approach**")
st.write("""
Multi-stage cleaning pipeline: date standardization with error handling, missing value 
imputation based on business logic, duplicate detection and removal, aggregation to monthly KPIs. 
Transactional dataset with inconsistent date formats and missing values.
""")

st.markdown("**Outcomes**")
st.write("- Cleaned dataset ready for monthly KPI reporting")
st.write("- Standardized 5,000+ inconsistent date entries")
st.write("- Documented decision logic for missing value handling")
st.write("- Time-series visualization of transaction trends")

if st.button("View Code - Data Cleaning", key="proj3"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/bi-data-cleaning-case-study)")

st.markdown("---")

# Project 4
st.subheader("Automated Data Reconciliation")
st.caption("Python, Pandas, Openpyxl")
st.markdown("**Status:** Completed")

st.markdown("**Purpose**")
st.write("""
Automate weekly reconciliation between two financial ledgers. Manual process involved 
sorting in Excel, visual comparison, and flagging mismatches.
""")

st.markdown("**Approach**")
st.write("""
Built reconciliation script that joins datasets on transaction IDs, compares amounts and dates, 
labels match status, and exports separate exception file for investigation. Implemented tolerance 
thresholds for amount matching and date drift handling.
""")

st.markdown("**Outcomes**")
st.write("- Weekly reconciliation automated from 4 hours to 5 minutes")
st.write("- Reconciled dataset with clear match/mismatch labels")
st.write("- Exception file with categorized issues for follow-up")
st.write("- Caught edge cases previously missed in manual review")

if st.button("View Code - Data Reconciliation", key="proj4"):
    st.markdown("[GitHub Repository](https://github.com/amit1820/data-reconciliation-exceptions)")

st.markdown("---")

st.info("All project code available on GitHub: github.com/amit1820")
