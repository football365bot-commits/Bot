from config_schema import get_settings
import os
PORT = int(os.getenv("PORT", 8080))

settings = get_settings()

BOT_TOKEN = settings.bot_token
CHANNEL_ID = settings.channel_id
WEBHOOK_HOST = settings.webhook_host
WEBHOOK_PATH = f"/webhook{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

