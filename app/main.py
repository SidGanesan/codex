from typing import Dict
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root() -> Dict[str, str]:
    return {"message": "Codex"}


@app.post("/sync")
def sync() -> Dict[str, str]:
    return {"message": "Completed"}
