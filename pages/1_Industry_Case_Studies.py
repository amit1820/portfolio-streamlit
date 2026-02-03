import streamlit as st

page_md = """
# Industry & Professional Case Studies

These projects reflect hands-on delivery of analytics and automation in production environments.

## AI-Powered Document Verification
**Context / Problem**  
The team manually verified ~400 compliance PDFs/month for stamps and signatures, which was slow and error-prone. :contentReference[oaicite:12]{index=12}

**Solution**  
Automated verification using OpenCV + OCR, flagging exceptions for review. :contentReference[oaicite:13]{index=13}

**Impact**  
- Automated validation of ~400 PDFs/month  
- Reduced manual effort by ~80% (≈40 hours/month)  
**Tools:** Python, OpenCV, PyMuPDF, scikit-image. :contentReference[oaicite:14]{index=14}

---

## Power Automate — File Renaming & Ticket Tracking
**Context / Problem**  
Manual renaming of ~480 files/month and daily Jira updates. :contentReference[oaicite:15]{index=15}

**Solution & Impact**  
Automated flows reduced errors by ~85% and saved ~80 hrs/month. **Tools:** Power Automate, Excel. :contentReference[oaicite:16]{index=16}

---

## Real-Time Trading Dashboards
**Context / Problem**  
Fragmented static reports; need for live KPIs. :contentReference[oaicite:17]{index=17}

**Solution & Impact**  
Power BI dashboards integrated with Zeppelin and Scala for live metrics. **Tools:** Power BI, Apache Zeppelin, Scala, SQL. :contentReference[oaicite:18]{index=18}

---

## Excel-Based Data Reconciliation & Validation
**Context / Problem**  
Large CSV volumes across trading DBs required reliable reconciliation. :contentReference[oaicite:19]{index=19}

**Solution & Impact**  
Power Query + VBA automation reduced reconciliation time by ~45 hrs/month and cut defects by ~40%. :contentReference[oaicite:20]{index=20}
"""
st.markdown(page_md, unsafe_allow_html=True)
