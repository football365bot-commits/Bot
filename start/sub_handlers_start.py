from aiogram.filters import CommandStart
from aiogram import Router, types
from create_bot import bot, CHANNEL_ID
from start.sub_link import sub_link_buttons
from language.lang_keyboard import language_keyboard

router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    """
    /start — проверка подписки и показ нужной клавиатуры
    """
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
        is_subscribed = member.status not in ["left", "kicked"]
    except Exception:
        is_subscribed = False

    if is_subscribed:
        text = f"Добро пожаловать, {message.from_user.full_name}! 👋\nВы уже подписаны ✅\nВыберите язык:"
        keyboard = language_keyboard
    else:
        text = f"Добро пожаловать, {message.from_user.full_name}! 👋\nПроверьте подписку, чтобы продолжить 👇"
        keyboard = sub_link_buttons

    await message.answer(text, reply_markup=keyboard)