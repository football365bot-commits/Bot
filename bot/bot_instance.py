from aiogram import Bot, Dispatcher
from aiogram.types import DefaultBotProperties

BOT_TOKEN = "BOT_TOKEN"

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)
dp = Dispatcher(bot)

from bot.routers.start import router as start_router  # noqa
dp.include_router(start_router)
