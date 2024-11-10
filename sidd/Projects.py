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
        # Get project names for the dropdown options
        project_names = [project["project_name"] for project in projects_data]

        # Dropdown to select a project
        selected_project = st.selectbox("Select a Project", project_names)

        # Find the selected project and display its details
        for project in projects_data:
            if project["project_name"] == selected_project:
                display_project_details(project)
                break

    else:
        st.error(f"Failed to retrieve data. Please try again later.")
        
        # Display links to GitHub and LinkedIn profiles
        st.markdown("For more details or if you have any questions, feel free to visit my profiles:")
        st.markdown("[GitHub](https://github.com/sidd6p) | [LinkedIn](https://www.linkedin.com/in/siddp6)")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}. Please try again later.")
    
