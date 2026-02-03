# pages/1_Industry_Case_Studies.py
import streamlit as st
from components import project_card

st.title("Industry & Professional Case Studies")
st.write("These projects reflect hands-on delivery of analytics and automation in production environments. (Source: Work Reference.)")

# 1 — AI-Powered Document Verification
project_card(
    title="AI-Powered Document Verification",
    subtitle="Python · OpenCV · OCR · Automation",
    context="The team manually verified ~400 compliance PDFs/month for stamps and signatures; a slow and error-prone process. :contentReference[oaicite:1]{index=1}",
    solution="Built an automated verification pipeline using OpenCV and OCR (PyMuPDF/Tesseract). The pipeline flagged exceptions for review, automating routine checks.",
    impact_lines=[
        "Automated validation of ~400 PDFs/month.",
        "Reduced manual review effort by ~80% (~40 hours/month)."
    ],
    tools="Python, OpenCV, PyMuPDF, scikit-image, Tesseract",
    status="Completed",
)

# 2 — Power Automate: File Renaming & Ticket Tracking
project_card(
    title="Power Automate — File Renaming & Ticket Tracking",
    subtitle="Power Automate · Excel · Power Query",
    context="Daily manual renaming of ~480 financial files and updating ~20 Jira tickets/day. :contentReference[oaicite:2]{index=2}",
    solution="Designed Power Automate flows with AI content recognition and rule-based renaming; automated Excel updates for ticket tracking.",
    impact_lines=[
        "Automated ~480 file renames/month.",
        "Reduced manual errors by ~85% and saved ~80 hours/month."
    ],
    tools="Power Automate, Excel, Power Query",
    status="Completed",
)

# 3 — Real-Time Trading Dashboards
project_card(
    title="Real-Time Trading Dashboards",
    subtitle="Power BI · Apache Zeppelin · Scala · SQL",
    context="Traders needed live, interactive reporting; current reports were static and fragmented. :contentReference[oaicite:3]{index=3}",
    solution="Built Power BI dashboards integrated with Apache Zeppelin and Scala scripts for near real-time KPI visualization.",
    impact_lines=[
        "Provided live visibility into trading KPIs and improved decision-making."
    ],
    tools="Power BI, Apache Zeppelin, Scala, SQL",
    status="Completed",
)

# 4 — Excel-Based Data Reconciliation
project_card(
    title="Excel-Based Data Reconciliation & Validation",
    subtitle="Power Query · VBA",
    context="30+ CSV files daily across trading DBs (~1.9M rows/month) required reconciliation. :contentReference[oaicite:4]{index=4}",
    solution="Implemented Power Query + VBA automation to reconcile and validate CSVs, standardize reporting and automate checks.",
    impact_lines=[
        "Reduced reconciliation time by ~45 hrs/month.",
        "Cut data defects by ~40%."
    ],
    tools="Excel (Power Query M), VBA",
    status="Completed",
)
