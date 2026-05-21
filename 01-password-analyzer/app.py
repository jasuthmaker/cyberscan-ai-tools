from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from core import analyze_password

app = FastAPI(title="Password Strength Analyzer", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class PasswordRequest(BaseModel):
    password: str


@app.get("/")
def index():
    return FileResponse("frontend/index.html")


@app.post("/analyze")
def analyze(req: PasswordRequest):
    return analyze_password(req.password)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
