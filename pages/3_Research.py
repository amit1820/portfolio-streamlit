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

/* Hide sidebar completely */
[data-testid="stSidebar"] {
    display: none;
}

section[data-testid="stSidebarNav"] {
    display: none;
}

/* Remove default padding */
.main > div {
    padding-top: 0rem;
}

/* Main background */
.main {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Typography */
div[data-testid="stMarkdownContainer"] h1 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
    font-size: 3rem;
    margin-bottom: 0.5rem;
    letter-spacing: -1px;
}

div[data-testid="stMarkdownContainer"] h2 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
    font-size: 2rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
    letter-spacing: -0.5px;
}

div[data-testid="stMarkdownContainer"] h3 {
    font-family: 'Inter', sans-serif;
    color: #64ffda;
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}

div[data-testid="stMarkdownContainer"] h4 {
    font-family: 'Inter', sans-serif;
    color: #ffd700;
    font-size: 1.1rem;
    font-weight: 600;
    margin-top: 1rem;
}

div[data-testid="stMarkdownContainer"] p {
    font-family: 'DM Sans', sans-serif;
    color: #ccd6f6;
    line-height: 1.8;
    font-size: 1.05rem;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.08) 0%, rgba(20, 27, 61, 0.4) 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid rgba(244, 196, 48, 0.2);
}

div[data-testid="stMetricLabel"] {
    font-family: 'Space Mono', monospace;
    color: #f4c430 !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

div[data-testid="stMetricValue"] {
    font-family: 'Space Mono', monospace;
    color: #ffffff !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricDelta"] {
    font-family: 'DM Sans', sans-serif;
    color: #a8b2d1 !important;
    font-size: 0.85rem !important;
}

/* Download button */
.stDownloadButton button {
    background: linear-gradient(135deg, #f4c430 0%, #ffd700 100%);
    color: #0a0e27 !important;
    font-family: 'Space Mono', monospace;
    font-weight: 700 !important;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 8px;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.stDownloadButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(244, 196, 48, 0.4);
    background: #ffd700;
}

.stDownloadButton button p {
    color: #0a0e27 !important;
    font-weight: 700 !important;
}

/* Navigation buttons - stylish version */
.stButton button {
    background: transparent;
    color: #ccd6f6;
    border: none;
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 500;
    padding: 0.6rem 1.5rem;
    border-radius: 6px;
    transition: all 0.3s ease;
    position: relative;
}

.stButton button:hover {
    color: #f4c430;
    background: rgba(244, 196, 48, 0.1);
    transform: translateY(-2px);
}

.stButton button::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%) scaleX(0);
    width: 80%;
    height: 2px;
    background: #f4c430;
    transition: transform 0.3s ease;
}

.stButton button:hover::after {
    transform: translateX(-50%) scaleX(1);
}

/* Info box */
div[data-testid="stAlert"] {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    border: 1px solid rgba(244, 196, 48, 0.3);
    border-radius: 12px;
    font-family: 'DM Sans', sans-serif;
}

/* Caption */
.stCaption {
    font-family: 'Inter', sans-serif;
    color: #8892b0 !important;
    font-size: 0.9rem !important;
}

/* Links */
a {
    color: #64ffda;
    text-decoration: none;
}

a:hover {
    color: #ffd700;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

st.title("Research & Applied Analytics")

# Master's Thesis
st.markdown("## Master's Thesis")
st.markdown("### Climate Policy Reversal and Global Equity Markets: A Cross-Country Event Study of US Environmental Deregulation (2025–2026)")
st.caption("**Authors:** Amit Kumar, Sairam Vinay Shetty | Frankfurt School of Finance & Management")
st.caption("**Supervisors:** Leonard Nils Grebe, Maria de la O Hervás Zurita")
st.caption("**Status:** Ongoing | Expected Completion: May 2026")

# Research Question
st.markdown("#### Research Question")
st.write("""
Did Trump's second-term climate policy rollback events (2025–2026) generate significantly different 
stock market reactions across US, European, and Asian markets? And do these differences reflect 
regional regulatory environments — particularly the divergence between US deregulation and Europe's 
strengthening climate framework (CSRD, CSDDD, SFDR)?
""")

st.info("""
**Key Hypothesis:** Trump's climate policy rollback events generated significantly negative (positive) 
abnormal returns for green (brown) firms in US markets, while European firms exhibited a different pattern — 
green European firms were less negatively affected due to the EU's continued climate regulation commitment, 
reflecting a "regulatory safe haven" effect.
""")

# Methodology
st.markdown("#### Methodology Overview")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### Event Study Design")
    st.write("• Market model with 250-day estimation window")
    st.write("• Cumulative Abnormal Returns (CARs) across multiple event windows")
    st.write("• Parametric t-test & non-parametric Wilcoxon signed-rank test")
    st.write("• Cross-sectional OLS regression with regional interaction terms")
    
    st.markdown("#### Key Policy Events Analyzed")
    st.write("• Jan 20, 2025 — Paris withdrawal, IRA freeze, energy emergency declaration")
    st.write("• Mar 2025 — EPA endangerment finding reconsideration")
    st.write("• Apr 2025 — Coal industry support, state climate policy attacks")
    st.write("• Jun 2025 — IRA tax credit restrictions")
    st.write("• Feb 11, 2026 — EPA formally rescinds endangerment finding")

with col2:
    st.markdown("#### Markets & Indices")
    st.write("• **US:** S&P 500")
    st.write("• **Europe:** DAX (Germany), FTSE 100 (UK), CAC 40 (France)")
    st.write("• **Asia:** Nikkei 225 (Japan), Hang Seng (Hong Kong), KOSPI (South Korea)")
    st.write("• **Benchmark:** MSCI World")
    
    st.markdown("#### Data Sources")
    st.write("• Bloomberg Terminal (daily index returns)")
    st.write("• Refinitiv Eikon (ESG scores, green revenue share)")
    st.write("• Kenneth French Data Library (Fama-French factors)")
    st.write("• LSEG (green revenue classification)")

# Analytical Approach
st.markdown("#### Analytical Approach")

st.write("""
Short-term event study methodology following the market model approach (Brown & Warner, 1985). For each 
event date, abnormal returns are calculated as the difference between actual returns and expected returns 
estimated via OLS regression over a 250-trading-day window ending 10 days before the event. CARs are 
computed across multiple windows ([-1,+1], [-2,+2], [-5,+5]) and tested for statistical significance.
""")

st.write("""
The cross-sectional regression tests whether regional regulatory environments moderate market reactions:
""")

st.code("""
CAR = α + β₁(Green) + β₂(Europe) + β₃(Asia) + β₄(Green×Europe) + β₅(Green×Asia) + Controls + ε

Where interaction terms β₄ and β₅ test whether green firms in Europe/Asia reacted 
differently from US green firms — the novel contribution of this study.
""", language=None)

st.write("""
Robustness checks include alternative factor models (Fama-French 3-factor and 5-factor), 
varying event windows, sector sub-samples, and multi-event aggregation following 
Conte Grand & D'Elia (2021).
""")

# Expected Contributions
st.markdown("#### Expected Contributions")

st.write("""
This research contributes novel insights at the intersection of climate policy and international financial 
markets. While existing studies examine US markets in isolation (Koch & Schiereck, 2025) or focus solely 
on the energy sector (Mukanjari & Sterner, 2024), this is the first study to analyze Trump's second-term 
(2025–2026) climate rollbacks across three major economic regions simultaneously. The cross-market 
comparison tests whether the same policy shock is priced differently across regulatory regimes — 
contributing to the Bolton & Kacperczyk (2023) carbon premium literature and the Pástor & Veronesi (2013) 
climate policy uncertainty framework.
""")

# Key Literature
st.markdown("#### Key Literature")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.write("• **Koch & Schiereck (2025)** — Trump 2024 election impact on US stocks using green revenue share")
    st.write("• **Ramelli et al. (2021)** — Trump 2016 election: carbon-intensive firms rewarded short-term")
    st.write("• **Bolton & Kacperczyk (2023)** — Global carbon premium across 77 countries")
    st.write("• **Mukanjari & Sterner (2024)** — Paris Agreement & Trump effects on energy stocks")

with col2:
    st.write("• **Pástor & Veronesi (2013)** — Political uncertainty and risk premia framework")
    st.write("• **Wagner et al. (2023)** — IRA event study on green firm valuations")
    st.write("• **Conte Grand & D'Elia (2021)** — 19 Trump first-term policy events, 49 US industries")
    st.write("• **Yun et al. (2023)** — US elections affect global stock volatility for climate-exposed firms")

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
    st.write("• Alternative data for alpha generation")

st.write("""
Open to research collaborations at the intersection of data science, climate finance, and international 
financial markets.
""")

st.markdown("---")

st.caption("Research updates and working papers will be available upon completion. Target publication: JUMS (Junior Management Science) & Finance Research Letters.")
