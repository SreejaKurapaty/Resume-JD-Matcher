# 📄 Resume–JD Matcher

An interactive AI-powered web app that calculates the semantic match between a **resume** and a **job description** using NLP techniques. Upload your resume, paste a JD, and instantly see how well they align.

---

## 🔍 What It Does

This app allows job seekers, recruiters, or career coaches to:

- Upload a **resume (.docx)**
- Paste a **job description**
- Get two match scores:
  - **TF-IDF Score** – based on keyword overlap
  - **LLM Score** – based on deep semantic understanding using a transformer model
- View how closely a resume matches the job role

---

## 🧠 How It Works

The app uses two techniques:
1. **TF-IDF + Cosine Similarity**
   - Captures keyword-level similarity between resume and JD
2. **Sentence-BERT (all-MiniLM-L6-v2)**
   - Generates contextual embeddings for both documents
   - Measures how closely they align using cosine similarity

---

## ⚙️ Built With

- [Streamlit](https://streamlit.io/) – UI
- [Sentence-Transformers](https://www.sbert.net/) – LLM embeddings
- `scikit-learn` – TF-IDF and similarity scoring
- `python-docx` – Resume parsing

---

## 🚀 Try It Live

👉 [Launch the App Here]
URL: https://jobsnapmatch.streamlit.app/  

---

## 📝 How to Use Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Resume-JP-Matcher.git
cd Resume-JP-Matcher
