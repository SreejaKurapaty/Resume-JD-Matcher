import streamlit as st
from docx import Document
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# ========== Utility Functions ==========
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,/-]', '', text)
    return text.strip().lower()

def read_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def get_tfidf_score(resume, jd):
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform([resume, jd])
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(score * 100, 2)

def get_llm_score(resume, jd):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode([resume, jd])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 2)

# ========== Streamlit UI ==========
st.title("📄 Resume vs Job Description Matcher")

resume_file = st.file_uploader("Upload Resume (.docx)", type=["docx"])
jd_text_input = st.text_area("Paste Job Description here", height=300)

if resume_file and jd_text_input.strip():
    if st.button("Apply & Match"):
        try:
            resume_text = clean_text(read_docx(resume_file))
            jd_text = clean_text(jd_text_input)

            tfidf_score = get_tfidf_score(resume_text, jd_text)
            llm_score = get_llm_score(resume_text, jd_text)

            st.success("✅ Files processed successfully!")
            st.write(f"📊 **TF-IDF Match Score:** {tfidf_score}%")
            st.write(f"🤖 **LLM-based Match Score:** {llm_score}%")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
