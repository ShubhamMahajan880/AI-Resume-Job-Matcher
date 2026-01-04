# AI Resume & Job Matcher

An AI-powered Streamlit application that evaluates how well a resume matches a given job description.  
The system calculates a percentage match, determines eligibility, highlights matching and missing skills, and suggests what to learn to qualify for the role.

This project simulates an **ATS-style resume screening process** using skill-based evaluation.

---

## 🚀 Problem Statement

Job applicants often apply without knowing:
- Whether their resume actually matches the job requirements.
- Which skills they already qualify for.
- What skills are missing and need improvement.

This leads to:
- Blind applications.
- Avoidable rejections.
- No clear learning direction.

**AI Resume & Job Matcher** solves this by providing a transparent, explainable resume–JD evaluation before applying.

---

## 🧠 How It Works (High-Level)

1. User uploads a **resume (PDF)**.
2. User pastes a **job description**.
3. The system extracts relevant skills from both.
4. Resume skills are compared **strictly against job requirements**.
5. A match percentage and eligibility status are calculated.
6. Missing skills are identified.
7. Actionable learning recommendations are provided.

The logic is deterministic and explainable, similar to how ATS systems filter candidates.

---

## 📊 Match Logic (ATS-Style)




# AI Resume & Job Matcher

An AI-powered Streamlit application that evaluates how well a resume matches a given job description.  
The system calculates a percentage match, determines eligibility, highlights matching and missing skills, and suggests what to learn to qualify for the role.

This project simulates an **ATS-style resume screening process** using skill-based evaluation.

---

## 🚀 Problem Statement

Job applicants often apply without knowing:
- Whether their resume actually matches the job requirements.
- Which skills they already qualify for.
- What skills are missing and need improvement.

This leads to:
- Blind applications.
- Avoidable rejections.
- No clear learning direction.

**AI Resume & Job Matcher** solves this by providing a transparent, explainable resume–JD evaluation before applying.

---

## 🧠 How It Works (High-Level)

1. User uploads a **resume (PDF)**.
2. User pastes a **job description**.
3. The system extracts relevant skills from both.
4. Resume skills are compared **strictly against job requirements**.
5. A match percentage and eligibility status are calculated.
6. Missing skills are identified.
7. Actionable learning recommendations are provided.

The logic is deterministic and explainable, similar to how ATS systems filter candidates.

---
Match Percentage = (Matched Job Skills / Total Job Skills) × 100

## 📊 Match Logic (ATS-Style)


### Eligibility Criteria
- **Eligible**: ≥ 70%
- **Partially Eligible**: 40% – 69%
- **Not Eligible**: < 40%

This ensures evaluation is **job-driven**, not resume-driven.

---

## 🖥️ Application Flow

1. Upload resume (PDF).
2. Paste job description.
3. System analyzes skills.
4. Results displayed:
   - Match percentage.
   - Eligibility status.
   - Matching criteria.
   - Missing criteria.
   - What to learn next.

A progress indicator guides the user through the evaluation steps.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI and interaction.
- **pdfplumber** – Resume PDF parsing.
- **Regex-based NLP** – Skill extraction.
- **Pandas** – Tabular visualization.

---

## 📂 Project Structure

```text
AI-Resume-Job-Matcher/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── matcher.py
│   ├── eligibility.py
│   └── suggestions.py
│
└── sample_data/
    └── sample_jd.txt
```




---

## ▶️ Run Locally

### Prerequisites
- Python 3.9+
- Git

### Steps
```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py

Open browser at:
http://localhost:8501



