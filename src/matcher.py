def calculate_match_details(resume_skills, jd_skills):
    """
    Compares resume skills against job description skills.

    Match percentage is calculated strictly based on
    job description requirements (ATS-style logic).

    Returns:
    - match_percentage
    - matched_skills
    - missing_skills
    """

    resume_skills = set(resume_skills)
    jd_skills = set(jd_skills)

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills

    if len(jd_skills) == 0:
        match_percentage = 0.0
    else:
        match_percentage = (len(matched_skills) / len(jd_skills)) * 100

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }
