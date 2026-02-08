# pages/1_Industry_Case_Studies.py
import streamlit as st

st.set_page_config(page_title="Industry Case Studies", layout="wide", page_icon="💼")

# Custom CSS for the entire page
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');

/* Main styling */
.main {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

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

.project-card {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.03) 0%, rgba(20, 27, 61, 0.5) 100%);
    border: 1px solid rgba(244, 196, 48, 0.2);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #f4c430 0%, #ffd700 100%);
    transform: scaleX(0);
    transition: transform 0.4s ease;
    transform-origin: left;
}

.project-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 16px 48px rgba(244, 196, 48, 0.2);
    border-color: #f4c430;
}

.project-card:hover::before {
    transform: scaleX(1);
}

.project-title {
    font-family: 'Space Mono', monospace;
    font-size: 1.5rem;
    color: #f4c430;
    margin-bottom: 0.5rem;
}

.project-subtitle {
    color: #8892b0;
    margin-bottom: 1rem;
}

.status-badge {
    display: inline-block;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #0a0e27;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    background: #4ade80;
    margin-left: 1rem;
}

.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #f4c430;
    margin: 1rem 0 0.5rem 0;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 700;
}

.section-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    color: #ccd6f6;
    line-height: 1.7;
    margin: 0 0 1rem 0;
}

.metrics-container {
    display: grid;
    grid-template-columns: 1fr auto 1fr 1fr;
    gap: 1rem;
    background: rgba(244, 196, 48, 0.05);
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    align-items: center;
}

.metric-box {
    text-align: center;
}

.metric-box.highlight {
    background: rgba(244, 196, 48, 0.1);
    padding: 0.5rem;
    border-radius: 8px;
    border: 1px solid rgba(244, 196, 48, 0.3);
}

.metric-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #8892b0;
    display: block;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
}

.metric-value {
    font-family: 'Space Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    display: block;
}

.metric-value.before { color: #ef4444; }
.metric-value.after { color: #4ade80; }
.metric-value.improvement { color: #f4c430; }

.metric-arrow {
    font-size: 2rem;
    color: #f4c430;
    text-align: center;
}

.impact-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.impact-item {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.95rem;
    color: #ccd6f6;
    padding: 0.5rem 0;
    padding-left: 1.5rem;
    position: relative;
}

.impact-item::before {
    content: '▹';
    color: #f4c430;
    position: absolute;
    left: 0;
    font-size: 1.2rem;
}

.tools-text {
    font-family: 'DM Sans', sans-serif;
    color: #a8b2d1;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(244, 196, 48, 0.1);
}

.tools-label {
    font-family: 'Space Mono', monospace;
    color: #8892b0;
    font-weight: 700;
}

@media (max-width: 768px) {
    .metrics-container {
        grid-template-columns: 1fr;
    }
    .metric-arrow {
        transform: rotate(90deg);
    }
}
</style>
""", unsafe_allow_html=True)

# Page header
st.markdown("""
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
st.markdown("""
<div class="project-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
        <div>
            <h3 class="project-title">AI-Powered Document Verification System</h3>
            <p class="project-subtitle">Python · OpenCV · OCR · Computer Vision</p>
        </div>
        <span class="status-badge">Completed</span>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">🎯 Problem</h4>
        <p class="section-text">
        The compliance team manually verified ~400 regulatory PDFs each month for required stamps, 
        signatures, and certifications. This manual process was time-intensive (2-3 minutes per document), 
        error-prone due to visual fatigue, and created bottlenecks in regulatory workflows.
        </p>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">💡 Solution</h4>
        <p class="section-text">
        Engineered an automated verification pipeline using OpenCV for stamp detection and Tesseract OCR 
        for signature validation. The system processes PDFs in batch, flags exceptions for human review, 
        and generates compliance reports. Implemented template matching algorithms with 95%+ accuracy on 
        standard document formats.
        </p>
    </div>
    
    <div class="metrics-container">
        <div class="metric-box">
            <span class="metric-label">Before</span>
            <span class="metric-value before">40 hrs/month</span>
        </div>
        <div class="metric-arrow">→</div>
        <div class="metric-box">
            <span class="metric-label">After</span>
            <span class="metric-value after">8 hrs/month</span>
        </div>
        <div class="metric-box highlight">
            <span class="metric-label">Impact</span>
            <span class="metric-value improvement">80% ↓</span>
        </div>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">📈 Impact</h4>
        <ul class="impact-list">
            <li class="impact-item">Automated validation of 400+ compliance PDFs per month</li>
            <li class="impact-item">Reduced manual review effort by 80% (~40 hours/month)</li>
            <li class="impact-item">Cut error rate from 8% to &lt;2% through consistent automated checks</li>
            <li class="impact-item">Enabled team to focus on complex edge cases requiring human judgment</li>
        </ul>
    </div>
    
    <div class="tools-text">
        <span class="tools-label">Stack:</span> Python, OpenCV, PyMuPDF, scikit-image, Tesseract OCR, pandas
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: none; height: 2px; background: linear-gradient(90deg, transparent 0%, rgba(244, 196, 48, 0.5) 50%, transparent 100%); margin: 3rem 0;'>", unsafe_allow_html=True)

# Project 2: Power Automate
st.markdown("""
<div class="project-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
        <div>
            <h3 class="project-title">Power Automate — File Renaming & Ticket Tracking</h3>
            <p class="project-subtitle">Power Automate · AI Builder · Excel · Power Query</p>
        </div>
        <span class="status-badge">Completed</span>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">🎯 Problem</h4>
        <p class="section-text">
        Operations team processed ~480 financial files daily, each requiring manual renaming based on content 
        classification. Additionally, ~20 Jira tickets per day needed manual Excel updates for tracking. 
        This consumed 80+ hours monthly and introduced frequent naming inconsistencies.
        </p>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">💡 Solution</h4>
        <p class="section-text">
        Designed intelligent Power Automate flows with AI Builder content recognition for automated file 
        classification and rule-based renaming. Built parallel workflow for Jira-to-Excel synchronization 
        with error handling and notification triggers. Implemented validation checks to ensure naming consistency.
        </p>
    </div>
    
    <div class="metrics-container">
        <div class="metric-box">
            <span class="metric-label">Before</span>
            <span class="metric-value before">480 files manually</span>
        </div>
        <div class="metric-arrow">→</div>
        <div class="metric-box">
            <span class="metric-label">After</span>
            <span class="metric-value after">Fully automated</span>
        </div>
        <div class="metric-box highlight">
            <span class="metric-label">Impact</span>
            <span class="metric-value improvement">80 hrs ↓</span>
        </div>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">📈 Impact</h4>
        <ul class="impact-list">
            <li class="impact-item">Automated renaming of 480+ files per month with 98% accuracy</li>
            <li class="impact-item">Eliminated 80 hours/month of manual file processing</li>
            <li class="impact-item">Reduced naming errors by 85% through standardized automation</li>
            <li class="impact-item">Real-time ticket tracking replaced end-of-day manual updates</li>
        </ul>
    </div>
    
    <div class="tools-text">
        <span class="tools-label">Stack:</span> Power Automate, AI Builder, Excel, Power Query, SharePoint
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: none; height: 2px; background: linear-gradient(90deg, transparent 0%, rgba(244, 196, 48, 0.5) 50%, transparent 100%); margin: 3rem 0;'>", unsafe_allow_html=True)

# Project 3: Real-Time Dashboards
st.markdown("""
<div class="project-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
        <div>
            <h3 class="project-title">Real-Time Trading Analytics Dashboards</h3>
            <p class="project-subtitle">Power BI · Apache Zeppelin · Scala · SQL Server</p>
        </div>
        <span class="status-badge">Completed</span>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">🎯 Problem</h4>
        <p class="section-text">
        Traders relied on static, fragmented reports distributed via email twice daily. This created 
        information lag, prevented intraday decision-making, and required ad-hoc data requests that 
        consumed analyst time. No single source of truth existed for trading KPIs.
        </p>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">💡 Solution</h4>
        <p class="section-text">
        Built interactive Power BI dashboards integrated with Apache Zeppelin notebooks and Scala-based 
        data pipelines. Implemented near real-time refresh schedules pulling from trading databases. 
        Created role-based views for different trading desks with drill-down capabilities into position 
        details and P&L attribution.
        </p>
    </div>
    
    <div class="metrics-container">
        <div class="metric-box">
            <span class="metric-label">Before</span>
            <span class="metric-value before">2x daily reports</span>
        </div>
        <div class="metric-arrow">→</div>
        <div class="metric-box">
            <span class="metric-label">After</span>
            <span class="metric-value after">Live dashboards</span>
        </div>
        <div class="metric-box highlight">
            <span class="metric-label">Impact</span>
            <span class="metric-value improvement">60% ↓ requests</span>
        </div>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">📈 Impact</h4>
        <ul class="impact-list">
            <li class="impact-item">Live KPI visibility replaced twice-daily static reports</li>
            <li class="impact-item">Reduced ad-hoc analyst requests by 60% through self-service analytics</li>
            <li class="impact-item">Improved intraday decision-making with &lt;15 minute data latency</li>
            <li class="impact-item">Dashboard adoption: 90%+ of trading team uses daily</li>
        </ul>
    </div>
    
    <div class="tools-text">
        <span class="tools-label">Stack:</span> Power BI, Apache Zeppelin, Scala, SQL Server, DAX
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: none; height: 2px; background: linear-gradient(90deg, transparent 0%, rgba(244, 196, 48, 0.5) 50%, transparent 100%); margin: 3rem 0;'>", unsafe_allow_html=True)

# Project 4: Excel Reconciliation
st.markdown("""
<div class="project-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
        <div>
            <h3 class="project-title">Excel-Based Data Reconciliation & Validation</h3>
            <p class="project-subtitle">Power Query M · VBA · Data Quality</p>
        </div>
        <span class="status-badge">Completed</span>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">🎯 Problem</h4>
        <p class="section-text">
        Daily reconciliation of 30+ CSV files across trading databases (~1.9M rows/month total). 
        Manual Excel-based process involved copy-paste across files, vlookup chains, and manual exception 
        identification. High defect rates (~40% of reconciliations had errors) and 45+ hours monthly effort.
        </p>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">💡 Solution</h4>
        <p class="section-text">
        Built automated reconciliation engine using Power Query for data transformation and VBA for 
        orchestration. Standardized validation rules, automated mismatch detection, and generated exception 
        reports with root cause categorization. Implemented data quality checks at ingestion and validation stages.
        </p>
    </div>
    
    <div class="metrics-container">
        <div class="metric-box">
            <span class="metric-label">Before</span>
            <span class="metric-value before">1.9M rows manual</span>
        </div>
        <div class="metric-arrow">→</div>
        <div class="metric-box">
            <span class="metric-label">After</span>
            <span class="metric-value after">Automated pipeline</span>
        </div>
        <div class="metric-box highlight">
            <span class="metric-label">Impact</span>
            <span class="metric-value improvement">45 hrs ↓</span>
        </div>
    </div>
    
    <div style="margin: 1rem 0;">
        <h4 class="section-label">📈 Impact</h4>
        <ul class="impact-list">
            <li class="impact-item">Automated reconciliation of 1.9M+ rows per month</li>
            <li class="impact-item">Reduced reconciliation time by 45 hours/month</li>
            <li class="impact-item">Cut data defects by 40% through standardized validation logic</li>
            <li class="impact-item">Generated daily exception reports with actionable insights</li>
        </ul>
    </div>
    
    <div class="tools-text">
        <span class="tools-label">Stack:</span> Excel, Power Query M, VBA, CSV processing
    </div>
</div>
""", unsafe_allow_html=True)

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
