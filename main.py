from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI application!"}