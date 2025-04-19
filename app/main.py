from fastapi import FastAPI, Request, HTTPException
from app.whatsapp import send_whatsapp_message
from app.utils import is_valid_phone

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the WhatsApp API BOT"}

@app.get("/send_message")
async def send_message(phone_number: str):
    if not is_valid_phone(phone_number):
        raise HTTPException(status_code=400, detail="Invalid phone number format")
    
    response = send_whatsapp_message(phone_number)
    
    if response.status_code == 200:
        return {"message": "WhatsApp message sent successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to send message")
