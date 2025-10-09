from aiogram.filters import CommandStart
from aiogram import Router
from aiogram import Message
from create_bot import bot
from start.sub_link import sub_link_buttons
from language.lang_keyboard import language_keyboard
from aiogram import types




router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    """
    /start — проверка подписки сразу и отправка правильной клавиатуры
    """
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
        is_subscribed = member.status != "left"
    except Exception:
        is_subscribed = False  # если не удалось проверить — считаем, что не подписан

    if is_subscribed:
        text = f"Добро пожаловать, {message.from_user.full_name}! 👋\nВы уже подписаны ✅\nВыберите язык:"
        keyboard = language_keyboard
    else:
        text = f"Добро пожаловать, {message.from_user.full_name}! 👋\nПроверьте подписку, чтобы продолжить 👇"
        keyboard = sub_link_buttons






