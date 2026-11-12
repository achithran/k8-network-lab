from fastapi import FastAPI
import httpx
import os

app = FastAPI()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "http://localhost:8002"
)

@app.get("/")
def home():
    return {"service": "Backend", "status": "running"}

@app.get("/process")
async def process():

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DATABASE_URL}/record"
        )

    return {
        "backend": "Order processed",
        "database_response": response.json()
    }