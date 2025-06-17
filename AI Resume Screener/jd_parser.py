import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def extract_jd_keywords(jd_text):
    jd_text = re.sub(r"[^a-zA-Z ]", " ", jd_text.lower())
    tokens = [word for word in jd_text.split() if word not in ENGLISH_STOP_WORDS and len(word) > 2]
    return list(set(tokens))