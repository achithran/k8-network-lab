from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"service": "Database API", "status": "running"}

@app.get("/record")
def get_record():
    return {
        "database": "Connected successfully",
        "order_id": 101,
        "product": "Laptop"
    }