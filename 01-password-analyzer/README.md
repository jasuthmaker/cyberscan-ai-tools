# Password Strength Analyzer

AI-generated Python backend with FastAPI + dark-theme frontend.

## What it does
Analyzes any password and returns:
- Strength label: Weak / Fair / Strong / Very Strong
- Score (0–100)
- Character type checks (uppercase, lowercase, digits, symbols)
- Improvement suggestions

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8001`

## API

```
POST /analyze
Body: { "password": "your_password" }
```

## Stack
- Python 3.10+
- FastAPI + Uvicorn
- Vanilla HTML/CSS/JS frontend
