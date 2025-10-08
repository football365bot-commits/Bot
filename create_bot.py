from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config

BOT_TOKEN = config("BOT_TOKEN")
ADMIN_ID = config("ADMIN_ID")
HOST = config("HOST")
PORT = int(config("PORT"))
WEBHOOK_PATH = f'/{BOT_TOKEN}'
BASE_URL = config("BASE_URL")
CHANNEL_USERNAME = config("CHANNEL_USERNAME")
CHANNEL_LINK = config("CHANNEL_LINK")
CHANNEL_ID = config("CHANNEL_ID")
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()