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


# Function to display experience details creatively
def display_experience_details(experience_data):
    st.markdown(f"# 🚀 **{experience_data['project_name']}**")
    st.markdown(f"__💻 Technology Used:__ {experience_data['technology_used']}")
    st.markdown(f"__💡 Concepts:__ {experience_data['concepts']}")
    st.markdown(f"### 🌐 [Code Link]({experience_data['code_link']})")

    st.markdown("#### Features:")
    for feature_category, features in experience_data["features"].items():
        st.markdown(f"**{feature_category}:**")
        if isinstance(features, dict):
            for feature, available in features.items():
                if available:
                    st.markdown(f" - {feature}")
        elif isinstance(features, bool):
            st.markdown(f" - {feature_category}")


# Load JSON data from URL
try:
    url = "https://raw.githubusercontent.com/sidd6p/sidd-package/refs/heads/main/src/experience.json"
    experiences_data = fetch_json_from_url(url)

    if experiences_data:  # Check if the data was successfully fetched
        # Get experience names for the dropdown options
        experience_names = [experience["project_name"] for experience in experiences_data]

        # Dropdown to select an experience
        selected_experience = st.selectbox("Select an Experience", experience_names)

        # Find the selected experience and display its details
        for experience in experiences_data:
            if experience["project_name"] == selected_experience:
                display_experience_details(experience)
                break

    else:
        st.error(f"Failed to retrieve experience data. Please try again later.")
        
        # Display links to GitHub and LinkedIn profiles
        st.markdown("For more details or if you have any questions, feel free to visit my profiles:")
        st.markdown("[GitHub](https://github.com/sidd6p) | [LinkedIn](https://www.linkedin.com/in/siddp6)")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}. Please try again later.")
