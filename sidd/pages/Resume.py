import os
import streamlit as st

from PIL import Image

st.set_page_config(page_title="Resume", page_icon="📄")

resume_pdf_path = os.path.abspath("src/siddhartha_resume.pdf")
resume_png_path = os.path.abspath("src/siddhartha_resume.png")

with open(resume_pdf_path, "rb") as file:
    btn = st.download_button(
        label="Download 📥",
        data=file,
        file_name="Siddhartha-Resume.pdf",
        mime="application/octet-stream",
    )

image = Image.open(resume_png_path)

st.image(image, caption="Siddhartha's Resume")
