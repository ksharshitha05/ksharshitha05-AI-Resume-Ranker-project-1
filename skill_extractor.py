import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python","machine learning","deep learning","nlp",
    "data science","tensorflow","pytorch","pandas",
    "numpy","scikit-learn","sql","flask","streamlit",
    "docker","kubernetes","tableau","power bi"
]

def extract_skills(text):

    text = text.lower()

    skills_found = []

    for skill in SKILLS_DB:
        if skill in text:
            skills_found.append(skill)

    return list(set(skills_found))