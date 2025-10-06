from fastapi import APIRouter, Request, HTTPException
from aiogram.types import Update
from bot.bot_instance import bot, dp
from config.settings import BOT_TOKEN

router = APIRouter()

@router.post("/webhook/{token}")
async def telegram_webhook(request: Request, token: str):
    if token != BOT_TOKEN:
        raise HTTPException(status_code=403, detail="Forbidden")

    body = await request.json()
    update = Update.model_validate(body, context={"bot": bot})
    await dp.feed_update(update)
    return {"ok": True}
