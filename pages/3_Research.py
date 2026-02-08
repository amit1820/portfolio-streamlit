# pages/3_Research.py
import streamlit as st

st.set_page_config(page_title="Research", layout="wide", page_icon="📚")

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');

.main {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}

div[data-testid="stMarkdownContainer"] h1 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
}

div[data-testid="stMarkdownContainer"] h2 {
    font-family: 'Space Mono', monospace;
    color: #f4c430;
    font-size: 1.5rem;
}

div[data-testid="stMarkdownContainer"] h3 {
    font-family: 'Space Mono', monospace;
    color: #8892b0;
    font-size: 1.1rem;
}

div[data-testid="stMarkdownContainer"] p {
    font-family: 'DM Sans', sans-serif;
    color: #ccd6f6;
    line-height: 1.7;
}

.stApp {
    background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
}
</style>
""", unsafe_allow_html=True)

st.title("Research & Applied Analytics")
st.markdown("""
**Academic research at Frankfurt School of Finance & Management**  
Applying quantitative methods to explore ESG factors in supply chains and equity market dynamics.
""")

st.markdown("---")

# Master's Thesis
st.subheader("Master's Thesis")
st.markdown("**The Impact of Supply Chain ESG Performance on Stock Returns and Volatility**")
st.caption("Authors: Amit Kumar, Sairam Vinay Shetty | Frankfurt School of Finance & Management")
st.markdown("**Status:** Ongoing | Expected Completion: August 2026")

st.markdown("**Research Question**")
st.write("""
Does supply chain ESG performance, specifically Scope 3 emissions and supplier human rights practices, 
significantly influence stock returns and volatility for European listed firms? Traditional ESG research 
focuses on direct operations (Scope 1 & 2), but supply chains often represent the largest sustainability 
footprint and risk exposure.
""")

st.markdown("**Key Hypothesis**")
st.info("""
Companies with stronger supply chain ESG governance should exhibit risk-adjusted outperformance 
due to reduced operational and reputational risks, and lower volatility from improved stakeholder 
relationships and regulatory compliance.
""")

st.markdown("**Methodology Overview**")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Dependent Variables**")
    st.write("- Monthly stock returns (log returns)")
    st.write("- Return volatility (rolling standard deviation)")
    st.write("- Risk-adjusted returns (Sharpe ratio)")
    
    st.markdown("**ESG Variables**")
    st.write("- Scope 3 emissions intensity")
    st.write("- Supplier human rights scores")
    st.write("- Supply chain transparency metrics")
    st.write("- Supplier audit frequency")

with col2:
    st.markdown("**Control Variables**")
    st.write("- Firm size (market cap, log)")
    st.write("- Book-to-market ratio")
    st.write("- Leverage (debt-to-equity)")
    st.write("- Momentum (12-month returns)")
    st.write("- Sector fixed effects")
    
    st.markdown("**Data Sources**")
    st.write("- Refinitiv ESG database")
    st.write("- MSCI ESG ratings")
    st.write("- Bloomberg terminal (pricing)")
    st.write("- STOXX Europe 600 constituents")

st.markdown("**Analytical Approach**")
st.write("""
Panel regression analysis with firm and time fixed effects to control for unobserved heterogeneity. 
Testing whether supply chain ESG metrics have explanatory power beyond traditional Fama-French factors 
and direct ESG scores. Robustness checks include lagged variables to address reverse causality and 
industry-specific subgroup analysis.
""")

st.markdown("**Expected Contributions**")
st.write("""
This research contributes to the growing literature on ESG materiality by focusing specifically on 
supply chain metrics - an understudied area despite representing 70-80% of most companies' total emissions. 
Findings could inform investor due diligence, corporate sustainability strategies, and regulatory approaches 
to Scope 3 reporting requirements.
""")

st.markdown("---")

st.subheader("Research Interests")
st.write("""
Beyond the master's thesis, my analytical interests span quantitative finance (factor models, risk attribution), 
alternative data in finance (NLP on earnings calls, satellite data for commodity markets), and operational 
analytics (trading desk optimization, market microstructure). Open to research collaborations at the 
intersection of data science and financial markets.
""")

st.markdown("---")

st.caption("Research updates and working papers will be available upon completion")
