import asyncio
from click import Command
import uvicorn
from fastapi import FastAPI, types
import asyncio
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from api_routes import main_router


import os
from dotenv import load_dotenv

from setup import app, dp, bot

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")


app.include_router(main_router)



origins = [
    "https://programmingneon.github.io/Alpine-Vibe/", 
    "http://localhost",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)







@app.get("/")
async def root():
    return {"message": "Сайт працює, бот теж!"}
@dp.message(Command("start"))
async def start(msg: types.Message, state: FSMContext):
    await msg.answer("Admin AlpsTravel BOT Вітає вас!")






async def run_fastapi():
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def run_bot():
    await dp.start_polling(bot)

async def main():
    await asyncio.gather(
        run_fastapi(),
        run_bot()
    )



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Вихід...")


   