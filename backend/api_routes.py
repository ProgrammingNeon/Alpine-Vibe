from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
import uvicorn
from database import session_factory
from models import ContactMessage
from schemas import ContactCreate

from fastapi import APIRouter

from aiogram import types



import os
from dotenv import load_dotenv

from setup import  bot



main_router = APIRouter()

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")






def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()



@main_router.post("/submit-contact")
async def create_contact_and_send_tg(contact: ContactCreate, db: Session = Depends(get_db)):
    
    f_name = contact.first_name.strip()
    l_name = contact.last_name.strip()
    phone_clean = "".join(filter(str.isdigit, contact.phone)) 

    if not f_name or not l_name:
        raise HTTPException(status_code=400, detail="Ім'я не може бути порожнім")
    
    
    new_message = ContactMessage(
        first_name=contact.first_name,
        last_name=contact.last_name,
        email=contact.email,
        phone=contact.phone,
        # subject=contact.subject,
        message=contact.message
    )
    
    try:
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        
        # phone_formatted = contact.phone if contact.phone.startswith('+') else f"+{contact.phone}"
        # phone_url = phone_formatted.replace('-', '').replace(' ', '')

        tg_text = (
            f"🚀 **Нова заявка з сайту!**\n\n"
            f"👤 Ім'я: {f_name} {l_name}\n"
            f"📧 Email: {contact.email}\n"
            f"📞 Телефон: `{phone_clean}`\n"
            # f"📝 Тема: {contact.subject}\n"
            f"💬 Повідомлення: {contact.message.strip()}\n\n"
            f"🔗 [Написати в Telegram](https://t.me/+{phone_clean})"
        )
        
        if phone_clean:
            await bot.send_message(chat_id=ADMIN_ID, text=tg_text, parse_mode="Markdown")
        return {"status": "success", "id": new_message.id}
        
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))