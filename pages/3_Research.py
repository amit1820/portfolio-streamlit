# pages/3_Research_Enhanced.py
import streamlit as st

st.set_page_config(page_title="Research & Analytics", layout="wide", page_icon="📚")

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');

.page-header {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    padding: 2rem;
    border-radius: 16px;
    border: 1px solid rgba(244, 196, 48, 0.2);
    margin-bottom: 3rem;
}

.page-title {
    font-family: 'Space Mono', monospace;
    font-size: 2.5rem;
    font-weight: 700;
    color: #f4c430;
    margin: 0 0 1rem 0;
    letter-spacing: -1px;
}

.page-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.2rem;
    color: #a8b2d1;
    line-height: 1.6;
    margin: 0;
}

.research-card {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.03) 0%, rgba(20, 27, 61, 0.5) 100%);
    border: 1px solid rgba(244, 196, 48, 0.2);
    border-radius: 16px;
    padding: 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}

.research-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #f4c430 0%, #ffd700 100%);
}

.research-title {
    font-family: 'Space Mono', monospace;
    font-size: 1.8rem;
    font-weight: 700;
    color: #f4c430;
    margin: 0 0 1rem 0;
    line-height: 1.3;
}

.research-authors {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    color: #8892b0;
    margin-bottom: 1.5rem;
    font-style: italic;
}

.research-section {
    margin-bottom: 1.5rem;
}

.section-heading {
    font-family: 'Space Mono', monospace;
    font-size: 0.95rem;
    color: #f4c430;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.8rem;
    font-weight: 700;
}

.section-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    color: #ccd6f6;
    line-height: 1.7;
}

.methodology-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.method-box {
    background: rgba(244, 196, 48, 0.05);
    border: 1px solid rgba(244, 196, 48, 0.2);
    border-radius: 12px;
    padding: 1.5rem;
}

.method-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #f4c430;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
    font-weight: 700;
}

.method-items {
    list-style: none;
    padding: 0;
    margin: 0;
}

.method-items li {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.95rem;
    color: #a8b2d1;
    padding: 0.4rem 0;
    padding-left: 1.2rem;
    position: relative;
}

.method-items li::before {
    content: '▹';
    color: #f4c430;
    position: absolute;
    left: 0;
}

.status-badge {
    display: inline-block;
    background: rgba(251, 191, 36, 0.2);
    color: #fbbf24;
    padding: 0.5rem 1.2rem;
    border-radius: 20px;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    font-weight: 700;
    border: 1px solid rgba(251, 191, 36, 0.4);
    margin-top: 1rem;
}

.insight-box {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.08) 0%, rgba(244, 196, 48, 0.02) 100%);
    border-left: 4px solid #f4c430;
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1.5rem 0;
}

.insight-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    color: #ccd6f6;
    line-height: 1.7;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

# Page header
st.markdown("""
<div class="page-header">
    <h1 class="page-title">📚 Research & Applied Analytics</h1>
    <p class="page-subtitle">
    Academic research at the intersection of finance, sustainability, and quantitative analysis. 
    Applying rigorous statistical methods to explore how ESG factors in supply chains influence 
    equity market dynamics.
    </p>
</div>
""", unsafe_allow_html=True)

# Master's Thesis
st.markdown("""
<div class="research-card">
    <h2 class="research-title">The Impact of Supply Chain ESG Performance on Stock Returns and Volatility</h2>
    <p class="research-authors">Authors: Amit Kumar, Sairam Vinay Shetty | Frankfurt School of Finance & Management</p>
    
    <div class="research-section">
        <h3 class="section-heading">🎯 Research Question</h3>
        <p class="section-text">
        Does supply chain ESG performance (specifically Scope 3 emissions and supplier human rights practices) 
        significantly influence stock returns and volatility for European listed firms? Traditional ESG research 
        focuses on direct operations (Scope 1 & 2), but supply chains often represent the largest sustainability 
        footprint and risk exposure.
        </p>
    </div>
    
    <div class="insight-box">
        <p class="insight-text">
        <strong>Key Hypothesis:</strong> Companies with stronger supply chain ESG governance should exhibit 
        (1) risk-adjusted outperformance due to reduced operational and reputational risks, and 
        (2) lower volatility from improved stakeholder relationships and regulatory compliance.
        </p>
    </div>
    
    <div class="research-section">
        <h3 class="section-heading">📊 Methodology Overview</h3>
    </div>
</div>
""", unsafe_allow_html=True)

# Methodology Grid
st.markdown('<div class="methodology-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="method-box">
        <div class="method-title">Dependent Variables</div>
        <ul class="method-items">
            <li>Monthly stock returns (log returns)</li>
            <li>Return volatility (rolling std dev)</li>
            <li>Risk-adjusted returns (Sharpe ratio)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="method-box">
        <div class="method-title">ESG Variables</div>
        <ul class="method-items">
            <li>Scope 3 emissions intensity</li>
            <li>Supplier human rights scores</li>
            <li>Supply chain transparency metrics</li>
            <li>Supplier audit frequency</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="method-box">
        <div class="method-title">Control Variables</div>
        <ul class="method-items">
            <li>Firm size (market cap, log)</li>
            <li>Book-to-market ratio</li>
            <li>Leverage (debt-to-equity)</li>
            <li>Momentum (12-month returns)</li>
            <li>Sector fixed effects</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="method-box">
        <div class="method-title">Data Sources</div>
        <ul class="method-items">
            <li>Refinitiv ESG database</li>
            <li>MSCI ESG ratings</li>
            <li>Bloomberg terminal (pricing)</li>
            <li>STOXX Europe 600 constituents</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Analysis approach
st.markdown("""
<div class="research-card">
    <div class="research-section">
        <h3 class="section-heading">🔬 Analytical Approach</h3>
        <p class="section-text">
        <strong>Panel regression analysis</strong> with firm and time fixed effects to control for unobserved 
        heterogeneity. We'll test whether supply chain ESG metrics have explanatory power beyond traditional 
        Fama-French factors and direct ESG scores. Robustness checks will include lagged variables to address 
        reverse causality and industry-specific subgroup analysis.
        </p>
    </div>
    
    <div class="research-section">
        <h3 class="section-heading">💡 Expected Contributions</h3>
        <p class="section-text">
        This research contributes to the growing literature on ESG materiality by focusing specifically on 
        <strong>supply chain metrics</strong> — an understudied area despite representing 70-80% of most companies' 
        total emissions. Findings could inform investor due diligence, corporate sustainability strategies, 
        and regulatory approaches to Scope 3 reporting requirements.
        </p>
    </div>
    
    <span class="status-badge">📝 Ongoing Research — Expected Completion: August 2026</span>
</div>
""", unsafe_allow_html=True)

# Additional research interests
st.markdown("---")
st.markdown("""
<div style="background: rgba(244, 196, 48, 0.05); padding: 2rem; border-radius: 12px; border: 1px solid rgba(244, 196, 48, 0.2);">
    <h3 style="font-family: 'Space Mono', monospace; color: #f4c430; margin-bottom: 1rem;">🔍 Research Interests</h3>
    <p style="font-family: 'DM Sans', sans-serif; font-size: 1rem; color: #ccd6f6; line-height: 1.7;">
    Beyond the master's thesis, my analytical interests span <strong>quantitative finance</strong> 
    (factor models, risk attribution), <strong>alternative data in finance</strong> (NLP on earnings calls, 
    satellite data for commodity markets), and <strong>operational analytics</strong> (trading desk optimization, 
    market microstructure). Open to research collaborations at the intersection of data science and financial markets.
    </p>
</div>
""", unsafe_allow_html=True)

# Bottom note
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1.5rem;">
    <p style="font-family: 'Space Mono', monospace; font-size: 0.9rem; color: #8892b0;">
    Research updates and working papers will be linked here as they become available
    </p>
</div>
""", unsafe_allow_html=True)
