import streamlit as st
import json
import requests

# Function to fetch JSON data from a URL
def fetch_json_from_url(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None

# Function to display project details creatively
def display_project_details(project_data):
    st.markdown(f"# 🚀 **{project_data['project_name']}**")
    st.markdown(f"__💻 Technology Used:__ {project_data['technology_used']}")
    st.markdown(f"__💡Concepts:__ {project_data['concepts']}")
    st.markdown(f"### 🌐 [Code Link]({project_data['code_link']})")
    st.markdown("#### Features:")
    st.json(project_data["features"])

# Load JSON data
try:
    url = "https://raw.githubusercontent.com/sidd6p/sidd-package/refs/heads/main/src/projects.json"
    projects_data = fetch_json_from_url(url)

    if projects_data:  # Check if the data was successfully fetched
        # Sort projects, putting starred projects at the top
        sorted_projects = sorted(
            projects_data, 
            key=lambda x: not x.get("star", False)  # False comes first, so starred projects (True) are on top
        )

        # Get project names for the dropdown, appending "⭐" for starred projects
        project_names = [
            f"{project['project_name']} ⭐" if project.get("star") else project["project_name"]
            for project in sorted_projects
        ]

        # Dropdown to select a project
        selected_project_name = st.selectbox("Select a Project", project_names)

        # Find and display the selected project based on the original name
        for project in sorted_projects:
            if selected_project_name.startswith(project["project_name"]):
                display_project_details(project)
                break

    else:
        st.error("Failed to retrieve data. Please try again later.")
        
        # Display links to GitHub and LinkedIn profiles
        st.markdown("For more details or if you have any questions, feel free to visit my profiles:")
        st.markdown("[GitHub](https://github.com/sidd6p) | [LinkedIn](https://www.linkedin.com/in/siddp6)")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}. Please try again later.")
