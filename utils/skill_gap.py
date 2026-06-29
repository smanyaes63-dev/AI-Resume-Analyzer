ROLE_SKILLS = {
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

    "AI Engineer": [
        "python",
        "deep learning",
        "tensorflow",
        "nlp"
    ]
}

def find_skill_gap(user_skills, role):

    user_skills = [s.lower() for s in user_skills]

    required = ROLE_SKILLS[role]

    missing = []

    for skill in required:
        if skill not in user_skills:
            missing.append(skill)

    return missing