import streamlit as st
import json
import os

# st.set_page_config(page_title="Projects", page_icon="🚀")


# Function to display project details creatively
def display_project_details(project_data):
    st.markdown(f"# 🚀 **{project_data['project_name']}**")

    st.markdown(f"__💻 Technology Used:__ {project_data['technology_used']}")

    st.markdown(f"__💡Concepts:__ {project_data['concepts']}")

    st.markdown(f"### 🌐 [Code Link]({project_data['code_link']})")

    st.markdown("#### Description:")
    for line in project_data["description"]:
        st.markdown(f" - {line}")

    st.markdown("#### Features:")
    st.json(project_data["features"])


# Hardcoded JSON file path
json_file_path = os.path.abspath("src/projects.json")

# Load JSON data
try:
    with open(json_file_path, "r") as file:
        projects_data = json.load(file)

        # Get project names for the dropdown options
        project_names = [project["project_name"] for project in projects_data]

        # Dropdown to select a project
        selected_project = st.selectbox("Select a Project", project_names)

        # Find the selected project and display its details
        for project in projects_data:
            if project["project_name"] == selected_project:
                display_project_details(project)
                break
except FileNotFoundError:
    st.error(f"File not found at path: {json_file_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")


    # Add more projects as needed
