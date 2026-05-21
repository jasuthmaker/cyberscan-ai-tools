# CyberScan AI Tools

5 production-ready cybersecurity tools built by an AI agent loop (Manager → Developer → Tester).

Each app is independent: Python core logic generated and tested by agents, wrapped with FastAPI + a dark-theme HTML frontend.

---

## Apps

| # | App | Port | Description |
|---|-----|------|-------------|
| 1 | [Password Analyzer](./01-password-analyzer/) | 8001 | Strength score, character checks, improvement tips |
| 2 | [IP Classifier](./02-ip-classifier/)         | 8002 | IPv4/IPv6 classification, class, private/global flags |
| 3 | [URL Analyzer](./03-url-analyzer/)           | 8003 | Risk scoring, suspicious TLD/IP/path detection |
| 4 | [Text & PII Scanner](./04-text-pii-scanner/) | 8004 | Detect emails, phones, SSNs, credit cards, keywords |
| 5 | [Hash & Encoding Toolkit](./05-hash-toolkit/)| 8005 | MD5/SHA/Blake2b hashing, Base64/Hex/URL encoding |

---

## Quick Start

Each app runs independently:

```bash
cd 01-password-analyzer
pip install -r requirements.txt
python app.py
```

Then open the URL shown in the terminal (e.g. `http://localhost:8001`).

---

## Architecture

```
app/
├── core.py          # AI-generated business logic (tested by agent loop)
├── app.py           # FastAPI wrapper + CORS
├── frontend/
│   └── index.html   # Dark-theme single-page UI
├── requirements.txt
└── README.md
```

---

## How it was built

An agent loop ran three specialized agents:

1. **Manager** — turned a task description into a detailed developer brief
2. **Developer** — wrote production Python code from the brief
3. **Tester** — ran the code in an isolated subprocess, returned PASS/FAIL + error
4. If FAIL: Developer fixed the code and Tester re-ran (up to 3 attempts)

All 5 apps passed on the **first attempt** with zero fixes needed.

---

## Stack

- Python 3.10+
- FastAPI + Uvicorn
- Tailwind CSS (CDN)
- Vanilla JavaScript
- NVIDIA NIM API (Llama 3.3 70B) for code generation
