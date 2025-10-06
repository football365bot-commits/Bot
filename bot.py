from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import BOT_TOKEN, CHANNEL_ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def check_subscription(user_id: int) -> bool:
    """Проверяем подписку на канал"""
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

@dp.message(CommandStart())
async def start(message: types.Message):
    """Обработка команды /start с проверкой подписки"""
    if await check_subscription(message.from_user.id):
        await message.answer("✅ Добро пожаловать! Доступ к боту открыт.")
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                "Подписаться на канал", 
                url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
            )
        )
        await message.answer(
            "❌ Вы не подписаны на канал.\nПодпишитесь, чтобы получить доступ к боту:", 
            reply_markup=keyboard
        )