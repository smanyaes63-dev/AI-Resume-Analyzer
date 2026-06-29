import streamlit as st

from utils.skill_extractor import extract_skills
from utils.pdf_parser import extract_text_from_pdf
from utils.ats_score import calculate_ats_score
from utils.job_recommendation import recommend_jobs
from utils.skill_gap import find_skill_gap

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🤖 AI Resume Analyzer & Career Guidance System")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    text = extract_text_from_pdf(uploaded_file)

    skills = extract_skills(text)

    score = calculate_ats_score(skills, text)

    jobs = recommend_jobs(skills)

    st.subheader("📄 Resume Preview")

    with st.expander("View Extracted Resume Text"):
        st.write(text)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛠 Skills Found")
        st.write(skills)

    with col2:
        st.subheader("📊 ATS Score")
        st.progress(score / 100)
        st.success(f"{score}/100")

        st.subheader("💪 Resume Strength")

        if score >= 80:
            st.success("Strong Resume")
        elif score >= 60:
            st.warning("Intermediate Resume")
        else:
            st.error("Beginner Resume")
    st.subheader("💼 Recommended Jobs")

    for job in jobs:
        st.write("✅", job)

    role = st.selectbox(
        "Choose Target Role",
        [
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer"
        ]
    )

    role_skills = {
        "Data Analyst": [
            "python",
            "sql",
            "excel",
            "power bi"
        ],
        "Data Scientist": [
            "python",
            "sql",
            "machine learning",
            "statistics"
        ],
        "Machine Learning Engineer": [
            "python",
            "machine learning",
            "deep learning",
            "tensorflow"
        ],
        "AI Engineer": [
            "python",
            "deep learning",
            "nlp",
            "tensorflow"
        ]
    }

    required = role_skills[role]

    missing_skills = []

    for skill in required:
        if skill not in [s.lower() for s in skills]:
            missing_skills.append(skill)
    st.subheader("⚠️ Skill Gap Analysis")

    if missing_skills:
        for skill in missing_skills:
            st.write("❌", skill)
    else:
        st.success("No Skill Gaps Found!")

    st.subheader("📌 Resume Suggestions")

    if score < 60:
        st.warning(
            "Add more technical skills, projects, and certifications."
        )

    if len(skills) < 5:
        st.warning(
            "Add more relevant skills."
        )

    if "github" not in text.lower():
        st.info("Add your GitHub profile link.")

    if "linkedin" not in text.lower():
        st.info("Add your LinkedIn profile link.")

    st.success("Resume Analysis Complete!")
    