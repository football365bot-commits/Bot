import uvicorn
from aiogram.filters import Command
from aiogram.types import Message
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from config.setting import BOT_TOKEN, WEBHOOK_PATH, WEBHOOK_URL, CHANNEL_ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()

# ------------------- Startup / Shutdown -------------------
@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)
    print(f"✅ Webhook установлен: {WEBHOOK_URL}")

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()
    print("🛑 Webhook удален, бот остановлен")

# ------------------- Webhook -------------------
@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update
    return {"ok": True}

# ------------------- Простейший старт -------------------
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Бот работает.")

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Подписаться на канал", url=CHANNEL_ID)]
        ]
    )
    await message.answer("Привет! Подпишись на канал, чтобы пользоваться ботом:", reply_markup=keyboard)

# ------------------- Тест сервера -------------------
@app.get("/")
async def root():
    return {"status": "Bot webhook server is running"}

if __name__ == "__main__":
    uvicorn.run("bot:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
