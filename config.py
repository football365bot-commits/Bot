from config_schema import get_settings
import os
PORT = int(os.getenv("PORT", 8080))

settings = get_settings()
settings = Settings()

BOT_TOKEN = settings.BOT_TOKEN
CHANNEL_ID = settings.CHANNEL_IF
WEBHOOK_HOST = settings.WEBHOOK_HOST.rstrip("/")
WEBHOOK_PATH = settings.WEBHOOK_PACH.lstrip("/")
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

