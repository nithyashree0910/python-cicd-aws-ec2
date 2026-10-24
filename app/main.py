from fastapi import FastAPI

app = FastAPI(
    title="DevOps Deployment API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "DevOps CI/CD Project",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}