# pages/1_Industry_Case_Studies.py - UPDATED
import streamlit as st

st.set_page_config(page_title="Industry Case Studies", layout="wide", page_icon="💼")

# [Navigation and CSS code remains the same as your original]

# Page Title
st.title("Industry Case Studies")
st.markdown("### Professional work across Deutsche Börse Group, Arcadis, Alliant Advisory, and Atal Incubation Centre")
st.write("""
Production analytics solutions, automation pipelines, and real-time dashboards deployed 
in financial markets, enterprise operations, and startup ecosystems.
""")

st.markdown("---")

# Project 1 - Eurex
st.markdown("## Power BI Dashboard for Commercial Sales Team")
st.caption("**Eurex (Deutsche Börse Group)** | Jan 2026 - Present")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Commercial sales team relied on static Excel reports for client performance tracking across 
    derivatives products. Reports were rarely updated and lacked interactivity, limiting real-time 
    decision-making capabilities.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Designing and deploying interactive Power BI dashboard to track client performance across 
    derivatives products. Automating 20+ hours/month of recurring BAU tasks using Python and VBA, 
    including Most Liquid Products lists and interactive chart updates. Extracting and structuring 
    trading data from StatistiX database using SQL across TRF, FTSE 100, and ESG segments.
    """)
    
    st.caption("**Tech Stack:** Power BI, Python, VBA, SQL")

with col2:
    st.markdown("#### Impact")
    st.metric("Time Saved", "20+ hrs/month", "Automation")
    st.metric("Status", "In Progress", "Current project")

st.markdown("---")

# Project 2
st.markdown("## Computer Vision-Based Document Verification")
st.caption("**Deutsche Börse AG** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Compliance team manually verified 400+ regulatory PDFs each month for stamps and signatures. 
    Manual process took 2-3 minutes per document and was prone to visual fatigue errors.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Developed computer vision-based verification tool using Python with OpenCV for stamp detection 
    and PyMuPDF for document processing. System automatically detects required elements and flags 
    exceptions for manual review.
    """)
    
    st.caption("**Tech Stack:** Python, OpenCV, PyMuPDF")

with col2:
    st.markdown("#### Impact")
    st.metric("Documents/Month", "400+", "Automated")
    st.metric("Time Saved", "20+ hrs/month", "50%+ reduction")
    st.metric("Error Reduction", "50%+", "Manual errors")

st.markdown("---")

# Project 3
st.markdown("## Power Automate Workflows for Cash Market Operations")
st.caption("**Deutsche Börse AG** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Cash market operations involved manual file processing and data entry across multiple systems. 
    Repetitive tasks consumed significant analyst time and introduced manual errors.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Engineered rule-based automation workflows using Power Automate with AI Builder for content recognition. 
    Automated reconciliation of 500K+ rows/month using Power Query and VBA, resolving inconsistent date 
    formats and field mappings across upstream trading systems.
    """)
    
    st.caption("**Tech Stack:** Power Automate, AI Builder, Power Query, VBA")

with col2:
    st.markdown("#### Impact")
    st.metric("Rows Reconciled", "500K+/month", "Automated")
    st.metric("Time Saved", "20+ hrs/month", "Workflow automation")
    st.metric("Data Defects", "30% reduction", "Quality improvement")

st.markdown("---")

# Project 4
st.markdown("## Real-Time Trading Analytics Dashboards")
st.caption("**Deutsche Börse AG** | July 2025 - Dec 2025")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Traders relied on static reports and ad-hoc data requests for analytics. No unified view of 
    trading KPIs led to information fragmentation and delayed decision-making.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Designed and deployed live Power BI dashboards integrating Scala and Apache Zeppelin data sources 
    for real-time trading analytics. Dashboards replaced ad-hoc report requests and provide traders 
    with self-service access to key metrics.
    """)
    
    st.caption("**Tech Stack:** Power BI, Apache Zeppelin, Scala, SQL")

with col2:
    st.markdown("#### Impact")
    st.metric("Adoption Rate", "Daily usage", "Traders check dashboards")
    st.metric("Ad-hoc Requests", "Significant reduction", "Self-service analytics")

st.markdown("---")

# Project 5 - Arcadis
st.markdown("## Power BI Dashboards for Project KPI Tracking")
st.caption("**Arcadis** | Aug 2022 - July 2024")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Project teams needed real-time visibility into KPIs and resource allocation. 
    Manual reporting processes created delays in project tracking and decision-making.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Built Power BI dashboards and Power Apps for real-time project KPI tracking and resource management. 
    Automated data validation and transformation pipelines using Python, VBA, and Dynamo. Led cross-functional 
    data automation initiatives reducing manual approval time by 2 days per project.
    """)
    
    st.caption("**Tech Stack:** Power BI, Power Apps, Python, VBA, Dynamo")

with col2:
    st.markdown("#### Impact")
    st.metric("Processing Time", "60% reduction", "Manual work eliminated")
    st.metric("Approval Time", "2 days saved", "Per project")

st.markdown("---")

# Project 6 - Alliant Advisory
st.markdown("## Excel-Based Analytics for Cost Segregation")
st.caption("**Alliant Advisory** | Feb 2022 - July 2022")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Cost segregation projects across 12+ clients required consistent analysis of large financial datasets. 
    Manual reporting processes created inefficiencies and inconsistencies in deliverables.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Analyzed and structured large financial datasets for cost segregation analysis. Created standardized 
    reporting templates and automated workflows using Excel VBA and Python. Developed analytics tools and 
    dashboards to track project performance metrics.
    """)
    
    st.caption("**Tech Stack:** Excel, VBA, Python")

with col2:
    st.markdown("#### Impact")
    st.metric("Projects", "12+ clients", "Served")
    st.metric("Turnaround Time", "28% reduction", "Process improvement")

st.markdown("---")

# Project 7 - Atal Incubation Centre
st.markdown("## MySQL Database & Performance Dashboards")
st.caption("**Atal Incubation Centre - Bihar Vidyapith** | Jan 2021 - Jan 2022")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Context")
    st.write("""
    Startup incubation program needed centralized database for tracking 2,400+ founders and their 
    applications. Manual processes led to data inconsistencies and inefficient screening workflows.
    """)
    
    st.markdown("#### Solution")
    st.write("""
    Built and maintained MySQL databases of 2,400+ founders, improving data accuracy from 92% to 99%. 
    Streamlined SQL-based screening workflows, shortening startup evaluation cycles by 33%. Designed 
    performance tracking dashboards to monitor portfolio metrics and support data-driven program management.
    """)
    
    st.caption("**Tech Stack:** MySQL, SQL, Dashboard Tools")

with col2:
    st.markdown("#### Impact")
    st.metric("Founders Tracked", "2,400+", "Database")
    st.metric("Data Accuracy", "92% → 99%", "Quality improvement")
    st.metric("Evaluation Time", "33% faster", "Process efficiency")

st.markdown("---")

st.caption("All projects deployed in production environments across financial markets, enterprise operations, and startup ecosystems")
