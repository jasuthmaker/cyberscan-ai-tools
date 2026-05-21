from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from core.password import analyze_password
from core.ip       import classify_ip
from core.url      import analyze_url
from core.text     import scan_text
from core.hash     import hash_text, encode_text, decode_base64

app = FastAPI(title="CyberScan AI Suite", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request models ───────────────────────────────────────────────────────────
class PasswordReq(BaseModel):
    password: str

class IPReq(BaseModel):
    ip: str

class URLReq(BaseModel):
    url: str

class TextReq(BaseModel):
    text: str

class DecodeReq(BaseModel):
    encoded: str


# ── Routes ───────────────────────────────────────────────────────────────────
@app.get("/")
def index():
    return FileResponse("frontend/index.html")

@app.post("/api/password")
def password_route(req: PasswordReq):
    return analyze_password(req.password)

@app.post("/api/ip")
def ip_route(req: IPReq):
    return classify_ip(req.ip)

@app.post("/api/url")
def url_route(req: URLReq):
    return analyze_url(req.url)

@app.post("/api/text")
def text_route(req: TextReq):
    return scan_text(req.text)

@app.post("/api/hash")
def hash_route(req: TextReq):
    return hash_text(req.text)

@app.post("/api/encode")
def encode_route(req: TextReq):
    return encode_text(req.text)

@app.post("/api/decode")
def decode_route(req: DecodeReq):
    return decode_base64(req.encoded)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
