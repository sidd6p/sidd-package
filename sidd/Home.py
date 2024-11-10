import streamlit as st



st.write("Hello I am Siddhartha Purwar")

projects_page = st.Page("./Projects.py", title="Projects")
link_page = st.Page("./Links.py", title="Links")
experience_page = st.Page("./Experiences.py", title="Experiences")
resume_page = st.Page("./Resume.py", title="Resume")


pg = st.navigation([projects_page, link_page, experience_page, resume_page])
# st.set_page_config(page_title="Siddhartha", page_icon=":material/edit:")
pg.run()
