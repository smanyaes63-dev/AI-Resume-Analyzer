def recommend_jobs(skills):

    skills = [skill.lower() for skill in skills]

    jobs = []

    if "python" in skills:
        jobs.append("Python Developer")

    if "sql" in skills:
        jobs.append("Data Analyst")

    if "machine learning" in skills:
        jobs.append("Machine Learning Engineer")

    if "deep learning" in skills:
        jobs.append("AI Engineer")

    if "aws" in skills:
        jobs.append("Cloud Engineer")

    if "power bi" in skills:
        jobs.append("Business Intelligence Analyst")

    if "tableau" in skills:
        jobs.append("Data Visualization Analyst")

    if "statistics" in skills:
        jobs.append("Data Scientist")

    return jobs