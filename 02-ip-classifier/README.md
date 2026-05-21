# IP Address Classifier

AI-generated Python backend with FastAPI + dark-theme frontend.

## What it does
Classifies any IPv4 or IPv6 address and returns:
- Valid / Invalid
- IP version (IPv4 / IPv6)
- Private, loopback, multicast, global flags
- IP Class (A/B/C/D/E for IPv4)
- Human-readable description

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:8002`

## API

```
POST /classify
Body: { "ip": "8.8.8.8" }
```

## Stack
- Python 3.10+
- FastAPI + Uvicorn
- Vanilla HTML/CSS/JS frontend
