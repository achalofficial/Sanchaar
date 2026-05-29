from fastapi import FastAPI

app = FastAPI(
    title="Sanchaar",
    version="0.1.0"
)


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