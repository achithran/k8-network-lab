from fastapi import FastAPI
import httpx
import os

app = FastAPI()

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8001"
)

@app.get("/")
def home():
    return {"service": "Frontend", "status": "running"}

@app.get("/order")
async def create_order():

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BACKEND_URL}/process"
        )

    return {
        "frontend": "Request received",
        "backend_response": response.json()
    } 