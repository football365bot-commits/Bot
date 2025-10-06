from aiogram import Router, types
from aiogram.filters import CommandStart
from config.settings import CHANNEL_ID

router = Router()

async def check_subscription(user_id: int, bot: types.Bot) -> bool:
    if not CHANNEL_ID:
        return False
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ("member", "administrator", "creator")
    except Exception:
        return False

@router.message(CommandStart())
async def start_handler(message: types.Message):
    is_sub = await check_subscription(message.from_user.id, message.bot)
    if is_sub:
        await message.answer("✅ Добро пожаловать! Доступ к боту открыт.")
        return

    channel_username = CHANNEL_ID.replace("@", "").strip()
    btn = types.InlineKeyboardButton(
        text="📢 Подписаться на канал",
        url=f"https://t.me/{channel_username}"
    )
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[btn]])

    await message.answer(
        "❌ Вы не подписаны на канал.\nПодпишитесь, чтобы получить доступ к боту:",
        reply_markup=keyboard
    )
