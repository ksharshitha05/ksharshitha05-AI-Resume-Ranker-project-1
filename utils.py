def skill_match(job_skills, resume_skills):

    if len(job_skills) == 0:
        return 0

    matched = set(job_skills) & set(resume_skills)

    score = len(matched) / len(job_skills)

    return round(score * 100, 2)