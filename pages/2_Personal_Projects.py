# pages/2_Personal_Projects.py
import streamlit as st
from components import project_card

st.title("Personal Analytics Projects")
st.write("Personal work that demonstrates analytical rigor, pipeline thinking and interactive visualization.")

# Interactive BI Analytics App (In Progress)
project_card(
    title="Interactive BI Analytics App",
    subtitle="Streamlit · Pandas · Plotly",
    context="Interactive dashboard exploring business KPIs with filters and executive summary.",
    solution="Streamlit UI with KPI cards, filters, time-series and CSV export. Built to be user-friendly and easy to adapt.",
    impact_lines=["Focus on clear decision-oriented visuals and stakeholder-friendly export."],
    tools="Streamlit, pandas, plotly",
    status="In Progress",
    repo_link="https://github.com/amit1820/interactive-bi-analytics-app"
)

# End-to-End Analytics Pipeline (In Progress)
project_card(
    title="End-to-End Analytics Pipeline",
    subtitle="Python · Pandas · ETL scripts",
    context="A reproducible pipeline from raw ingestion to aggregated outputs and dashboards.",
    solution="Scripted ETL, tests for core transformations, and a final simple dashboard to present outputs.",
    impact_lines=["Emphasizes reproducibility, logging, and clear folder structure."],
    tools="Python, pandas, pytest (for checks)",
    status="In Progress",
    repo_link="https://github.com/amit1820/end-to-end-analytics-pipeline"
)

# BI Realism
project_card(
    title="BI Realism — From Messy Data to Decision-Ready Output",
    subtitle="Python · Pandas · Time-Series",
    context="Transactional data with inconsistent date formats and missing values prevented reliable KPIs.",
    solution="Standardized dates, filled/filtered missing values, and aggregated monthly KPIs for business review.",
    impact_lines=["Cleaned monthly summary dataset", "Time-series visualization of total transaction volume"],
    tools="Python (pandas)",
    status="Completed",
)

# Automated Data Reconciliation
project_card(
    title="Automated Data Reconciliation & Exception Reporting",
    subtitle="Python · Data Validation",
    context="Two ledgers required weekly reconciliation; manual checks missed edge cases.",
    solution="Joined datasets on transaction ID, labeled matches/mismatches, and exported exception reports for follow-up.",
    impact_lines=["Reconciled dataset with status labels", "Separate exception file for investigations"],
    tools="Python, pandas",
    status="Completed",
)
