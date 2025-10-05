from config_schema import get_settings

settings = get_settings()

BOT_TOKEN = settings.bot_token
CHANNEL_ID = settings.channel_id
WEBHOOK_HOST = settings.webhook_host