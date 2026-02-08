# pages/1_Industry_Case_Studies_Enhanced.py
import streamlit as st
from components import project_card_enhanced, load_project_card_css

st.set_page_config(page_title="Industry Case Studies", layout="wide", page_icon="💼")

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
</style>

<div class="page-header">
    <h1 class="page-title">💼 Industry & Professional Case Studies</h1>
    <p class="page-subtitle">
    Production-ready analytics solutions deployed at Deutsche Börse Group and Arcadis. 
    These projects showcase hands-on delivery of automation pipelines, real-time dashboards, 
    and data workflows that eliminated manual processes and improved decision-making velocity.
    </p>
</div>
""", unsafe_allow_html=True)

# Project 1: AI Document Verification
project_card_enhanced(
    title="AI-Powered Document Verification System",
    subtitle="Python · OpenCV · OCR · Computer Vision",
    context="The compliance team manually verified ~400 regulatory PDFs each month for required stamps, signatures, and certifications. This manual process was time-intensive (2-3 minutes per document), error-prone due to visual fatigue, and created bottlenecks in regulatory workflows.",
    solution="Engineered an automated verification pipeline using OpenCV for stamp detection and Tesseract OCR for signature validation. The system processes PDFs in batch, flags exceptions for human review, and generates compliance reports. Implemented template matching algorithms with 95%+ accuracy on standard document formats.",
    impact_lines=[
        "Automated validation of 400+ compliance PDFs per month",
        "Reduced manual review effort by 80% (~40 hours/month)",
        "Cut error rate from 8% to <2% through consistent automated checks",
        "Enabled team to focus on complex edge cases requiring human judgment"
    ],
    tools="Python, OpenCV, PyMuPDF, scikit-image, Tesseract OCR, pandas",
    status="Completed",
    metrics={
        "before": "40 hrs/month",
        "after": "8 hrs/month",
        "improvement": "80% ↓"
    }
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Project 2: Power Automate Workflows
project_card_enhanced(
    title="Power Automate — File Renaming & Ticket Tracking",
    subtitle="Power Automate · AI Builder · Excel · Power Query",
    context="Operations team processed ~480 financial files daily, each requiring manual renaming based on content classification. Additionally, ~20 Jira tickets per day needed manual Excel updates for tracking. This consumed 80+ hours monthly and introduced frequent naming inconsistencies.",
    solution="Designed intelligent Power Automate flows with AI Builder content recognition for automated file classification and rule-based renaming. Built parallel workflow for Jira-to-Excel synchronization with error handling and notification triggers. Implemented validation checks to ensure naming consistency.",
    impact_lines=[
        "Automated renaming of 480+ files per month with 98% accuracy",
        "Eliminated 80 hours/month of manual file processing",
        "Reduced naming errors by 85% through standardized automation",
        "Real-time ticket tracking replaced end-of-day manual updates"
    ],
    tools="Power Automate, AI Builder, Excel, Power Query, SharePoint",
    status="Completed",
    metrics={
        "before": "480 files manually",
        "after": "Fully automated",
        "improvement": "80 hrs ↓"
    }
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Project 3: Real-Time Trading Dashboards
project_card_enhanced(
    title="Real-Time Trading Analytics Dashboards",
    subtitle="Power BI · Apache Zeppelin · Scala · SQL Server",
    context="Traders relied on static, fragmented reports distributed via email twice daily. This created information lag, prevented intraday decision-making, and required ad-hoc data requests that consumed analyst time. No single source of truth existed for trading KPIs.",
    solution="Built interactive Power BI dashboards integrated with Apache Zeppelin notebooks and Scala-based data pipelines. Implemented near real-time refresh schedules pulling from trading databases. Created role-based views for different trading desks with drill-down capabilities into position details and P&L attribution.",
    impact_lines=[
        "Live KPI visibility replaced twice-daily static reports",
        "Reduced ad-hoc analyst requests by 60% through self-service analytics",
        "Improved intraday decision-making with <15 minute data latency",
        "Dashboard adoption: 90%+ of trading team uses daily"
    ],
    tools="Power BI, Apache Zeppelin, Scala, SQL Server, DAX",
    status="Completed",
    metrics={
        "before": "2x daily reports",
        "after": "Live dashboards",
        "improvement": "60% ↓ requests"
    }
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# Project 4: Excel Data Reconciliation
project_card_enhanced(
    title="Excel-Based Data Reconciliation & Validation",
    subtitle="Power Query M · VBA · Data Quality",
    context="Daily reconciliation of 30+ CSV files across trading databases (~1.9M rows/month total). Manual Excel-based process involved copy-paste across files, vlookup chains, and manual exception identification. High defect rates (~40% of reconciliations had errors) and 45+ hours monthly effort.",
    solution="Built automated reconciliation engine using Power Query for data transformation and VBA for orchestration. Standardized validation rules, automated mismatch detection, and generated exception reports with root cause categorization. Implemented data quality checks at ingestion and validation stages.",
    impact_lines=[
        "Automated reconciliation of 1.9M+ rows per month",
        "Reduced reconciliation time by 45 hours/month",
        "Cut data defects by 40% through standardized validation logic",
        "Generated daily exception reports with actionable insights"
    ],
    tools="Excel, Power Query M, VBA, CSV processing",
    status="Completed",
    metrics={
        "before": "1.9M rows manual",
        "after": "Automated pipeline",
        "improvement": "45 hrs ↓"
    }
)

# Bottom CTA
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: rgba(244, 196, 48, 0.05); border-radius: 12px; border: 1px solid rgba(244, 196, 48, 0.2);">
    <p style="font-family: 'DM Sans', sans-serif; font-size: 1.1rem; color: #ccd6f6; margin-bottom: 1rem;">
    👈 Explore <strong style="color: #f4c430;">Personal Projects</strong> in the sidebar to see analytical depth and technical execution.
    </p>
    <p style="font-family: 'Space Mono', monospace; font-size: 0.9rem; color: #8892b0;">
    All metrics based on production deployment at Deutsche Börse Group and Arcadis
    </p>
</div>
""", unsafe_allow_html=True)
