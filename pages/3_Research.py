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
st.caption("**Status:** Final draft completed | Submission: May 2026")
st.caption("**Target publication:** JUMS (Junior Management Science) & Finance Research Letters")

st.markdown("---")

# Research Question
st.markdown("#### Research Question")
st.write("""
Did Trump's second-term climate policy rollback events (2025–2026) generate significantly different 
stock market reactions across US, European, and Asian markets? And do these differences reflect 
regional regulatory environments — particularly the divergence between US deregulation and Europe's 
strengthening climate framework (CSRD, CSDDD, SFDR)?
""")

st.info("""
**Key Finding: The "Regulatory Safe Haven" Effect.** Non-US markets became progressively insulated 
from US climate policy shocks over the 13-month study period. The Europe regression dummy increased 
from +1.84 (p = 0.020) in Event 1 to +2.53 (p = 0.038) in Event 4, while Asia moved from +1.39 
(p = 0.056) to +2.42 (p = 0.044) — with Japan's Nikkei 225 and South Korea's KOSPI reaching 
effectively zero abnormal returns by the final event.
""")

st.markdown("---")

# Key Results
st.markdown("## Principal Findings")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("US Market (S&P 500)", "-3.1%", "CAR across all 4 events")
with col2:
    st.metric("Europe Mean CAR", "-1.22% → -0.66%", "Progressive insulation")
with col3:
    st.metric("Asia Mean CAR", "-1.67% → -0.77%", "Nikkei/KOSPI → ~0%")
with col4:
    st.metric("R-squared", "56–63%", "Region explains CAR variation")

st.markdown("---")

st.markdown("#### Five Principal Findings")

st.write("""
**1. Significant negative global reactions.** All four events generated statistically significant negative 
CAARs across global equity markets, confirmed by both parametric t-tests and non-parametric Wilcoxon 
signed-rank tests (p < 0.01 for Events 1-3, p < 0.05 for Event 4).

**2. US consistently most affected.** The S&P 500 experienced CARs of approximately -3.1% in the [-1,1] 
window across all four events — remarkably stable despite the events spanning 13 months.

**3. European insulation.** European markets (DAX, FTSE 100, CAC 40, STOXX 600) experienced significantly 
smaller reactions, with mean CARs declining from -1.22% in Event 1 to -0.66% in Event 4.

**4. Asian decoupling.** The most dramatic evolution — Japan's Nikkei 225 and South Korea's KOSPI reached 
essentially zero abnormal returns by Event 4, indicating complete decoupling from US climate policy.

**5. ETF sentiment amplification.** The US-listed MSCI Asia Pacific ETF maintained large negative CARs 
of ~-2.5% across all events despite actual Asian indices converging toward zero — reflecting US investor 
sentiment rather than actual Asian market conditions.
""")

st.markdown("---")

# Four Events Studied
st.markdown("## Four Policy Events Studied")

events_data = [
    ("Event 1 — 20 Jan 2025", "Inauguration Executive Orders", 
     "Paris withdrawal, IRA freeze, energy emergency declaration", "-1.625%"),
    ("Event 2 — 12 Mar 2025", "EPA Zeldin Recommendation", 
     "EPA Administrator recommends reconsidering Endangerment Finding", "-1.663%"),
    ("Event 3 — 1 Aug 2025", "EPA Proposed Rule", 
     "Proposed rule to rescind the Endangerment Finding", "-1.126%"),
    ("Event 4 — 12 Feb 2026", "Endangerment Finding Rescission", 
     "Final rescission — EPA calls it 'the single largest deregulatory action in US history'", "-0.995%"),
]

for date, title, desc, caar in events_data:
    with st.expander(f"**{date}** — {title} (CAAR: {caar})"):
        st.write(desc)

st.markdown("---")

# Methodology
st.markdown("## Methodology")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### Event Study Design")
    st.write("• Market model with 250-day estimation window (OLS)")
    st.write("• 9 event windows: [0], [0,1], [0,2], [-1,1], [-2,2], [-3,3], [-5,5], [-1,5], [-5,10]")
    st.write("• Primary window: [-1,1]")
    st.write("• Parametric t-test & non-parametric Wilcoxon signed-rank test")
    st.write("• Cross-sectional OLS regression with regional dummy variables")
    
    st.markdown("#### Cross-Sectional Regression Model")
    st.code("""
CAR = α + β₁(Europe) + β₂(Asia) + ε

Where:
  α (intercept) = US market reaction (reference)
  β₁ = Europe differential vs US
  β₂ = Asia differential vs US
    """, language=None)

with col2:
    st.markdown("#### Markets & Indices (N=9)")
    st.write("• **US:** S&P 500")
    st.write("• **Europe:** DAX, FTSE 100, CAC 40, EURO STOXX 600")
    st.write("• **Asia:** Nikkei 225, Hang Seng, KOSPI, MSCI Asia Pacific")
    st.write("• **Benchmark:** MSCI World")
    
    st.markdown("#### Data Sources")
    st.write("• Bloomberg Terminal (daily index returns)")
    st.write("• Refinitiv Eikon (ESG scores)")
    st.write("• Kenneth French Data Library (Fama-French factors)")
    st.write("• LSEG (green revenue classification)")

    st.markdown("#### Implementation")
    st.write("• All analysis conducted in **R**")
    st.write("• OLS estimation, parametric & non-parametric testing")
    st.write("• Diagnostic checks: Shapiro-Wilk, VIF, Cook's distance")

st.markdown("---")

# Cross-Sectional Results Table
st.markdown("## Cross-Sectional Regression Results [-1,1] Window")

import pandas as pd

reg_data = {
    "Variable": ["Intercept (US)", "Europe dummy", "Asia dummy", "R-squared", "Adj. R-squared"],
    "Event 1": ["-3.062***", "+1.840**", "+1.392*", "0.625", "0.500"],
    "Event 2": ["-3.114***", "+1.805**", "+1.461*", "0.603", "0.471"],
    "Event 3": ["-3.193***", "+2.447**", "+2.204**", "0.633", "0.511"],
    "Event 4": ["-3.199***", "+2.534**", "+2.425**", "0.563", "0.417"],
}

df = pd.DataFrame(reg_data)
st.dataframe(df, use_container_width=True, hide_index=True)
st.caption("*, **, *** indicate significance at 10%, 5%, 1% levels. Standard errors omitted for brevity.")

st.markdown("---")

# Regional CAR Table
st.markdown("## Mean CARs by Region [-1,1] Window")

car_data = {
    "Region": ["US (S&P 500)", "Europe (mean of 4)", "Asia (mean of 4)"],
    "Event 1": ["-3.062%", "-1.222%", "-1.670%"],
    "Event 2": ["-3.114%", "-1.309%", "-1.653%"],
    "Event 3": ["-3.193%", "-0.746%", "-0.989%"],
    "Event 4": ["-3.199%", "-0.664%", "-0.774%"],
}

df2 = pd.DataFrame(car_data)
st.dataframe(df2, use_container_width=True, hide_index=True)

st.markdown("---")

# Implications
st.markdown("## Implications")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### For Investors")
    st.write("""
    Geographic diversification across regulatory regimes provides meaningful insulation from 
    single-country policy risk. The climate governance framework of a jurisdiction is a relevant 
    factor in assessing market resilience — not just firm-level ESG scores.
    """)

with col2:
    st.markdown("#### For Policymakers")
    st.write("""
    Unilateral climate policy reversal primarily imposes costs on the domestic market rather than 
    undermining climate commitments globally. Durable, legally embedded climate governance frameworks 
    — as exemplified by the EU's CSRD/CSDDD/SFDR — provide tangible economic stability benefits 
    that investors recognise and price.
    """)

st.markdown("---")

# Key Literature
st.markdown("## Key Literature")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.write("• **Aras, Grebe & Schiereck (2025)** — CDP A-List event study methodology (our primary reference)")
    st.write("• **Koch & Schiereck (2025)** — Trump 2024 election impact using green revenue share")
    st.write("• **Ramelli et al. (2021)** — Trump 2016 election: carbon-intensive firms rewarded short-term")
    st.write("• **Bolton & Kacperczyk (2023)** — Global carbon premium across 77 countries")

with col2:
    st.write("• **Pástor & Veronesi (2012, 2013)** — Political uncertainty and risk premia framework")
    st.write("• **Baker, Bloom & Davis (2016)** — Economic Policy Uncertainty index")
    st.write("• **Martins et al. (2025)** — 2024 US election: cross-market renewable energy reactions")
    st.write("• **Mukanjari & Sterner (2024)** — Paris Agreement & Trump effects on energy stocks")

st.markdown("---")

# Research Interests
st.markdown("## Research Interests")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Quantitative Finance")
    st.write("• Event study methodology")
    st.write("• Factor models & risk attribution")
    st.write("• Climate policy uncertainty pricing")

with col2:
    st.markdown("#### ESG & Sustainable Finance")
    st.write("• Carbon premium dynamics")
    st.write("• Regulatory divergence effects")
    st.write("• Cross-market ESG transmission")

with col3:
    st.markdown("#### Data-Driven Analytics")
    st.write("• Financial econometrics in R & Python")
    st.write("• Market microstructure analysis")
    st.write("• Statistical modelling & outlier detection")

st.write("""
Open to research collaborations at the intersection of data science, climate finance, and international 
financial markets.
""")

st.markdown("---")

st.caption("Research updates and working papers will be available upon completion. Target publication: JUMS (Junior Management Science) & Finance Research Letters.")
