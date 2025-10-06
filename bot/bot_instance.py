from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

BOT_TOKEN = "BOT_TOKEN"

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)
    disable_web_page_preview=True,
    protect_content=True
dp = Dispatcher(bot)

from bot.routers.start import router as start_router  # noqa
dp.include_router(start_router)
