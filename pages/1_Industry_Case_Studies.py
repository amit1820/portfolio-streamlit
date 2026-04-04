# pages/1_Industry_Case_Studies.py
import streamlit as st

st.set_page_config(page_title="Industry Case Studies", layout="wide", page_icon="💼")

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
.stDownloadButton button { background: linear-gradient(135deg, #f4c430 0%, #ffd700 100%); color: #0a0e27 !important; font-family: 'Space Mono', monospace; font-weight: 700 !important; border: none; padding: 0.75rem 2rem; border-radius: 8px; }
.stButton button { background: transparent; color: #ccd6f6; border: none; font-family: 'DM Sans', sans-serif; font-size: 1rem; font-weight: 500; padding: 0.6rem 1.5rem; border-radius: 6px; transition: all 0.3s ease; }
.stButton button:hover { color: #f4c430; background: rgba(244, 196, 48, 0.1); }
div[data-testid="stAlert"] { background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%); border: 1px solid rgba(244, 196, 48, 0.3); border-radius: 12px; font-family: 'DM Sans', sans-serif; }
.stCaption { font-family: 'Inter', sans-serif; color: #8892b0 !important; font-size: 0.9rem !important; }
a { color: #64ffda; text-decoration: none; }
a:hover { color: #ffd700; text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

# Page Title
st.title("Industry Case Studies")
st.markdown("### Production analytics solutions deployed across Deutsche Börse Group, Arcadis, and more")
st.write("""
Real-world dashboards, automation pipelines, statistical models, and data infrastructure 
deployed in financial markets, enterprise operations, and startup ecosystems.
""")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# EUREX — Project 1: Derivatives Analytics & Dashboards
# ═══════════════════════════════════════════════════════════════
st.markdown("## Derivatives Analytics & Market Intelligence")
st.caption("**Eurex Clearing AG (Deutsche Börse Group)** | Jan 2026 - Present")

st.info("""
**Current Role:** Business Analytics, Market & Liquidity Analytics (Internship). Designing dashboards 
for 200+ clearing members, developing statistical models, building Databricks data infrastructure, 
and producing published market intelligence.
""")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Interactive Power BI Dashboards")
    st.write("""
    Design interactive Power BI dashboards for 200+ clearing members across 22 countries, 
    including a monthly derivatives performance report for the Eurex sales team. Replacing 
    static Excel processes with scalable self-service analytics. Collaborate with Sales Intelligence 
    to define KPI frameworks for derivatives performance tracking across Equity Index and Fixed Income 
    products spanning 10+ product categories.
    """)

    st.markdown("#### Market Intelligence Reports")
    st.write("""
    Produce monthly market intelligence reports analyzing trading volumes, open interest trends, 
    and liquidity metrics across all Eurex product categories — published on the Eurex website 
    as the primary market intelligence resource for external stakeholders.
    """)

    st.caption("**Tech Stack:** Power BI (DAX, Power Query), Python, VBA, SQL, MicroStrategy, StatistiX")

with col2:
    st.markdown("#### Impact")
    st.metric("Clearing Members", "200+", "Across 22 countries")
    st.metric("Product Categories", "10+", "Equity, Fixed Income, ESG")
    st.metric("Newsletter", "Monthly", "Published on Eurex website")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# EUREX — Project 2: Statistical Outlier Detection
# ═══════════════════════════════════════════════════════════════
st.markdown("## Statistical Outlier Detection for Collateral Fee Analysis")
st.caption("**Eurex Clearing AG (Deutsche Börse Group)** | Jan 2026 - Present")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Eurex Clearing manages collateral fees (securities collateral and add-on fees) across 200+ 
    clearing members. Identifying which members have anomalous fee patterns — and understanding 
    the key drivers behind fee changes — required a systematic, data-driven approach beyond 
    manual inspection.
    """)

    st.markdown("#### Solution")
    st.write("""
    Developing a Python-based statistical outlier detection model using SciPy and Statsmodels 
    on live HDFS data. The model analyzes securities collateral and add-on fee patterns across 
    weekly, monthly, and yearly periods to detect anomalous trends and identify key drivers 
    of fee variability across clearing members.
    """)

    st.caption("**Tech Stack:** Python (SciPy, Statsmodels), Apache Zeppelin, HDFS")

with col2:
    st.markdown("#### Impact")
    st.metric("Members Analyzed", "200+", "All Eurex clearing members")
    st.metric("Fee Types", "2", "Securities collateral & add-on")
    st.metric("Periods", "3", "Weekly, monthly, yearly")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# EUREX — Project 3: Databricks Data Models
# ═══════════════════════════════════════════════════════════════
st.markdown("## Centralized Data Models on Databricks")
st.caption("**Eurex Clearing AG (Deutsche Börse Group)** | Jan 2026 - Present")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    The Market & Liquidity Analytics department relied on multiple disparate data sources 
    for reporting and analytics. BI developers had to query different systems separately, 
    creating inconsistencies and inefficiencies in the analytics workflow.
    """)

    st.markdown("#### Solution")
    st.write("""
    Building centralized data models on Databricks as a single-source analytics layer for the 
    department. Consolidating multiple data sources into a unified platform, enabling BI developers 
    to connect directly instead of querying multiple systems — improving data consistency, 
    reducing query complexity, and accelerating dashboard development.
    """)

    st.caption("**Tech Stack:** Databricks, SQL, Data Modeling")

with col2:
    st.markdown("#### Impact")
    st.metric("Data Sources", "Multiple", "Consolidated into one layer")
    st.metric("Outcome", "Single-source", "Analytics layer for BI")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# DB — Project 4: Computer Vision
# ═══════════════════════════════════════════════════════════════
st.markdown("## Computer Vision-Based Document Verification")
st.caption("**Deutsche Börse AG, Cash Market Services (Working Student)** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Compliance team manually verified 400+ regulatory PDFs each month for stamps and signatures. 
    Manual process was time-consuming and prone to visual fatigue errors, creating compliance risk.
    """)

    st.markdown("#### Solution")
    st.write("""
    Developed computer vision-based verification tool using Python with OpenCV for stamp and signature 
    detection and PyMuPDF for document processing. System automatically scans each PDF, detects required 
    compliance elements, and flags exceptions for manual review.
    """)

    st.caption("**Tech Stack:** Python, OpenCV, PyMuPDF")

with col2:
    st.markdown("#### Impact")
    st.metric("Documents/Month", "400+", "Automated scanning")
    st.metric("Exception Flagging", "Automated", "Compliance risk reduced")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# DB — Project 5: Power Automate Workflows
# ═══════════════════════════════════════════════════════════════
st.markdown("## Power Automate Workflows for Cash Market Operations")
st.caption("**Deutsche Börse AG, Cash Market Services (Working Student)** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Cash market operations involved manual file processing and data entry across multiple systems. 
    Repetitive tasks consumed significant analyst time and introduced manual errors.
    """)

    st.markdown("#### Solution")
    st.write("""
    Engineered rule-based automation workflows using Power Automate with AI Builder for content recognition, 
    saving 20+ hours/month and reducing manual errors by 50%+ across cash market operations. Automated 
    reconciliation of 500K+ rows/month using Power Query and VBA, achieving 30% reduction in data defects 
    after resolving inconsistent date formats and field mappings.
    """)

    st.caption("**Tech Stack:** Power Automate, AI Builder, Power Query, VBA")

with col2:
    st.markdown("#### Impact")
    st.metric("Rows Reconciled", "500K+/month", "Automated")
    st.metric("Time Saved", "20+ hrs/month", "Workflow automation")
    st.metric("Manual Errors", "50%+ reduction", "Quality improvement")
    st.metric("Data Defects", "30% reduction", "Field mapping fixes")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# DB — Project 6: Real-Time Trading Dashboards
# ═══════════════════════════════════════════════════════════════
st.markdown("## Real-Time Trading Analytics Dashboards")
st.caption("**Deutsche Börse AG, Cash Market Services (Working Student)** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Traders relied on static reports and ad-hoc data requests for analytics. No unified view of 
    trading KPIs led to information fragmentation and delayed decision-making.
    """)

    st.markdown("#### Solution")
    st.write("""
    Designed and deployed real-time Power BI dashboards integrating Scala and Apache Zeppelin data sources 
    for live trading analytics. Dashboards replaced ad-hoc report requests and provide traders 
    with self-service access to key metrics — dashboards traders check daily.
    """)

    st.caption("**Tech Stack:** Power BI, Apache Zeppelin, Scala, SQL")

with col2:
    st.markdown("#### Impact")
    st.metric("Adoption", "Daily usage", "Traders check dashboards daily")
    st.metric("Ad-hoc Requests", "Significant reduction", "Self-service analytics")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# Arcadis — HS2
# ═══════════════════════════════════════════════════════════════
st.markdown("## Power BI Dashboards & Data Automation for UK HS2 Rail Programme")
st.caption("**Arcadis — Data & Analytics Consultant, BIM Analytics** | Aug 2022 - July 2024")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    HS2 — the UK's £100B+ national rail infrastructure programme — needed real-time visibility into 
    KPIs and resource allocation across 15+ work packages. Manual reporting processes created delays 
    in project tracking and cross-functional decision-making.
    """)

    st.markdown("#### Solution")
    st.write("""
    Built Power BI dashboards and Power Apps for real-time KPI tracking and resource management across 
    15+ work packages. Automated data validation and transformation pipelines using Python, Dynamo, and 
    VBA, reducing manual processing time by 60%. Led cross-functional data automation initiatives across 
    engineering and project management teams, reducing manual approval time by 2 days per work package.
    """)

    st.caption("**Tech Stack:** Power BI, Power Apps, Python, Dynamo, VBA")

with col2:
    st.markdown("#### Impact")
    st.metric("Work Packages", "15+", "Real-time KPI tracking")
    st.metric("Processing Time", "60% reduction", "Automation pipelines")
    st.metric("Approval Time", "2 days saved", "Per work package")
    st.metric("Programme Scale", "£100B+", "UK national infrastructure")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# Alliant Advisory
# ═══════════════════════════════════════════════════════════════
st.markdown("## Financial Data Analytics for Cost Segregation")
st.caption("**Alliant Advisory — Associate, Cost Segregation Analytics** | Feb 2022 - July 2022")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Cost segregation projects for US tax advisory required consistent analysis of large financial 
    datasets across multiple real estate client engagements. Manual reporting processes created 
    inefficiencies and inconsistencies in deliverables.
    """)

    st.markdown("#### Solution")
    st.write("""
    Analyzed large financial datasets for cost segregation across 5+ real estate client projects, 
    supporting US tax advisory decisions. Created standardized reporting templates and automated 
    workflows, reducing turnaround time by 28%.
    """)

    st.caption("**Tech Stack:** Excel, VBA, Python")

with col2:
    st.markdown("#### Impact")
    st.metric("Client Projects", "5+", "Real estate cost segregation")
    st.metric("Turnaround Time", "28% reduction", "Process improvement")

st.markdown("---")

# ═══════════════════════════════════════════════════════════════
# Atal Incubation Centre
# ═══════════════════════════════════════════════════════════════
st.markdown("## MySQL Database & Screening Workflows for Startup Incubator")
st.caption("**Atal Incubation Centre — Program Associate, Entrepreneurship Cell (Internship)** | Jan 2021 - Jan 2022")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Startup incubation programme needed a centralized database for tracking 2,400+ founders and their 
    applications. Manual processes led to data inconsistencies and inefficient screening workflows.
    """)

    st.markdown("#### Solution")
    st.write("""
    Built and maintained MySQL databases of 2,400+ founders, improving data accuracy from 92% to 99%. 
    Streamlined SQL-based screening workflows, shortening startup evaluation cycles by 33%.
    """)

    st.caption("**Tech Stack:** MySQL, SQL")

with col2:
    st.markdown("#### Impact")
    st.metric("Founders Tracked", "2,400+", "Centralized database")
    st.metric("Data Accuracy", "92% → 99%", "Quality improvement")
    st.metric("Evaluation Cycles", "33% faster", "SQL workflow optimization")

st.markdown("---")

st.caption("All projects deployed in production across financial markets, enterprise operations, and startup ecosystems | Updated April 2026")
