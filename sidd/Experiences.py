import streamlit as st
import json
import os

# Function to display experience details creatively
def display_experience_details(experience_data):
    st.markdown(f"# 🚀 **{experience_data['Title']}** at {experience_data['Company']}")

    st.markdown(f"__💻 Skills:__ {experience_data['Skills']}")
    st.markdown(f"__📅 Duration:__ {experience_data['start_date']} - {experience_data['end_date']}")

    st.markdown("#### Description:")
    for line in experience_data["description"]:
        st.markdown(f" - {line}")

# Hardcoded JSON file path
json_file_path = os.path.join(os.path.dirname(__file__), 'src/experiences.json')

# Load JSON data
try:
    with open(json_file_path, "r") as file:
        experiences_data = json.load(file)

        # Get experience titles for the dropdown options
        experience_titles = [f"{exp['Title']} at {exp['Company']}" for exp in experiences_data]

        # Dropdown to select an experience
        selected_experience = st.selectbox("Select an experience", experience_titles)

        # Find the selected experience and display its details
        for experience in experiences_data:
            experience_label = f"{experience['Title']} at {experience['Company']}"
            if experience_label == selected_experience:
                display_experience_details(experience)
                break

except FileNotFoundError:
    st.error(f"File not found at path: {json_file_path}")
except Exception as e:
    st.error(f"An error occurred: {e}")
