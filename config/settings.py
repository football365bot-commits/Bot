import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID", "")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "").rstrip("/")
PORT = int(os.getenv("PORT", "8000"))
SKIP_WEBHOOK_SETUP = os.getenv("SKIP_WEBHOOK_SETUP", "0").lower() in ("1", "true", "yes")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in environment")

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
