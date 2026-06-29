def calculate_ats_score(skills, text):

    score = 0

    # Skills contribution
    score += min(len(skills) * 8, 40)

    # Check important sections
    if "education" in text.lower():
        score += 15

    if "project" in text.lower():
        score += 15

    if "experience" in text.lower():
        score += 15

    if "github" in text.lower():
        score += 5

    if "linkedin" in text.lower():
        score += 5

    if "certification" in text.lower():
        score += 5

    return min(score, 100)