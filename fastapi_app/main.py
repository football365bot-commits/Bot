import uvicorn
from fastapi import FastAPI
from config import WEBHOOK_URL, BOT_TOKEN, PORT
from bot import dp, bot
from fastapi_app.webhook import webhook_router

app = FastAPI()
app.include_router(webhook_router, prefix="")

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)
    print(f"✅ Webhook установлен: {WEBHOOK_URL}")

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()
    print("🛑 Webhook удалён, бот остановлен")

if __name__ == "__main__":
    uvicorn.run("fastapi_app.main:app", host="0.0.0.0", port=PORT)
