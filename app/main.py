from fastapi import FastAPI, Request, HTTPException
from app.whatsapp import send_whatsapp_message

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the WhatsApp API BOT"}

@app.get("/send_message")
async def send_message(phone_number: str):

    response = send_whatsapp_message(phone_number)

    try:    
        if response.status_code == 200:
            return {"message": "WhatsApp message sent successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to send message")
    except Exception as e:
        print(f"Error: {e}")