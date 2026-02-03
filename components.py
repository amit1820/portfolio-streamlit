# components.py
import streamlit as st

def project_card(title, subtitle, context, solution, impact_lines, tools, status=None, repo_link=None):
    """
    Renders a project card in Streamlit.
    - title: str
    - subtitle: str (short tech list)
    - context: str
    - solution: str
    - impact_lines: list[str]
    - tools: str
    - status: optional str, e.g. "In Progress" or "Completed"
    - repo_link: optional URL
    """
    # Outer container / custom CSS class assumed to exist in styles/main.css
    st.markdown(f"<div class='project-card'>", unsafe_allow_html=True)
    header = f"**{title}**  •  *{subtitle}*"
    st.markdown(header)
    if status:
        st.markdown(f"<div class='status-badge'>{status}</div>", unsafe_allow_html=True)
    st.markdown("**Context / Problem**")
    st.write(context)
    st.markdown("**Solution**")
    st.write(solution)
    if impact_lines:
        st.markdown("**Impact / Output**")
        for line in impact_lines:
            st.write(f"- {line}")
    st.markdown(f"**Tools:** {tools}")
    if repo_link:
        st.markdown(f"[View code]({repo_link})")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("")  # spacing
