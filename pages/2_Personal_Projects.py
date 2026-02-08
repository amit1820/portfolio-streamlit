# pages/2_Personal_Projects_Enhanced.py
import streamlit as st
from components_enhanced import project_card_enhanced, load_project_card_css

st.set_page_config(page_title="Personal Projects", layout="wide", page_icon="🔬")

# Load custom CSS
load_project_card_css()

# Page header
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');

.page-header {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    padding: 2rem;
    border-radius: 16px;
    border: 1px solid rgba(244, 196, 48, 0.2);
    margin-bottom: 3rem;
}

.page-title {
    font-family: 'Space Mono', monospace;
    font-size: 2.5rem;
    font-weight: 700;
    color: #f4c430;
    margin: 0 0 1rem 0;
    letter-spacing: -1px;
}

.page-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.2rem;
    color: #a8b2d1;
    line-height: 1.6;
    margin: 0;
}

.section-divider {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent 0%, rgba(244, 196, 48, 0.5) 50%, transparent 100%);
    margin: 3rem 0;
}

.wip-badge {
    display: inline-block;
    background: rgba(251, 191, 36, 0.2);
    color: #fbbf24;
    padding: 0.3rem 0.8rem;
    border-radius: 12px;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    border: 1px solid rgba(251, 191, 36, 0.4);
    margin-left: 0.5rem;
}
</style>

<div class="page-header">
    <h1 class="page-title">🔬 Personal Analytics Projects</h1>
    <p class="page-subtitle">
    Experimental work demonstrating analytical rigor, pipeline thinking, and clean code principles. 
    These projects showcase technical depth in data transformation, visualization, and ETL design — 
    built for learning and portfolio demonstration.
    </p>
</div>
""", unsafe_allow_html=True)

# Project 1: Interactive BI App
project_card_enhanced(
    title="Interactive BI Analytics Dashboard",
    subtitle="Streamlit · Pandas · Plotly · Data Visualization",
    context="Need for a reusable, stakeholder-friendly dashboard template that non-technical users can interact with. Most BI tools require licenses; wanted to build a lightweight, customizable alternative for quick analytics delivery.",
    solution="Built interactive Streamlit application with KPI cards, time-series visualizations, and dynamic filters. Implemented CSV export for further analysis and designed mobile-responsive layouts. Emphasized clean UI/UX following dashboard design best practices.",
    impact_lines=[
        "Reusable template for rapid analytics deployment",
        "Interactive filters for dynamic data exploration",
        "Export functionality for stakeholder deep-dives",
        "Zero licensing costs, easily deployable via Streamlit Cloud"
    ],
    tools="Python, Streamlit, pandas, plotly, altair",
    status="In Progress",
    repo_link="https://github.com/amit1820/interactive-bi-analytics-app"
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Project 2: End-to-End Analytics Pipeline
project_card_enhanced(
    title="End-to-End Analytics Pipeline",
    subtitle="Python · ETL · Data Engineering · Testing",
    context="Most portfolio projects show final outputs but not the engineering behind them. Wanted to demonstrate a production-grade ETL pipeline with proper logging, error handling, testing, and reproducibility.",
    solution="Designed modular ETL pipeline with separation of concerns: ingestion → transformation → validation → aggregation → output. Implemented pytest for data quality tests, structured logging, and configuration management. Built final dashboard to visualize pipeline outputs.",
    impact_lines=[
        "Reproducible pipeline with clear folder structure",
        "Data quality tests prevent bad data downstream",
        "Logging enables debugging and audit trails",
        "Demonstrates software engineering practices for analytics"
    ],
    tools="Python, pandas, pytest, logging, configparser, streamlit",
    status="In Progress",
    repo_link="https://github.com/amit1820/end-to-end-analytics-pipeline"
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Project 3: BI Realism - Data Cleaning
project_card_enhanced(
    title="BI Realism — From Messy Data to Decision-Ready Output",
    subtitle="Python · Pandas · Data Cleaning · Time Series",
    context="Transactional dataset with inconsistent date formats (MM/DD/YYYY vs DD-MM-YYYY), missing values in critical fields, and duplicate records. Real-world data is rarely clean — this project showcases practical data wrangling before analysis.",
    solution="Implemented multi-stage cleaning pipeline: (1) date standardization with error handling, (2) missing value imputation based on business logic, (3) duplicate detection and removal, (4) aggregation to monthly KPIs. Generated time-series visualizations for business review.",
    impact_lines=[
        "Cleaned dataset ready for monthly KPI reporting",
        "Standardized 5,000+ inconsistent date entries",
        "Documented decision logic for missing value handling",
        "Time-series visualization reveals transaction trends"
    ],
    tools="Python, pandas, matplotlib, datetime",
    status="Completed",
    repo_link="https://github.com/amit1820/bi-data-cleaning-case-study.git",
    metrics={
        "before": "Messy data",
        "after": "Clean dataset",
        "improvement": "5K+ rows"
    }
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Project 4: Automated Reconciliation
project_card_enhanced(
    title="Automated Data Reconciliation & Exception Reporting",
    subtitle="Python · Data Validation · Quality Controls",
    context="Two financial ledgers (internal vs vendor) required weekly reconciliation. Manual process involved sorting in Excel, visual comparison, and flagging mismatches. Missed edge cases (amount discrepancies <$1) and consumed 4+ hours weekly.",
    solution="Built reconciliation script that joins datasets on transaction IDs, compares amounts and dates, labels match status, and exports separate exception file for investigation. Implemented tolerance thresholds for amount matching and date drift handling.",
    impact_lines=[
        "Weekly reconciliation automated from 4 hours to 5 minutes",
        "Reconciled dataset with clear match/mismatch labels",
        "Exception file with categorized issues for follow-up",
        "Caught edge cases previously missed in manual review"
    ],
    tools="Python, pandas, openpyxl",
    status="Completed",
    repo_link="https://github.com/amit1820/data-reconciliation-exceptions.git",
    metrics={
        "before": "4 hrs weekly",
        "after": "5 min automated",
        "improvement": "98% ↓"
    }
)

# Bottom CTA
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: rgba(244, 196, 48, 0.05); border-radius: 12px; border: 1px solid rgba(244, 196, 48, 0.2);">
    <p style="font-family: 'DM Sans', sans-serif; font-size: 1.1rem; color: #ccd6f6; margin-bottom: 1rem;">
    All project code available on <a href="https://github.com/amit1820" style="color: #f4c430; text-decoration: none; font-weight: 700;">GitHub</a>
    </p>
    <p style="font-family: 'Space Mono', monospace; font-size: 0.9rem; color: #8892b0;">
    👈 Check out <strong style="color: #f4c430;">Research</strong> for academic work on ESG and financial markets
    </p>
</div>
""", unsafe_allow_html=True)
