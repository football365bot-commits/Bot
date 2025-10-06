import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Токен бота
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")  # URL вашего сервера
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"   # Путь для вебхука
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
CHANNEL_ID = os.getenv("CHANNEL_ID")    # Ваш канал
