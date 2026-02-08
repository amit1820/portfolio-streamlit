# pages/4_Contact.py
import streamlit as st

st.set_page_config(page_title="Contact", layout="wide", page_icon="📧")

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

st.title("Contact")

st.markdown("""
Open to Business Intelligence, Analytics, and Data Analyst roles, consulting projects, 
and research collaborations. Particularly interested in financial markets analytics, 
automation, and quantitative analysis.
""")

st.markdown("---")

# Contact Information
col1, col2 = st.columns(2)

with col1:
    st.subheader("Get in Touch")
    st.markdown("**Email**")
    st.write("amit.kumar.analytics.eu@gmail.com")
    
    st.markdown("**Location**")
    st.write("Frankfurt am Main, Germany")
    st.caption("Open to hybrid/remote opportunities")
    
    st.markdown("**Phone**")
    st.write("+49 15560576084")

with col2:
    st.subheader("Professional Links")
    st.markdown("**LinkedIn**")
    st.write("[linkedin.com/in/amit1820](https://www.linkedin.com/in/amit1820)")
    
    st.markdown("**GitHub**")
    st.write("[github.com/amit1820](https://github.com/amit1820)")
    
    st.markdown("**Portfolio**")
    st.write("This site")

st.markdown("---")

st.subheader("Current Status")
st.info("""
Currently pursuing Master of Science in Management at Frankfurt School of Finance & Management 
(Expected graduation: August 2026). Seeking full-time BI/Analytics roles for post-graduation.
""")

st.markdown("---")

st.subheader("Areas of Interest")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Role Types**")
    st.write("- Business Intelligence Analyst")
    st.write("- Data Analyst")
    st.write("- Analytics Consultant")
    st.write("- Data Engineer")

with col2:
    st.markdown("**Technical Focus**")
    st.write("- Dashboard Development")
    st.write("- Process Automation")
    st.write("- Data Pipeline Design")
    st.write("- Quantitative Analysis")

with col3:
    st.markdown("**Industries**")
    st.write("- Financial Markets")
    st.write("- Trading & Exchanges")
    st.write("- Banking & Fintech")
    st.write("- Enterprise Analytics")

st.markdown("---")

st.subheader("Work Authorization")
st.write("Eligible to work in Germany. Open to opportunities in Germany and Europe.")

st.markdown("---")

st.subheader("Response Time")
st.caption("""
I typically respond to emails within 24-48 hours. For urgent inquiries, please mention 
"Urgent" in the subject line.
""")

st.markdown("---")

st.caption("Portfolio built with Streamlit | Deployed on Streamlit Cloud | Source code on GitHub")
