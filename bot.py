import logging
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from start.start_bot import router as start_router

from create_bot import bot, dp, BASE_URL, WEBHOOK_PATH, HOST, PORT, ADMIN_ID

async def set_commands():
    commands = [BotCommand(command='start', description='Старт')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

async def on_startup() -> None:
    await set_commands()
    await bot.set_webhook(f"{BASE_URL}{WEBHOOK_PATH}")
    await bot.send_message(chat_id=ADMIN_ID, text='✅ Бот запущен!')

async def on_shutdown() -> None:
    await bot.send_message(chat_id=ADMIN_ID, text='🛑 Бот остановлен!')
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()

def main() -> None:
    dp.include_router(start_router)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()
    webhook_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=HOST, port=PORT)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    main()
