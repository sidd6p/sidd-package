import streamlit as st


projects_page = st.Page("./Projects.py", title="Projects")
experience_page = st.Page("./Experiences.py", title="Experiences")
resume_page = st.Page("./Resume.py", title="Resume")
about_page = st.Page("./About.py", title="About")


pg = st.navigation([about_page, projects_page, experience_page, resume_page])
pg.run()
