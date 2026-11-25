import secrets

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()

# Temporary storage: short code -> long URL. Wiped when the server restarts.
urls = {}


class ShortenRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"message": "hi"}


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.post("/shorten")
def shorten(body: ShortenRequest):
    code = secrets.token_urlsafe(4)
    urls[code] = body.url
    return {"code": code, "short_url": f"http://localhost:8000/{code}"}


@app.get("/{code}")
def go(code: str):
    if code not in urls:
        raise HTTPException(status_code=404, detail="Short link not found")
    return RedirectResponse(urls[code])
