import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query

load_dotenv()

API_KEY = os.getenv("D360_API_KEY")
print(f"API_KEY: {API_KEY}")  # Debugging line to check if API_KEY is loaded correctly
SANDBOX_URL = "https://waba-sandbox.360dialog.io/v1/messages"

app = FastAPI()

def send_whatsapp_message(phone_number: str):
    headers = {
        "D360-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_number,  # use the actual number passed in
        "type": "text",
        "text": {
            "body": "Hello from FastAPI via 360dialog Sandbox!"
        }
    }

    response = requests.post(SANDBOX_URL, headers=headers, json=payload)

    if response.status_code == 201:
        return {"message": "Message sent successfully"}
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)