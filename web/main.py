import uvicorn
from fastapi import FastAPI
from config.settings import WEBHOOK_URL, PORT, SKIP_WEBHOOK_SETUP
from web.routes.webhook import router as webhook_router
from bot.bot_instance import bot

app = FastAPI(title="Telegram Bot (FastAPI + Aiogram)")
app.include_router(webhook_router)

@app.on_event("startup")
async def on_startup():
    if not SKIP_WEBHOOK_SETUP:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_webhook(WEBHOOK_URL)
        print(f"✅ Webhook установлен: {WEBHOOK_URL}")
    else:
        print("SKIP_WEBHOOK_SETUP=1 — установка webhook пропущена")

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()
    print("Webhook удалён и сессия бота закрыта")

if __name__ == "__main__":
    uvicorn.run("web.main:app", host="0.0.0.0", port=PORT)
