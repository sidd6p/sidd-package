import streamlit as st
import requests
from PIL import Image
from io import BytesIO

def fetch_and_open_png_from_url(url):
    try:
        # Send GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the image data in bytes
            return BytesIO(response.content)
        else:
            print(f"Failed to retrieve the file. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Catch any exceptions during the request
        print(f"An error occurred: {e}")
        return None

# Example usage for image (PNG)
url = "https://raw.githubusercontent.com/sidd6p/sidd-package/main/sidd/src/siddhartha_resume.png"
image_data = fetch_and_open_png_from_url(url)

# URL for the PDF (raw URL for direct access to the PDF)
resume_pdf_url = "https://raw.githubusercontent.com/sidd6p/sidd-package/main/sidd/src/siddhartha_resume.pdf"

# Fetch the PDF content
response = requests.get(resume_pdf_url)

if response.status_code == 200:
    # Create a download button for the PDF
    st.download_button(
        label="Download Resume 📥",
        data=response.content,
        file_name="Siddhartha-Resume.pdf",
        mime="application/pdf"
    )
else:
    st.error("Failed to retrieve the resume PDF.")

if image_data:
    # Display the image using Streamlit's st.image
    st.image(image_data, caption="Siddhartha's Resume")
