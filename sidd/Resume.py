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
            # st.error(f"Failed to retrieve the image. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Catch any exceptions during the request
        st.error(f"An error occurred while fetching the image: {e}")
        return None

# Example usage for image (PNG)
url = "https://raw.githubusercontent.com/sidd6p/sidd-package/main/src/siddhartha_resume.png"
image_data = fetch_and_open_png_from_url(url)

# URL for the PDF (raw URL for direct access to the PDF)
resume_pdf_url = "https://raw.githubusercontent.com/sidd6p/sidd-package/main/src/siddhartha_resume.pdf"

try:
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
        st.error("Failed to retrieve the resume PDF. Please try again later.")
except requests.exceptions.RequestException as e:
    st.error(f"An error occurred while fetching the resume PDF: {e}")

# Displaying the image if it was successfully fetched
if image_data:
    st.image(image_data, caption="Siddhartha's Resume")

# Displaying links to GitHub and LinkedIn profiles in case of error
st.markdown("For more details or if you have any questions, feel free to visit my profiles:")
st.markdown("[GitHub](https://github.com/sidd6p) | [LinkedIn](https://www.linkedin.com/in/siddp6)")
