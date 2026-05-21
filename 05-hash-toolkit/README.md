# Hash & Encoding Toolkit

AI-generated Python backend with FastAPI + dark-theme frontend.

## What it does
Three tools in one:
- **Hash**: MD5, SHA-1, SHA-256, SHA-512, Blake2b + Shannon entropy
- **Encode**: Base64, Hex, URL encoding, HTML encoding
- **Decode**: Base64 decode with error handling

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8005`

## API

```
POST /hash    Body: { "text": "..." }
POST /encode  Body: { "text": "..." }
POST /decode  Body: { "encoded": "..." }
```

## Stack
- Python 3.10+
- FastAPI + Uvicorn
- Vanilla HTML/CSS/JS frontend (tabbed interface)
