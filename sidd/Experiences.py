import streamlit as st
import json
import requests

# Function to fetch JSON data from a URL (or local file for testing)
def fetch_json_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching the experience data: {e}")
        return None

# Function to display experience details creatively
def display_experience_details(experience_data):
    # Displaying company name and title with emoji
    st.markdown(f"## 🏢 **{experience_data['Company']}** - {experience_data['Title']}")
    
    # Displaying key details
    st.markdown(f"**Skills Used:** 🔧 {experience_data['Skills']}")
    st.markdown(f"**Job Type:** 💼 {experience_data['Type']}")
    st.markdown(f"**Duration:** 📅 {experience_data['start_date']} to {experience_data['end_date']}")
    
    st.markdown("### 📄 **Job Description:**")
    # Displaying the description creatively with bullet points
    for item in experience_data['description']:
        st.markdown(f"➡️ {item}")
    
    # Adding a horizontal line to separate different experiences
    st.markdown("---")

# Load JSON data from URL
try:
    url = "https://raw.githubusercontent.com/sidd6p/sidd-package/main/src/experiences.json"
    experiences_data = fetch_json_from_url(url)

    if experiences_data:  # Check if the data was successfully fetched
        # Get job titles for the dropdown options
        experience_titles = [experience["Title"] for experience in experiences_data]

        # Dropdown to select a job title
        selected_experience = st.selectbox("Experiences 🧐", experience_titles)

        # Find the selected experience and display its details
        for experience in experiences_data:
            if experience["Title"] == selected_experience:
                display_experience_details(experience)
                break

    else:
        st.error(f"Failed to retrieve experience data. Please try again later.")
        
        # Display links to GitHub and LinkedIn profiles
        st.markdown("For more details or if you have any questions, feel free to visit my profiles:")
        st.markdown("[GitHub](https://github.com/sidd6p) | [LinkedIn](https://www.linkedin.com/in/siddp6)")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}. Please try again later.")
