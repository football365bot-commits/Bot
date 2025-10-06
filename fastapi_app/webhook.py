from fastapi import APIRouter, Request
from bot import dp, bot
from config import BOT_TOKEN

webhook_router = APIRouter()

@webhook_router.post(f"/webhook/{BOT_TOKEN}")
async def process_webhook(request: Request):
    """Обработка входящих вебхуков от Telegram"""
    update = await request.json()
    await dp.feed_webhook_update(bot, update)
    return {"ok": True}
