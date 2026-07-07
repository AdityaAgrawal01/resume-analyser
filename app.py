# 1. Imports
from flask import Flask, render_template, request
import PyPDF2
import os
from dotenv import load_dotenv
import google.generativeai as genai
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def save_to_db(resume_text, job_description, match_score, analysis_result):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO analyses (resume_text, job_description, match_score, analysis_result)
        VALUES (%s, %s, %s, %s)
    """, (resume_text, job_description, match_score, analysis_result))
    conn.commit()
    cur.close()
    conn.close()

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. App creation
app = Flask(__name__)

# 3. Helper function
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text, jd_text):
    model = genai.GenerativeModel('gemini-2.5-flash')    
    prompt = f"""
    You are an expert technical recruiter. Analyze this resume against the job description.
    
    RESUME:
    {resume_text}
    
    JOB DESCRIPTION:
    {jd_text}
    
    Provide analysis in exactly this format:
    MATCH SCORE: [number out of 100]
    
    MISSING KEYWORDS:
    - [keyword 1]
    - [keyword 2]
    
    MATCHING SKILLS:
    - [skill 1]
    - [skill 2]
    
    SUGGESTIONS:
    - [suggestion 1]
    - [suggestion 2]
    """
    
    response = model.generate_content(prompt)
    return response.text

# 4. Routes
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return "Upload your resume here"

@app.route('/analyze', methods=['POST'])
def analyze():
    userfile = request.files['resume']
    jd = request.form['job_description']
    resume_text = extract_text(userfile)
    analysis = analyze_resume(resume_text, jd)
    
    # Extract match score from analysis text
    match_score = 0
    for line in analysis.split('\n'):
        if 'MATCH SCORE' in line:
            try:
                match_score = int(''.join(filter(str.isdigit, line.split(':')[1][:3])))
            except:
                match_score = 0
    
    # Save to database
    save_to_db(resume_text, jd, match_score, analysis)
    
    return render_template('result.html', analysis=analysis)

# 5. Run
if __name__ == '__main__':
    app.run(debug=True)