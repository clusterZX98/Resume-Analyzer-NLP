import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from backend.pdf_parser import extract_text
from backend.preprocess import clean_text
from backend.skill_extractor import extract_skills
#from backend.classifier import predict_category
from backend.job_matcher import match_resume_job
from backend.ats_score import ats_score

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 1rem;
}

.metric-card {
    background: #1E1E1E;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #333;
}

.skill-card {
    background-color:#262730;
    padding:10px;
    border-radius:8px;
    margin:5px;
}

.big-font {
    font-size:40px !important;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown(
    """
    <h1 style='text-align:center'>
    Intelligent Resume Analyzer
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h5 style='text-align:center;color:gray'>
    NLP • ATS • Resume Classification • Job Matching
    </h5>
    """,
    unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=120
)

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Upload Resume",
        "NLP Analysis",
        "Skills",
        "Classification",
        "ATS Score",
        "Job Matching"
    ]
)

# -------------------------------------------------
# UPLOAD
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    tokens = clean_text(resume_text)

    skills = extract_skills(resume_text)

    # ---------------------------------------------
    # PAGE 1
    # ---------------------------------------------

    if section == "Upload Resume":

        st.success("Resume Uploaded Successfully")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Words", len(resume_text.split()))

        with col2:
            st.metric("Skills Found", len(skills))

        with col3:
            st.metric("Tokens", len(tokens))

        st.subheader("Resume Preview")

        st.text_area(
            "",
            resume_text[:5000],
            height=400
        )

    # ---------------------------------------------
    # PAGE 2 NLP ANALYSIS
    # ---------------------------------------------

    elif section == "NLP Analysis":

        st.header("NLP Processing")

        tab1, tab2, tab3 = st.tabs(
            [
                "Original Text",
                "Cleaned Tokens",
                "Statistics"
            ]
        )

        with tab1:

            st.text_area(
                "Resume Text",
                resume_text,
                height=400
            )

        with tab2:

            st.write(tokens)

        with tab3:

            df = pd.DataFrame({
                "Metric":[
                    "Words",
                    "Characters",
                    "Tokens"
                ],
                "Count":[
                    len(resume_text.split()),
                    len(resume_text),
                    len(tokens)
                ]
            })

            fig = px.bar(
                df,
                x="Metric",
                y="Count"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # ---------------------------------------------
    # PAGE 3 SKILLS
    # ---------------------------------------------

    elif section == "Skills":

        st.header("🎯 Skills Extracted")

        cols = st.columns(4)

        for i, skill in enumerate(skills):

            cols[i % 4].success(skill)

        if len(skills) > 0:

            skill_df = pd.DataFrame(
                {
                    "Skill": skills,
                    "Count": [1]*len(skills)
                }
            )

            fig = px.pie(
                skill_df,
                names="Skill",
                values="Count",
                title="Skill Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # # ---------------------------------------------
    # # PAGE 4 CLASSIFICATION
    # # ---------------------------------------------

    # elif section == "Classification":

    #     # category = predict_category(
    #     #     resume_text
    #     # )

    #     # st.header("Resume Classification")

    #     # st.success(
    #     #     f"Predicted Domain : {category}"
    #     # )

    #     fig = go.Figure(
    #         go.Indicator(
    #             mode="gauge+number",
    #             value=95,
    #             title={
    #                 "text":"Classification Confidence"
    #             }
    #         )
    #     )

    #     st.plotly_chart(
    #         fig,
    #         use_container_width=True
    #     )

    # ---------------------------------------------
    # PAGE 5 ATS SCORE
    # ---------------------------------------------

    elif section == "ATS Score":

        st.header("ATS Score")

        job_skills = [
            "Python",
            "SQL",
            "Machine Learning",
            "Power BI",
            "TensorFlow"
        ]

        score = ats_score(
            skills,
            job_skills
        )

        st.metric(
            "ATS Score",
            f"{score}%"
        )

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=score,
                gauge={
                    "axis":{
                        "range":[0,100]
                    }
                }
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------------------------------------
    # PAGE 6 JOB MATCHING
    # ---------------------------------------------

    elif section == "Job Matching":

        st.header(" Job Matching Engine")

        jd = st.text_area(
            "Paste Job Description"
        )

        if st.button("Analyze Match"):

            score = match_resume_job(
                resume_text,
                jd
            )

            st.metric(
                "Match Score",
                f"{score}%"
            )

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=score,
                    gauge={
                        "axis":{
                            "range":[0,100]
                        }
                    }
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            resume_skills = set(skills)

            jd_skills = {
                "Python",
                "SQL",
                "Machine Learning",
                "TensorFlow",
                "Docker",
                "AWS"
            }

            missing = list(
                jd_skills - resume_skills
            )

            st.subheader(
                " Skill Gap Analysis"
            )

            if missing:

                for skill in missing:
                    st.warning(skill)

            else:
                st.success(
                    "No Skill Gap Found"
                )

else:

    st.info(
        "Upload a Resume PDF to Start Analysis"
    )