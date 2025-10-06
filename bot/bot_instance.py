from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

from bot.routers.start import router as start_router  # noqa
dp.include_router(start_router)
