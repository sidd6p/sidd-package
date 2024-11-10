import os
import streamlit as st

from PIL import Image


resume_pdf_path = "./siddhartha_resume.pdf"
resume_png_path = "./siddhartha_resume.png"

with open(resume_pdf_path, "rb") as file:
    btn = st.download_button(
        label="Download 📥",
        data=file,
        file_name="Siddhartha-Resume.pdf",
        mime="application/octet-stream",
    )

image = Image.open(resume_png_path)

st.image(image, caption="Siddhartha's Resume")
