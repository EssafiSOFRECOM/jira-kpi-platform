from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="JIRA KPI Platform",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app_name": os.getenv("APP_NAME", "jira-kpi-platform")
    }