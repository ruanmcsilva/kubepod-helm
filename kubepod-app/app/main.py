from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "app": "kubepod",
        "status": "running",
        "environment": os.getenv("ENVIRONMENT", "dev")
    }

@app.get("/health")
def health():
    return {"status": "ok."}

