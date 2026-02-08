# pages/3_Research.py
import streamlit as st

st.set_page_config(page_title="Research", layout="wide", page_icon="📚")

# Custom CSS - Same as Home page
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&family=Inter:wght@400;600;700&display=swap');

.main {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1729 0%, #141b3d 100%);
}

section[data-testid="stSidebarNav"] a {
    color: #ccd6f6;
    font-family: 'DM Sans', sans-serif;
}

section[data-testid="stSidebarNav"] a:hover {
    color: #f4c430;
}

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

div[data-testid="stAlert"] {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    border: 1px solid rgba(244, 196, 48, 0.3);
    border-radius: 12px;
    font-family: 'DM Sans', sans-serif;
}

.stCaption {
    font-family: 'Inter', sans-serif;
    color: #8892b0 !important;
    font-size: 0.9rem !important;
}

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
st.markdown("### The Impact of Supply Chain ESG Performance on Stock Returns and Volatility")
st.caption("**Authors:** Amit Kumar, Sairam Vinay Shetty | Frankfurt School of Finance & Management")
st.caption("**Status:** Ongoing | Expected Completion: August 2026")

# Research Question
st.markdown("### Research Question")
st.write("""
Does supply chain ESG performance, specifically Scope 3 emissions and supplier human rights practices, 
significantly influence stock returns and volatility for European listed firms? Traditional ESG research 
focuses on direct operations (Scope 1 & 2), but supply chains often represent the largest sustainability 
footprint and risk exposure.
""")

st.info("""
**Key Hypothesis:** Companies with stronger supply chain ESG governance should exhibit risk-adjusted 
outperformance due to reduced operational and reputational risks, and lower volatility from improved 
stakeholder relationships and regulatory compliance.
""")

# Methodology
st.markdown("### Methodology Overview")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("# Dependent Variables")
    st.write("• Monthly stock returns (log returns)")
    st.write("• Return volatility (rolling standard deviation)")
    st.write("• Risk-adjusted returns (Sharpe ratio)")
    
    st.markdown("# ESG Variables")
    st.write("• Scope 3 emissions intensity")
    st.write("• Supplier human rights scores")
    st.write("• Supply chain transparency metrics")
    st.write("• Supplier audit frequency")

with col2:
    st.markdown("## Control Variables")
    st.write("• Firm size (market cap, log)")
    st.write("• Book-to-market ratio")
    st.write("• Leverage (debt-to-equity)")
    st.write("• Momentum (12-month returns)")
    st.write("• Sector fixed effects")
    
    st.markdown("## Data Sources")
    st.write("• Refinitiv ESG database")
    st.write("• MSCI ESG ratings")
    st.write("• Bloomberg terminal (pricing)")
    st.write("• STOXX Europe 600 constituents")

# Analytical Approach
st.markdown("## Analytical Approach")

st.write("""
Panel regression analysis with firm and time fixed effects to control for unobserved heterogeneity. 
Testing whether supply chain ESG metrics have explanatory power beyond traditional Fama-French factors 
and direct ESG scores. Robustness checks include lagged variables to address reverse causality and 
industry-specific subgroup analysis.
""")

# Expected Contributions
st.markdown("## Expected Contributions")

st.write("""
This research contributes to the growing literature on ESG materiality by focusing specifically on 
supply chain metrics - an understudied area despite representing 70-80% of most companies' total emissions. 
Findings could inform investor due diligence, corporate sustainability strategies, and regulatory approaches 
to Scope 3 reporting requirements.
""")

st.markdown("---")

# Research Interests
st.markdown("## Research Interests")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Quantitative Finance")
    st.write("• Factor models")
    st.write("• Risk attribution")
    st.write("• Portfolio optimization")

with col2:
    st.markdown("#### Alternative Data")
    st.write("• NLP on earnings calls")
    st.write("• Satellite data for commodities")
    st.write("• Sentiment analysis")

with col3:
    st.markdown("#### Operational Analytics")
    st.write("• Trading desk optimization")
    st.write("• Market microstructure")
    st.write("• Execution algorithms")

st.write("""
Open to research collaborations at the intersection of data science and financial markets.
""")

st.markdown("---")

st.caption("Research updates and working papers will be available upon completion")
