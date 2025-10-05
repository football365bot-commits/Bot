import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler

from config import BOT_TOKEN, WEBHOOK_HOST
from handlers.start import router as start_router

WEBHOOK_PATH = f"/webhook{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

import os
PORT = int(os.getenv("PORT", 8080))

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)

async def handle(request):
    request_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    update_data = await request.json()
    update = Update(**update_data)
    await request_handler(update)
    return web.Response(text="OK")

app = web.Application()
app.router.add_post(WEBHOOK_PATH, handle)

async def on_startup(app):
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(WEBHOOK_URL)
    print(f"🚀 Webhook установлен: {WEBHOOK_URL}")

app.on_startup.append(on_startup)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=PORT)