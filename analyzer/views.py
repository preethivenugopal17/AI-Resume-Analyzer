import pdfplumber
from groq import Groq
from django.shortcuts import render
from django.conf import settings

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def analyze_resume(text, job_desc):
    client = Groq(api_key=settings.GROQ_API_KEY)
    prompt = f"""
You are an expert resume reviewer.

Analyze this resume:
{text}

Job Description:
{job_desc}

Provide a structured response with exactly these sections:
**Skills Found:** (list them)
**Missing Skills:** (list them)
**Suggestions:** (3-5 bullet points)
**Score:** (X/100)
**Match Percentage:** (X%)
"""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def index(request):
    result = None
    error = None

    if request.method == "POST":
        resume_text = request.POST.get("resume_text", "").strip()
        job_desc = request.POST.get("job_desc", "").strip()
        file = request.FILES.get("resume_file")

        try:
            if file:
                resume_text = extract_text(file)
            if resume_text and job_desc:
                result = analyze_resume(resume_text, job_desc)
            else:
                error = "Please provide both a resume and a job description."
        except Exception as e:
            error = f"Something went wrong: {str(e)}"

    return render(request, "index.html", {"result": result, "error": error})