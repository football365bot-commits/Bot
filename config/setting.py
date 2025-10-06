import os
from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = os.getenv("WEBHOOK_URL") 
CHANNEL_ID = os.getenv("CHANNEL_ID")
