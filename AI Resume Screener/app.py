import streamlit as st
from resume_parser import parse_resume
from jd_parser import extract_jd_keywords
from matcher import score_resumes
import os
import pandas as pd

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("📄 AI-Powered Resume Screening Tool")

# Upload Job Description
st.subheader("1️⃣ Upload Job Description")
jd_text = st.text_area("Paste the job description here:", height=300)

# Upload Resumes
st.subheader("2️⃣ Upload Resume PDFs")
resume_files = st.file_uploader("Upload one or more resumes", type=["pdf"], accept_multiple_files=True)

if jd_text and resume_files:
    jd_keywords = extract_jd_keywords(jd_text)
    resume_data = []

    for file in resume_files:
        text = parse_resume(file)
        resume_data.append({
            "filename": file.name,
            "text": text
        })

    df_scores = score_resumes(resume_data, jd_keywords)

    st.subheader("📊 Candidate Rankings")
    st.dataframe(df_scores.sort_values(by="Score", ascending=False), use_container_width=True)

    csv = df_scores.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Ranked Results", csv, "ranked_resumes.csv", "text/csv")
