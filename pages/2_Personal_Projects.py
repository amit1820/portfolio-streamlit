import streamlit as st

page_md = """
# Personal Analytics Projects

These are projects I built to demonstrate analytical rigor, production thinking and visualization.

## Interactive BI Analytics App *(In Progress)*
Interactive Streamlit dashboard for business KPI exploration. Features: filters, KPI cards, time-series trends, and CSV export. *(Repo: https://github.com/amit1820/interactive-bi-analytics-app)*

## End-to-End Analytics Pipeline *(In Progress)*
A scripted ETL that goes from raw data to aggregated output and a simple dashboard. Will include reproducible scripts and a clear folder structure. *(Repo: https://github.com/amit1820/end-to-end-analytics-pipeline)*

## BI Realism – From Messy Data to Decision-Ready Output *(Completed)*
- Cleaned inconsistent dates and missing values using pandas  
- Produced normalized monthly summary dataset and time-series visuals  
- Future: add data validation and schedule refreshes

## Automated Data Reconciliation & Exception Reporting *(Completed)*
- Merged ledgers on transaction IDs, flagged exceptions, produced an investigation file  
- Future: automated alerts and historical anomaly monitoring
"""
st.markdown(page_md, unsafe_allow_html=True)
