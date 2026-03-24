# 🤖 AI Resume Analyzer

An AI-powered web application built using Django that analyzes resumes and provides intelligent feedback based on job descriptions.

---

## 🚀 Live Demo
🔗 https://ai-resume-analyzer-sdqp.onrender.com/

---

## 📌 Features

- 📄 Upload Resume (PDF) or Paste Text
- 🧠 AI-based Resume Analysis
- 🎯 Job Description Matching
- 📊 Skill Extraction
- ❌ Missing Skills Identification
- 💡 Personalized Suggestions
- 📈 Resume Score & Match Percentage

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **AI Integration:** Groq API (LLM)
- **PDF Processing:** pdfplumber
- **Deployment:** Render

---

## ⚙️ How It Works

1. Upload resume (PDF) or paste text  
2. Extract text using `pdfplumber`  
3. Provide job description  
4. Send data to Groq AI model  
5. Get analysis:
   - Skills found  
   - Missing skills  
   - Suggestions  
   - Match score  
6. Display results on UI  

---

## 📸 Screenshots

### 🔹 Home Page
![Home](images/home.png)

### 🔹 Analysis Result
![Result](images/result.png)

---

## 📂 Project Structure
resume_analyzer/
│
├── analyzer/
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│
├── resume_analyzer/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── templates/
├── manage.py
├── requirements.txt
├── Procfile
├── build.sh

---

## 🔐 Environment Variables
SECRET_KEY=your_secret_key
DEBUG=False
GROQ_API_KEY=your_api_key

---

## 🧪 Run Locally

```bash
git clone https://github.com/preethivenugopal17/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
