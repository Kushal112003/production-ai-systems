"""RAG service — production FastAPI API. PoW #1 (Dec 2026)."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="production-ai-systems rag-service")


class Health(BaseModel):
    status: str
    version: str


@app.get("/health", response_model=Health)
def health() -> Health:
    return Health(status="ok", version="0.1.0")

class Version(BaseModel):
    version: str

@app.get("/version", response_model=Version)
def version() -> Version:
    return Version(version="0.1.0")
