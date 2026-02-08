# pages/4_Contact_Enhanced.py
import streamlit as st

st.set_page_config(page_title="Contact", layout="wide", page_icon="📧")

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');

.contact-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

.contact-header {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    padding: 3rem 2rem;
    border-radius: 16px;
    border: 1px solid rgba(244, 196, 48, 0.2);
    margin-bottom: 3rem;
    text-align: center;
}

.contact-title {
    font-family: 'Space Mono', monospace;
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #f4c430 0%, #ffd700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 1rem 0;
    letter-spacing: -1px;
}

.contact-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.3rem;
    color: #a8b2d1;
    line-height: 1.6;
    margin: 0 auto;
    max-width: 600px;
}

.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.contact-card {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.03) 0%, rgba(20, 27, 61, 0.5) 100%);
    border: 1px solid rgba(244, 196, 48, 0.2);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.contact-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #f4c430 0%, #ffd700 100%);
    transform: scaleX(0);
    transition: transform 0.3s ease;
    transform-origin: left;
}

.contact-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(244, 196, 48, 0.2);
    border-color: #f4c430;
}

.contact-card:hover::before {
    transform: scaleX(1);
}

.contact-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
}

.contact-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #8892b0;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.8rem;
    font-weight: 700;
}

.contact-value {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.1rem;
    color: #ccd6f6;
    font-weight: 500;
    margin-bottom: 1rem;
}

.contact-link {
    font-family: 'Space Mono', monospace;
    display: inline-block;
    background: rgba(244, 196, 48, 0.1);
    color: #f4c430;
    padding: 0.7rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 700;
    border: 1px solid rgba(244, 196, 48, 0.3);
    transition: all 0.3s ease;
    margin-top: 0.5rem;
}

.contact-link:hover {
    background: rgba(244, 196, 48, 0.2);
    transform: scale(1.05);
    border-color: #f4c430;
    text-decoration: none;
    color: #f4c430;
}

.interests-section {
    background: rgba(244, 196, 48, 0.05);
    border: 1px solid rgba(244, 196, 48, 0.2);
    border-radius: 16px;
    padding: 2rem;
    margin: 3rem 0;
}

.interests-title {
    font-family: 'Space Mono', monospace;
    font-size: 1.5rem;
    color: #f4c430;
    margin-bottom: 1.5rem;
    font-weight: 700;
}

.interests-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
}

.interest-tag {
    font-family: 'DM Sans', sans-serif;
    background: rgba(244, 196, 48, 0.1);
    color: #ccd6f6;
    padding: 0.8rem 1.2rem;
    border-radius: 8px;
    border: 1px solid rgba(244, 196, 48, 0.2);
    text-align: center;
    font-size: 0.95rem;
}

.cta-section {
    background: linear-gradient(135deg, rgba(244, 196, 48, 0.1) 0%, rgba(20, 27, 61, 0.3) 100%);
    border: 2px solid rgba(244, 196, 48, 0.3);
    border-radius: 16px;
    padding: 2.5rem;
    text-align: center;
    margin: 3rem 0;
}

.cta-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.2rem;
    color: #ccd6f6;
    line-height: 1.7;
    margin-bottom: 1.5rem;
}

.cta-button {
    font-family: 'Space Mono', monospace;
    display: inline-block;
    background: #f4c430;
    color: #0a0e27;
    padding: 1rem 2.5rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.3s ease;
    border: none;
}

.cta-button:hover {
    background: #ffd700;
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(244, 196, 48, 0.4);
    text-decoration: none;
    color: #0a0e27;
}
</style>
""", unsafe_allow_html=True)

# Contact Header
st.markdown("""
<div class="contact-container">
    <div class="contact-header">
        <h1 class="contact-title">Let's Connect</h1>
        <p class="contact-subtitle">
        Open to Business Intelligence, Analytics, and Data Analyst roles, consulting projects, 
        and research collaborations. Always interested in discussing analytics architecture, 
        automation, and quantitative finance.
        </p>
    </div>
""", unsafe_allow_html=True)

# Contact Cards
st.markdown('<div class="contact-grid">', unsafe_allow_html=True)

# Email
st.markdown("""
<div class="contact-card">
    <span class="contact-icon">📧</span>
    <div class="contact-label">Email</div>
    <div class="contact-value">amit.kumar.analytics.eu@gmail.com</div>
    <a href="mailto:amit.kumar.analytics.eu@gmail.com" class="contact-link">Send Email</a>
</div>
""", unsafe_allow_html=True)

# Location
st.markdown("""
<div class="contact-card">
    <span class="contact-icon">📍</span>
    <div class="contact-label">Location</div>
    <div class="contact-value">Frankfurt am Main, Germany</div>
    <div style="font-family: 'DM Sans', sans-serif; font-size: 0.85rem; color: #8892b0; margin-top: 0.5rem;">
    Open to hybrid/remote opportunities
    </div>
</div>
""", unsafe_allow_html=True)

# GitHub
st.markdown("""
<div class="contact-card">
    <span class="contact-icon">💻</span>
    <div class="contact-label">GitHub</div>
    <div class="contact-value">@amit1820</div>
    <a href="https://github.com/amit1820" target="_blank" class="contact-link">View Repositories</a>
</div>
""", unsafe_allow_html=True)

# LinkedIn
st.markdown("""
<div class="contact-card">
    <span class="contact-icon">💼</span>
    <div class="contact-label">LinkedIn</div>
    <div class="contact-value">Amit Kumar</div>
    <a href="https://www.linkedin.com/in/amit1820" target="_blank" class="contact-link">Connect on LinkedIn</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Open to section
st.markdown("""
<div class="interests-section">
    <h2 class="interests-title">💡 Open To</h2>
    <div class="interests-grid">
        <div class="interest-tag">BI Analyst Roles</div>
        <div class="interest-tag">Data Analytics</div>
        <div class="interest-tag">Analytics Consulting</div>
        <div class="interest-tag">Research Collaborations</div>
        <div class="interest-tag">Dashboard Projects</div>
        <div class="interest-tag">Automation Workflows</div>
        <div class="interest-tag">Quantitative Analysis</div>
        <div class="interest-tag">Speaking Engagements</div>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section">
    <p class="cta-text">
    <strong>Currently seeking full-time BI/Analytics roles for post-graduation (August 2026)</strong><br>
    Have a project or opportunity? Let's discuss how I can help transform your data into actionable insights.
    </p>
    <a href="mailto:amit.kumar.analytics.eu@gmail.com?subject=Opportunity%20Discussion" class="cta-button">
    📬 Start a Conversation
    </a>
</div>
""", unsafe_allow_html=True)

# Response time note
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <p style="font-family: 'DM Sans', sans-serif; font-size: 0.95rem; color: #8892b0; line-height: 1.6;">
    I typically respond to emails within 24-48 hours.<br>
    For urgent inquiries, please mention "Urgent" in the subject line.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="font-family: 'Space Mono', monospace; font-size: 0.85rem; color: #8892b0;">
    Built with Streamlit • Deployed on Streamlit Cloud • Source code available on GitHub
    </p>
</div>
""", unsafe_allow_html=True)
