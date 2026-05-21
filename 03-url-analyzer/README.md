# URL Security Analyzer

AI-generated Python backend with FastAPI + dark-theme frontend.

## What it does
Analyzes any URL for security risks and returns:
- Risk score (0–100) and risk level (Safe / Low / Medium / High / Critical)
- Detected risks: IP host, suspicious TLD, shortened URL, path keywords
- URL breakdown: scheme, domain, path, subdomain count

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8003`

## API

```
POST /analyze
Body: { "url": "https://example.com/path" }
```

## Stack
- Python 3.10+
- FastAPI + Uvicorn
- Vanilla HTML/CSS/JS frontend
