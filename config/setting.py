import os
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные из .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
WEBHOOK_HOST = os.getenv("WEBHOOK_URL")  # https://bot-1-juge.onrender.com
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"   # путь на сервере
WEBHOOK_URL = WEBHOOK_HOST.rstrip("/") + WEBHOOK_PATH  # полный URL
