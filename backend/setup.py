
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


import os
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")


bot = Bot(token=API_TOKEN)
dp = Dispatcher()
app = FastAPI()


