# AI Resume Analyser

An AI-powered resume analysis system that evaluates a resume against a job description and returns a structured report with match score, missing keywords, and suggestions.

## Live Demo
https://resume-analyser-6tfu.onrender.com

## Tech Stack
- Python + Flask — backend web server
- Gemini AI API (gemini-2.5-flash) — AI analysis engine
- PostgreSQL — database with B-tree indexing
- AWS S3 — cloud storage for uploaded PDFs
- PyPDF2 — PDF text extraction
- HTML + CSS + JavaScript — frontend with loading spinner
- Render — cloud deployment

## How It Works
1. User uploads resume PDF and pastes job description
2. PDF stored on AWS S3, text extracted via PyPDF2
3. Resume text + JD sent to Gemini AI with structured prompt
4. Gemini returns match score, missing keywords, matching skills, suggestions
5. Results stored in PostgreSQL with B-tree indexes on match_score and created_at
6. Clean styled results page displayed to user

## Key Features
- Match score out of 100
- Missing keywords identified
- Matching skills highlighted
- Actionable improvement suggestions
- All analyses stored in PostgreSQL database
- Resume PDFs stored on AWS S3

## How to Run Locally
```bash
pip install flask google-generativeai PyPDF2 psycopg2-binary python-dotenv boto3 gunicorn
python app.py
```

## Environment Variables Required
```
GEMINI_API_KEY=
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_BUCKET_NAME=
AWS_REGION=
```