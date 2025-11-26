import re
import spacy
from sentence_transformers import SentenceTransformer

nlp = spacy.load("en_core_web_sm")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

SKILL_KEYWORDS = [
    "python", "java", "c++", "django", "machine learning",
    "deep learning", "nlp", "data science", "sql", "html",
    "css", "javascript", "react", "pandas", "numpy", "tensorflow"
]

def extract_skills(text):
    text_lower = text.lower()
    found = [skill for skill in SKILL_KEYWORDS if skill in text_lower]
    return list(set(found))

def extract_education(text):
    patterns = [
        r"(B\.?Tech|Bachelor|Bachelors|BSc|B\.Sc)",
        r"(M\.?Tech|Master|Masters|MSc|M\.Sc|Postgraduate)"
    ]
    found = []
    for p in patterns:
        found.extend(re.findall(p, text, re.IGNORECASE))
    return list(set(found))

def extract_experience(text):
    match = re.search(r"(experience:.*)", text, re.IGNORECASE)
    return match.group(0) if match else None

def extract_resume_info(text):
    return {
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "embedding": embedding_model.encode(text).tolist()
    }
