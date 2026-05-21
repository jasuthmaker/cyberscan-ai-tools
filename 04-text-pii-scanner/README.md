# Text & PII Scanner

AI-generated Python backend with FastAPI + dark-theme frontend.

## What it does
Scans any text for personally identifiable information (PII) and returns:
- PII detected: emails, US phone numbers, SSNs, credit cards, IP addresses
- Sensitive keywords: password, secret, api_key, token, credential, etc.
- Risk level: Clean / Low / Medium / High
- Word count, character count, sentence count

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8004`

## API

```
POST /scan
Body: { "text": "your text here" }
```

## Stack
- Python 3.10+
- FastAPI + Uvicorn
- Vanilla HTML/CSS/JS frontend
