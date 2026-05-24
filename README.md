# 🤖 AI-Powered ATS Resume Expert

A smart, AI-powered Applicant Tracking System (ATS) built with **Streamlit** and **Google Gemini 2.5 Flash**. This tool helps job seekers evaluate their resumes against job descriptions and improve their chances of getting hired.

---

## 🔗 Live Demo
👉 [ai-powered-ats-resume-expert.streamlit.app](https://ai-powered-ats-resume-expert.streamlit.app)

---

## 📌 Problem Statement
Many job seekers get rejected not because they are unqualified, but because their resumes fail to pass ATS (Applicant Tracking System) filters used by companies. These systems scan resumes for relevant keywords and rank candidates automatically.

This project solves that problem by giving candidates instant AI-powered feedback on how well their resume matches a job description.

---

## 🎯 Objective
To build an end-to-end AI application that:
- Evaluates a resume against a job description
- Provides a match percentage score
- Identifies missing keywords
- Gives professional HR-level feedback

---

## 🚀 Features
- 📄 Upload resume as PDF
- 📋 Paste any job description
- 🔍 Get professional evaluation of your resume
- 📊 Get ATS match percentage + missing keywords
- ⚡ Powered by Google Gemini 2.5 Flash (latest LLM)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| PDF Processing | pdf2image, Pillow |
| Environment | python-dotenv |
| Deployment | Streamlit Cloud |
| Version Control | GitHub |

---

## 📁 Project Structure
```
AI-Powered-ATS-Resume-Expert/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignores .env file
└── README.md           # Project documentation
```

---

## ⚙️ How It Works
1. User uploads their **resume as a PDF**
2. User pastes the **job description**
3. The PDF is converted to an image using `pdf2image`
4. The image + job description are sent to **Google Gemini 2.5 Flash**
5. Gemini analyzes both and returns:
   - Professional HR evaluation **or**
   - ATS match percentage + missing keywords

---

## 🖥️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/SohaibAltaf135/AI-Powered-ATS-Resume-Expert.git
cd AI-Powered-ATS-Resume-Expert
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```
Get your free API key at: https://aistudio.google.com/app/apikey

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📊 Use Cases
- Job seekers optimizing their resumes
- Fresh graduates entering the job market
- Career switchers tailoring resumes for new roles
- HR professionals screening candidates

---

## 🔮 Future Improvements
- Add resume improvement suggestions
- Support multiple pages of resume
- Add interview question generator based on job description
- Support for multiple file formats (DOCX, TXT)

---

## 👨‍💻 Author
**Sohaib Altaf**
- GitHub: [@SohaibAltaf135](https://github.com/SohaibAltaf135)

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
