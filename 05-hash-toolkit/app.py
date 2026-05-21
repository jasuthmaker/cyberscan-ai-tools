from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from core import hash_text, encode_text, decode_base64

app = FastAPI(title="Hash & Encoding Toolkit", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


class DecodeRequest(BaseModel):
    encoded: str


@app.get("/")
def index():
    return FileResponse("frontend/index.html")


@app.post("/hash")
def hash_endpoint(req: TextRequest):
    return hash_text(req.text)


@app.post("/encode")
def encode_endpoint(req: TextRequest):
    return encode_text(req.text)


@app.post("/decode")
def decode_endpoint(req: DecodeRequest):
    return decode_base64(req.encoded)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8005, reload=True)
