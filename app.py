from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "CI/CD Demo API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}