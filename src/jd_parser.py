import re

def extract_jd_skills(jd_text, skill_list):
    jd_text = jd_text.lower()
    skills = []
    for skill in skill_list:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, jd_text):
            skills.append(skill)
    return list(set(skills))
