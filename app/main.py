from fastapi import FastAPI
from app.routes.webhook import router as webhook_router

app = FastAPI(
    title="Sanchaar",
    version="0.1.0"
)

app.include_router(webhook_router)

@app.get("/")
def root():
    return {
        "service": "sanchaar",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "healthy": True
    }