import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf, extract_email, extract_phone
from semantic_ranker import rank_resumes
from skill_extractor import extract_skills
from utils import skill_match


st.title("AI Resume Screening & Ranking System")

job_description = st.text_area("Enter Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)",
    type="pdf",
    accept_multiple_files=True
)

if st.button("Analyze Resumes"):

    resume_texts = []
    data = []

    for file in uploaded_files:

        text = extract_text_from_pdf(file)

        resume_texts.append(text)

    similarity_scores = rank_resumes(job_description, resume_texts)

    job_skills = extract_skills(job_description)

    for i, file in enumerate(uploaded_files):

        text = resume_texts[i]

        resume_skills = extract_skills(text)

        skill_score = skill_match(job_skills, resume_skills)

        final_score = (similarity_scores[i] * 100 * 0.7) + (skill_score * 0.3)

        email = extract_email(text)

        phone = extract_phone(text)

        data.append({
            "Resume": file.name,
            "Email": email,
            "Phone": phone,
            "Semantic Score": round(similarity_scores[i]*100,2),
            "Skill Match %": skill_score,
            "Final Score": round(final_score,2)
        })

    df = pd.DataFrame(data)

    df = df.sort_values(by="Final Score", ascending=False)

    st.subheader("Resume Ranking")

    st.dataframe(df)

    st.bar_chart(df.set_index("Resume")["Final Score"])