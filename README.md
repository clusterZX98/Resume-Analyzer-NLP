# Intelligent Resume Analyzer and Job Matching System

An end-to-end Resume Analyzer and Job Matching System built using Python, Natural Language Processing, Machine Learning, and Streamlit.

This project automates the resume screening process by extracting useful information from PDF resumes, performing NLP-based analysis, calculating ATS scores, identifying skill gaps, and matching resumes with job descriptions. It provides both recruiters and job seekers with valuable insights through an interactive dashboard.

---

## Project Overview

Recruiters often receive hundreds of resumes for a single job opening. Manually reviewing each resume is time-consuming and inefficient.

This project simplifies the screening process by:

- Extracting text from PDF resumes
- Performing NLP preprocessing
- Extracting skills, education, and experience
- Calculating ATS scores
- Matching resumes with job descriptions
- Identifying missing skills
- Displaying insights through an interactive Streamlit dashboard

---

## Features

### Resume Analysis

- Upload Resume PDF
- PDF Text Extraction
- Resume Text Cleaning
- Resume Statistics

### Natural Language Processing

- Text Cleaning
- Tokenization
- Stopword Removal
- Lemmatization
- Part-of-Speech Tagging
- Named Entity Recognition

### Information Extraction

- Skill Extraction
- Education Extraction
- Experience Extraction

### ATS and Job Matching

- ATS Score Calculation
- Resume and Job Description Matching
- Cosine Similarity Based Matching
- Skill Gap Analysis

### Interactive Dashboard

- Resume Overview
- NLP Analysis
- Skill Visualization
- Resume Classification
- ATS Score Dashboard
- Job Matching Dashboard

---

## Project Workflow

```text
Resume PDF
      │
      ▼
PDF Parser
      │
      ▼
NLP Preprocessing
      │
      ▼
Information Extraction
      ├── Skills
      ├── Education
      └── Experience
      │
      ▼
ATS Score Calculator
      │
      ▼
Job Matching Engine
      │
      ▼
Skill Gap Analysis
      │
      ▼
Streamlit Dashboard
```

---

## Project Structure

```text
Resume_Analyzer_NLP_System
│
├── backend
│   ├── ats_score.py
│   ├── classifier.py
│   ├── education_extractor.py
│   ├── experience_extractor.py
│   ├── job_matcher.py
│   ├── ner_extractor.py
│   ├── pdf_parser.py
│   ├── pos_tagger.py
│   ├── preprocess.py
│   ├── skill_extractor.py
│   └── utils.py
│
├── data
│   ├── jobs
│   ├── resumes
│   ├── resume_dataset.csv
│   └── skills.csv
│
├── frontend
│   └── app.py
│
├── models
│   ├── classifier.pkl
│   ├── label_encoder.pkl
│   └── tfidf.pkl
│
├── notebooks
│   └── model_training.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

### Programming Language

- Python

### Natural Language Processing

- NLTK
- SpaCy

### Machine Learning

- Scikit-learn
- Logistic Regression
- TF-IDF Vectorization

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Plotly
- Matplotlib
- Seaborn

### PDF Processing

- PDFPlumber

### Frontend

- Streamlit

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Resume-Analyzer-NLP.git
```

### Navigate to the Project Directory

```bash
cd Resume-Analyzer-NLP
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux or macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download the SpaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

### Run the Application

```bash
streamlit run frontend/app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## NLP Techniques Used

- Text Cleaning
- Tokenization
- Stopword Removal
- Lemmatization
- Part-of-Speech Tagging
- Named Entity Recognition
- TF-IDF Vectorization
- Cosine Similarity
- Information Extraction
- Text Analytics

---

## Machine Learning Pipeline

The Resume Classification model follows the workflow below:

- Resume Dataset Loading
- Data Cleaning
- Text Preprocessing
- Label Encoding
- Train-Test Split
- TF-IDF Vectorization
- Logistic Regression Training
- Model Evaluation
- Model Serialization using Joblib

---

## Future Improvements

Some planned enhancements include:

- Resume Classification using advanced models
- Candidate Ranking Engine
- Word2Vec Integration
- FastText Embeddings
- GloVe Embeddings
- AI Resume Summarization
- Career Recommendation System
- Interview Question Generator
- Resume Improvement Suggestions
- FastAPI Backend
- PostgreSQL Database
- Docker Deployment
- AWS Deployment
- Authentication System
- Recruiter Dashboard
- Multiple Resume Upload
- Resume Comparison

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing
- Resume Parsing
- Information Extraction
- Machine Learning Pipelines
- ATS Score Evaluation
- Recommendation Systems
- Streamlit Application Development
- End-to-End NLP Project Development

---

## Use Cases

- Resume Screening
- Recruitment Automation
- ATS Score Evaluation
- Resume Improvement
- Skill Gap Analysis
- Candidate Ranking
- Career Guidance

---

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## Author

**PIYUSH RAWAT**

Data Scientist

NLP Enthusiast

---

## License

This project is intended for educational and portfolio purposes. You are free to use and modify it for learning, research, and personal development.
