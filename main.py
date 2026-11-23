from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hi"}
@app.get("/ping")
def ping():
    return {"status": "ok"}