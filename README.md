# AI Resume Analyser

An AI-powered resume analysis system that evaluates a resume against a job description and returns a structured report.

## Tech Stack
- Python + Flask
- Gemini AI API (gemini-2.5-flash)
- PostgreSQL with B-tree Indexing
- PyPDF2
- HTML + CSS + JavaScript
- AWS S3 (upcoming)
- Render Deployment (upcoming)

## What It Does
- User uploads resume PDF and pastes job description
- PyPDF2 extracts text from PDF
- Gemini AI analyzes match score, missing keywords, matching skills, suggestions
- Results stored in PostgreSQL database with B-tree indexes
- Clean styled results page with loading spinner

## How to Run
```bash
pip install flask google-generativeai PyPDF2 psycopg2-binary python-dotenv
python app.py
```

## Key Features
- Match score out of 100
- Missing keywords identified
- Matching skills highlighted
- Actionable suggestions
- All analyses stored in PostgreSQL
