# SkillAlign AI – Job Fit Analyzer

An AI-powered Streamlit application that evaluates how well a resume matches a given job description.  
The system calculates a percentage match, determines eligibility, highlights matching and missing skills, and suggests what to learn to qualify for the role.

This project simulates an **ATS-style resume screening process** using transparent, skill-based evaluation.

---

## 🌐 Live Demo

🔗 **Live Application:** [https://ai-resume-job-matcher-jpjyv5v3gvhfxklydnumbv.streamlit.app]

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

**AI Resume & Job Matcher** solves this by providing a clear, explainable resume–job description evaluation *before* applying.

---

## 🧠 How It Works (High-Level)

1. User uploads a **resume (PDF)**.
2. User pastes a **job description**.
3. The system extracts relevant skills from both.
4. Resume skills are compared **strictly against job requirements**.
5. A match percentage and eligibility status are calculated.
6. Missing skills are identified.
7. Actionable learning recommendations are generated.

The logic is deterministic and explainable, similar to how ATS systems screen candidates.

---

## 📊 Match Logic (ATS-Style)

```text
Match Percentage = (Matched Job Skills / Total Job Skills) × 100
```

### Eligibility Criteria
- **Eligible:** ≥ 70%
- **Partially Eligible:** 40% – 69%
- **Not Eligible:** < 40%

This ensures the evaluation is **job-driven**, not resume-driven.

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

A step-based flow with progress indicators guides the user through the evaluation.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI and application flow.
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
```

Open browser at:
```
http://localhost:8501
```

---

## 📌 Example Output

- **Match Percentage:** 55%
- **Eligibility:** Partially Eligible
- **Matching Skills:** Python, SQL
- **Missing Skills:** Data Structures, Docker
- **Learning Suggestions:**
  - Learn core data structures and algorithms.
  - Understand containerization using Docker.

---

## ⚠️ Limitations

- Skill extraction is keyword-based (not semantic).
- Does not evaluate years of experience or depth of expertise.
- Designed as a screening and learning assistant, not a final hiring decision tool.

---

## 🔮 Future Enhancements

- NLP-based semantic skill extraction.
- Resume bullet-point improvement suggestions.
- Job description PDF upload.
- Recalculate eligibility based on planned skills.
- Application tracking and analytics.

---

## 👤 Author & Ownership

This project is designed, developed, and maintained by **Shubham Mahajan**.

- GitHub: https://github.com/ShubhamMahajan880  
- LinkedIn: https://www.linkedin.com/in/shubham-mahajan-2a9a47220/

The application includes an in-app author watermark and footer credit to clearly establish ownership and originality.

---
