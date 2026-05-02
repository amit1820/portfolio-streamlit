# pages/3_Research.py
import streamlit as st

st.set_page_config(page_title="Research", layout="wide", page_icon="📚")

# Top Navigation - centered
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

# Custom CSS
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
.stButton button { background: transparent; color: #ccd6f6; border: none; font-family: 'DM Sans', sans-serif; font-size: 1rem; font-weight: 500; padding: 0.6rem 1.5rem; border-radius: 6px; transition: all 0.3s ease; }
.stButton button:hover { color: #f4c430; background: rgba(244, 196, 48, 0.1); }
div[data-testid="stAlert"] { background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%); border: 1px solid rgba(244, 196, 48, 0.3); border-radius: 12px; font-family: 'DM Sans', sans-serif; }
.stCaption { font-family: 'Inter', sans-serif; color: #8892b0 !important; font-size: 0.9rem !important; }
a { color: #64ffda; text-decoration: none; }
a:hover { color: #ffd700; text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

st.title("Research & Applied Analytics")

# Master's Thesis
st.markdown("## Master's Thesis")
st.markdown("### Climate Policy Reversal and Global Equity Markets: A Cross-Country Event Study of US Environmental Deregulation (2025–2026)")
st.caption("**Authors:** Amit Kumar, Sairam Vinay Shetty | Frankfurt School of Finance & Management")
st.caption("**Supervisors:** Professor Leonard Nils Grebe (First Assessor), Professor Maria de la O Hervás Zurita (Second Assessor)")
st.caption("**Status:** Draft in progress | Submission: May 2026")

st.markdown("---")

# Research Question
st.markdown("#### Research Question")
st.write("""
Did the four major climate policy reversal events of Trump's second term (January 2025 – February 2026)
generate measurable abnormal returns in global equity markets, and do firm-level characteristics or
regional regulatory environments explain the cross-sectional variation in these reactions?
""")

st.info("""
**Headline finding.** Of the four climate deregulation events studied, only the EPA Proposed Rule
of 1 August 2025 (Event 3) produced a statistically significant negative market reaction. The result is
robust across two independent datasets (Yahoo Finance, Investing.com) and survives in a firm-level
pooled panel regression covering 929 firms across the US, Europe, and Asia, with controls for ROA,
market capitalisation, leverage, sector, and event fixed effects.
""")

st.markdown("---")

# Key Results
st.markdown("## Principal Findings")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Event 3 CAAR", "-1.50%", "p = 0.006 [-1,+1] window")
with col2:
    st.metric("Pooled Event 3 β", "-2.14%", "p < 0.001, firm-level")
with col3:
    st.metric("Firms Analysed", "929", "US 501 / EU 333 / Asia 95")
with col4:
    st.metric("Datasets", "2", "Yahoo + Investing.com")

st.markdown("---")

st.markdown("#### Five Principal Findings")

st.write("""
**1. Single-event significance.** Of four climate deregulation events analysed, only the EPA Proposed
Rule (Event 3, 1 August 2025) generated a statistically significant negative market reaction at the
index level (CAAR[-1,+1] = -1.50%, p = 0.006). The other three events showed no significant abnormal
returns in the primary window.

**2. Anticipation effect.** The final rescission (Event 4, 12 February 2026) produced no significant
reaction despite being described by the EPA as the single largest deregulatory action in US history,
consistent with full market anticipation following Event 3's proposed rule five months earlier.

**3. Cross-source replication.** Independent replication across two data sources produced directionally
identical and statistically consistent results (Yahoo: -1.50%, p = 0.006; Investing.com: -1.37%, p = 0.003),
reinforcing robustness against data-source bias.

**4. Firm-level confirmation.** A pooled panel regression across 929 firms × 4 events (3,592 firm-event
observations) confirms the Event 3 effect (β = -2.14%, p < 0.001) survives controls for ROA, market
capitalisation, leverage, sector fixed effects, and firm-clustered standard errors.

**5. Composition over geography.** The cross-regional differences observed at the index level largely
attenuate once firm characteristics are controlled for. The Event 3 reaction is broad-based across
developed markets, with sector composition and firm fundamentals explaining most of the cross-firm
variation rather than regional location per se.
""")

st.markdown("---")

# Four Events Studied
st.markdown("## Four Policy Events Studied")

events_data = [
    ("Event 1 — 20 Jan 2025", "Inauguration Executive Orders",
     "Paris Agreement withdrawal, IRA spending freeze, national energy emergency declaration",
     "+0.28%", "p = 0.358 (n.s.)"),
    ("Event 2 — 12 Mar 2025", "EPA Zeldin Recommendation",
     "EPA Administrator formally recommends reconsidering the 2009 Endangerment Finding",
     "+0.06%", "p = 0.866 (n.s.)"),
    ("Event 3 — 1 Aug 2025", "EPA Proposed Rule",
     "Federal Register publication of the proposed rule to rescind the Endangerment Finding (570,000+ public comments)",
     "-1.50%", "p = 0.006 ***"),
    ("Event 4 — 12 Feb 2026", "Endangerment Finding Rescission",
     "Final rescission — described by the EPA as the single largest deregulatory action in US history",
     "+0.10%", "p = 0.861 (n.s.)"),
]

for date, title, desc, caar, sig in events_data:
    with st.expander(f"**{date}** — {title} (CAAR[-1,+1]: {caar}, {sig})"):
        st.write(desc)

st.caption("CAARs reported on the [-1,+1] window from the Yahoo Finance dataset. *** p < 0.01.")

st.markdown("---")

# Methodology
st.markdown("## Methodology")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### Event Study Design")
    st.write("• Standard market model with 250-day estimation window (OLS)")
    st.write("• 11 event windows tested: [0], [0,1], [0,2], [-1,1], [-2,2], [-3,3], [-5,5], [-1,5], [-5,10], [-5,-1], [1,5]")
    st.write("• Primary window: [-1,+1]")
    st.write("• Parametric t-test and non-parametric Wilcoxon signed-rank test")
    st.write("• Pre/post-announcement decomposition to test for leakage and drift")

    st.markdown("#### Firm-Level Pooled Regression")
    st.code("""
CAR[-5,+5] = α + β·EventFE + γ·RegionFE
           + δ·SectorFE + ROA + log(MktCap)
           + Leverage + ε

Standard errors clustered by firm.
    """, language=None)

with col2:
    st.markdown("#### Markets & Sample")
    st.write("• **Index-level (N=9):** S&P 500; DAX, FTSE 100, CAC 40, STOXX 600; Nikkei 225, Hang Seng, KOSPI, MSCI Asia-Pacific")
    st.write("• **Firm-level (N=929):** S&P 500 constituents (501); STOXX 600 constituents (333); large-cap Asian sample across Nikkei, Hang Seng, KOSPI (95)")
    st.write("• **Benchmark:** MSCI World")

    st.markdown("#### Data Sources")
    st.write("• **Index returns & firm prices:** Yahoo Finance (Amit) and Investing.com (Sairam) — independent replication")
    st.write("• **Firm fundamentals:** Yahoo Finance (ROA, market capitalisation, sector classification)")

    st.markdown("#### Implementation")
    st.write("• Index-level analysis: **R** (tidyverse, lm, wilcox.test)")
    st.write("• Firm-level extension: **Python** (yfinance, pandas, statsmodels)")
    st.write("• Diagnostics: clustered SE, HC3 robust SE, winsorisation at 1%/99%")

st.markdown("---")

# Index-Level Cross-Sectional Results
st.markdown("## Index-Level Cross-Sectional Results [-1,+1]")

import pandas as pd

idx_data = {
    "Event": ["Event 1 — Inauguration", "Event 2 — Zeldin", "Event 3 — Proposed Rule", "Event 4 — Rescission"],
    "CAAR (Yahoo)": ["+0.28%", "+0.06%", "-1.50%***", "+0.10%"],
    "CAAR (Investing)": ["+0.22%", "+0.16%", "-1.37%***", "+0.32%"],
    "Europe dummy (β, p)": ["-0.39 (0.81)", "-0.03 (0.98)", "-1.70 (0.28)", "+0.38 (0.87)"],
    "Asia dummy (β, p)": ["-0.39 (0.59)", "+0.72 (0.55)", "-1.62 (0.29)", "+0.39 (0.86)"],
}

df_idx = pd.DataFrame(idx_data)
st.dataframe(df_idx, use_container_width=True, hide_index=True)
st.caption("CAARs in the [-1,+1] window. *** p < 0.01. Regional dummies estimated relative to the US (S&P 500) intercept; small index-level cross-section (N=9) limits power on regional differences.")

st.markdown("---")

# Firm-Level Pooled Regression Result
st.markdown("## Firm-Level Pooled Panel Regression")
st.caption("Dependent variable: winsorised CAR[-5,+5]. N = 3,592 firm-event observations. Standard errors clustered by firm.")

fl_data = {
    "Variable": ["Constant", "Event 2 (vs Event 1)", "Event 3 (vs Event 1)", "Event 4 (vs Event 1)",
                 "Region: Europe (vs US)", "Region: Asia (vs US)", "ROA", "log(Market Cap)",
                 "Sector fixed effects", "R-squared"],
    "Coefficient": ["+0.0089", "+0.0017", "-0.0214", "-0.0079", "+0.0011", "-0.0002",
                    "-0.0675", "+0.0008", "Included", "0.039"],
    "p-value": ["0.610", "0.560", "<0.001 ***", "0.013 **", "0.623", "0.972",
                "0.003 ***", "0.224", "—", "—"],
}

df_fl = pd.DataFrame(fl_data)
st.dataframe(df_fl, use_container_width=True, hide_index=True)
st.caption("*** p < 0.01, ** p < 0.05. Event 3 effect (-2.14%) is the largest and most significant coefficient; "
           "regional dummies are not significant once firm characteristics and sector fixed effects are included.")

st.markdown("---")

# Implications
st.markdown("## Implications and Interpretation")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### Why Event 3?")
    st.write("""
    Event 3 was the only event in the sequence with concrete, legally binding regulatory content —
    the formal Federal Register publication initiating the 60-day notice-and-comment period. Events 1
    and 2 conveyed political intent; Event 4 ratified what Event 3 had already proposed. Markets price
    legal commitment, not rhetoric.
    """)

with col2:
    st.markdown("#### Composition vs. geography")
    st.write("""
    The index-level finding of larger non-US reactions weakens substantially in the firm-level regression
    once sector composition is controlled for. The Event 3 reaction appears to operate primarily through
    sector-level channels (notably interactions with profitability and industry exposure) rather than
    through cross-jurisdictional regulatory differentials.
    """)

st.markdown("---")

# Limitations and Future Research
st.markdown("## Limitations and Future Research")

st.write("""
The firm-level extension is constrained by sample size (929 firms) and the absence of climate-specific
firm characteristics (carbon intensity, green revenue share, ESG quality scores). Future work could
substantially expand the sample with point-in-time index constituents from Bloomberg or Refinitiv,
incorporate carbon-emissions data from CDP or MSCI ESG, and test interaction terms between event dummies
and firm-level climate exposure to better identify the channels driving the Event 3 reaction. The
single-country focus of the policy events also limits external validity; comparable studies of climate
policy reversal in other major regulatory regimes would strengthen generalisability.
""")

st.markdown("---")

# Key Literature
st.markdown("## Key Literature")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.write("• **Aras, Grebe & Schiereck (2025)** — CDP A-List event study methodology (primary methodological reference)")
    st.write("• **Koch & Schiereck (2025)** — Trump 2024 election impact using green revenue share classification")
    st.write("• **Ramelli et al. (2021)** — Trump 2016 election: carbon-intensive firms in the short-run")
    st.write("• **Bolton & Kacperczyk (2023)** — Global carbon premium across 77 countries")

with col2:
    st.write("• **Pástor & Veronesi (2012, 2013)** — Political uncertainty and risk premia framework")
    st.write("• **Ahmad et al. (2025)** — G20 country-level reactions to sequential Trump events")
    st.write("• **Martins et al. (2025)** — Cross-market renewable-energy reactions to the 2024 US election")
    st.write("• **Mukanjari & Sterner (2024)** — Paris Agreement and Trump effects on energy stocks")

st.markdown("---")

# Research Interests
st.markdown("## Research Interests")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Quantitative Finance")
    st.write("• Event study methodology")
    st.write("• Factor models and risk attribution")
    st.write("• Climate policy uncertainty pricing")

with col2:
    st.markdown("#### ESG and Sustainable Finance")
    st.write("• Carbon premium dynamics")
    st.write("• Regulatory divergence effects")
    st.write("• Cross-market ESG transmission")

with col3:
    st.markdown("#### Data-Driven Analytics")
    st.write("• Financial econometrics in R and Python")
    st.write("• Market microstructure analysis")
    st.write("• Statistical modelling and outlier detection")

st.write("""
Open to research collaborations at the intersection of data science, climate finance, and international
financial markets.
""")

st.markdown("---")

st.caption("Full thesis manuscript and replication code will be made available upon submission and approval.")
