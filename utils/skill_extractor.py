SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "java",
    "c++",
    "git",
    "github",
    "aws",
    "tensorflow",
    "pytorch",
    "power bi",
    "tableau",
    "excel",
    "data analysis",
    "statistics",
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn",
    "nlp",
    "computer vision",
    "azure"
]

def extract_skills(text):

    found_skills = []

    text = text.lower().replace("\n", " ")

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills