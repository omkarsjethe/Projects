from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def score_resumes(resume_data, jd_keywords):
    jd_text = " ".join(jd_keywords)
    texts = [jd_text] + [r["text"] for r in resume_data]

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(texts)
    sim_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    scores = pd.DataFrame({
        "Candidate": [r["filename"] for r in resume_data],
        "Score": [round(score * 100, 2) for score in sim_scores]
    })
    return scores