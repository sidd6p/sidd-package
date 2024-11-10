import streamlit as st


st.set_page_config(page_title="Home", page_icon="👋")

st.write("Hello I am Siddhartha Purwar")

projects_page = st.Page("./pages/Projects.py", title="Projects")
link_page = st.Page("./pages/Links.py", title="Links")
experience_page = st.Page("./pages/Experiences.py", title="Experiences")


pg = st.navigation([projects_page, link_page])
st.set_page_config(page_title="Siddhartha", page_icon=":material/edit:")
pg.run()