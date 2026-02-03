import streamlit as st

page_md = """
# Research & Applied Analytics

## Master’s Thesis — Supply Chain ESG & Stock Returns
**Title:** The Impact of Supply Chain ESG Performance on Stock Returns and Volatility  
**Summary:** This empirical project studies the relationship between supply chain ESG metrics (Scope 3 emissions, Supplier Human Rights) and firm financial performance for European listed companies (STOXX Europe 600 sample). :contentReference[oaicite:22]{index=22}

**Methodology:** multivariate regressions with asset-pricing controls; monthly returns and volatility as dependent variables. Data sources planned: Refinitiv / MSCI / Bloomberg.

**Status:** Ongoing — analysis and notebooks will be linked here when available.
"""
st.markdown(page_md, unsafe_allow_html=True)
