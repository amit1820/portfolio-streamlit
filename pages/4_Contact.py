# pages/4_Contact.py
import streamlit as st

st.set_page_config(page_title="Contact", layout="wide", page_icon="📧")

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
div[data-testid="stMarkdownContainer"] h1 { font-family: 'Space Mono', monospace; color: #f4c430; font-size: 3rem; }
div[data-testid="stMarkdownContainer"] h2 { font-family: 'Space Mono', monospace; color: #f4c430; font-size: 2rem; margin-top: 2rem; }
div[data-testid="stMarkdownContainer"] h4 { font-family: 'Inter', sans-serif; color: #ffd700; font-size: 1.1rem; }
div[data-testid="stMarkdownContainer"] p { font-family: 'DM Sans', sans-serif; color: #ccd6f6; line-height: 1.8; font-size: 1.05rem; }
div[data-testid="stAlert"] { background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%); border: 1px solid rgba(244, 196, 48, 0.3); border-radius: 12px; }
.stButton button { background: transparent; color: #ccd6f6; border: none; font-family: 'DM Sans', sans-serif; font-size: 1rem; }
.stButton button:hover { color: #f4c430; background: rgba(244, 196, 48, 0.1); }
a { color: #64ffda; text-decoration: none; }
a:hover { color: #ffd700; }
</style>
""", unsafe_allow_html=True)

st.title("Contact")

st.markdown("---")

st.markdown("## Contact Information")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("#### Email")
    st.write("amit.kumar.analytics.eu@gmail.com")
    
    st.markdown("#### Location")
    st.write("Frankfurt am Main, Germany")
    st.caption("Open to relocation anywhere in Germany")
    
    st.markdown("#### Phone")
    st.write("+49 15560576084")

with col2:
    st.markdown("#### LinkedIn")
    st.write("[linkedin.com/in/amit1820](https://www.linkedin.com/in/amit1820)")
    
    st.markdown("#### GitHub")
    st.write("[github.com/amit1820](https://github.com/amit1820)")
    
    st.markdown("#### Portfolio")
    st.write("You're looking at it!")

st.markdown("---")

st.markdown("## Availability")

st.info("""
**Available for full-time employment from May 2026.** Currently completing M.Sc. in Management 
at Frankfurt School of Finance & Management (coursework completed). Open to BI Analyst, Data Analyst, 
Analytics Engineer, and Data Engineer roles anywhere in Germany.
""")

st.markdown("---")

st.markdown("## Areas of Interest")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("#### Role Types")
    st.write("• Business Intelligence Analyst")
    st.write("• Data Analyst")
    st.write("• Analytics Engineer")
    st.write("• Data Engineer")

with col2:
    st.markdown("#### Technical Focus")
    st.write("• Power BI Dashboard Development")
    st.write("• ETL Pipeline Design")
    st.write("• Python & Statistical Modelling")
    st.write("• Databricks & Cloud Platforms")

with col3:
    st.markdown("#### Industries")
    st.write("• Financial Markets & Trading")
    st.write("• Banking & Fintech")
    st.write("• Enterprise Analytics")
    st.write("• Technology & SaaS")

st.markdown("---")

st.markdown("## Work Authorization")
st.write("Residence permit with work authorization in Germany. No sponsorship required.")

st.markdown("---")

st.caption("Portfolio built with Streamlit | Deployed on Streamlit Cloud | Updated April 2026")
