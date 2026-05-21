from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from core import classify_ip

app = FastAPI(title="IP Address Classifier", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class IPRequest(BaseModel):
    ip: str


@app.get("/")
def index():
    return FileResponse("frontend/index.html")


@app.post("/classify")
def classify(req: IPRequest):
    return classify_ip(req.ip)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8002, reload=True)
