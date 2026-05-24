from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import io
import base64
import pdf2image
from google import genai
from google.genai import types

# --- Page Config ---
st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="📄",
    layout="centered"
)

# --- Gemini Client ---
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Functions ---
def get_gemini_response(input, pdf_content, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            input,
            types.Part.from_bytes(
                data=base64.b64decode(pdf_content[0]["data"]),
                mime_type="image/jpeg"
            ),
            prompt
        ]
    )
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=r"C:\Program Files (x86)\poppler\Library\bin"
        )
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No PDF file uploaded.")


# --- UI ---
st.markdown("""
    <h1 style='text-align: center; color: #4A90D9;'>📄 ATS Resume Expert</h1>
    <p style='text-align: center; color: gray;'>Powered by Google Gemini AI</p>
    <hr>
""", unsafe_allow_html=True)

# --- Input Section ---
st.subheader("📋 Job Description")
input_text = st.text_area(
    "Paste the job description here:",
    height=150,
    placeholder="e.g. We are looking for a Data Scientist with experience in Python, ML, and SQL..."
)

st.subheader("📎 Upload Your Resume")
uploaded_file = st.file_uploader("Upload PDF only", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully!")

st.markdown("<br>", unsafe_allow_html=True)

# --- Buttons ---
col1, col2 = st.columns(2)
with col1:
    submit1 = st.button("🔍 Evaluate My Resume", use_container_width=True)
with col2:
    submit3 = st.button("📊 Match Percentage", use_container_width=True)

# --- Prompts ---
input_prompt1 = """
You are an experienced HR with Tech experience in the field of any one job role from Data Science,
Full Stack Web Development, Big Data Engineering, Cloud Computing, Artificial Intelligence,
DEVOPS, Data Analyst.
Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns 
with the role. Highlight the strengths and weaknesses of the resume in relation to the job description.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role from
Data Science, Full Stack Web Development, Big Data Engineering, Cloud Computing, Artificial Intelligence, 
DEVOPS, Data Analyst and deep ATS Functionality.
Your task is to evaluate the resume against the provided job description. 
Give me the percentage of match if the resume matches the job description. First the output should 
come as a Percentage and then keywords missing in the resume
which are present in the job description.
"""

# --- Response ---
st.markdown("<hr>", unsafe_allow_html=True)

if submit1:
    if uploaded_file is not None:
        with st.spinner("🤖 Analyzing your resume..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("📝 Expert Evaluation:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume first.")

elif submit3:
    if uploaded_file is not None:
        with st.spinner("🤖 Calculating match percentage..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("📊 Match Result:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume first.")

# --- Footer ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color: gray; font-size: 12px;'>
        Built with ❤️ using Streamlit & Google Gemini AI
    </p>
""", unsafe_allow_html=True)