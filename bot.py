import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN, WEBHOOK_HOST
from handlers.start import router as start_router

# Уникальный путь для webhook
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Порт, который Render или сервер предоставляет через переменную окружения
import os
PORT = int(os.getenv("PORT", 8443))  # 8443 по умолчанию для webhook

async def main():
    # Создаём экземпляр бота
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)

    # Удаляем старый webhook, если он был
    await bot.delete_webhook(drop_pending_updates=True)

    # Создаём веб-приложение aiohttp
    app = web.Application()

    # Запуск webhook сервера
    await dp.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        bot=bot,
        skip_updates=True,
        host="0.0.0.0",  # слушаем все интерфейсы
        port=PORT,
        web_app=app
    )

if __name__ == "__main__":
    print(f"🚀 Бот запускается с webhook на {WEBHOOK_URL}")
    asyncio.run(main())