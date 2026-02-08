# pages/4_Contact.py
import streamlit as st

st.set_page_config(page_title="Contact", layout="wide", page_icon="📧")

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

st.title("Contact")
st.markdown("### Get in Touch")

st.write("""
Open to Business Intelligence, Analytics, and Data Analyst roles, consulting projects, 
and research collaborations. Particularly interested in financial markets analytics, 
automation, and quantitative analysis.
""")

st.markdown("---")

# Contact Information
st.markdown("## Contact Information")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### Email")
    st.write("amit.kumar.analytics.eu@gmail.com")
    
    st.markdown("### Location")
    st.write("Frankfurt am Main, Germany")
    st.caption("Open to hybrid/remote opportunities")
    
    st.markdown("### Phone")
    st.write("+49 15560576084")

with col2:
    st.markdown("### LinkedIn")
    st.write("[linkedin.com/in/amit1820](https://www.linkedin.com/in/amit1820)")
    
    st.markdown("### GitHub")
    st.write("[github.com/amit1820](https://github.com/amit1820)")
    
    st.markdown("### Portfolio")
    st.write("This site")

st.markdown("---")

# Current Status
st.markdown("## Current Status")

st.info("""
Currently pursuing **Master of Science in Management** at Frankfurt School of Finance & Management 
(Expected graduation: August 2026). Seeking full-time BI/Analytics roles for post-graduation.
""")

st.markdown("---")

# Areas of Interest
st.markdown("## Areas of Interest")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("#### Role Types")
    st.write("• Business Intelligence Analyst")
    st.write("• Data Analyst")
    st.write("• Analytics Consultant")
    st.write("• Data Engineer")

with col2:
    st.markdown("#### Technical Focus")
    st.write("• Dashboard Development")
    st.write("• Process Automation")
    st.write("• Data Pipeline Design")
    st.write("• Quantitative Analysis")

with col3:
    st.markdown("#### Industries")
    st.write("• Financial Markets")
    st.write("• Trading & Exchanges")
    st.write("• Banking & Fintech")
    st.write("• Enterprise Analytics")

st.markdown("---")

# Work Authorization
st.markdown("## Work Authorization")
st.write("Eligible to work in Germany. Open to opportunities in Germany and Europe.")

st.markdown("---")

# Response Time
st.markdown("## Response Time")
st.caption("""
I typically respond to emails within 24-48 hours. For urgent inquiries, please mention 
"Urgent" in the subject line.
""")

st.markdown("---")

st.caption("Portfolio built with Streamlit | Deployed on Streamlit Cloud | Source code on GitHub")
