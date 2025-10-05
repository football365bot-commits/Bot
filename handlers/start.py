from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.exceptions import TelegramBadRequest

from keyboards.start_keyboard import subscription_keyboard
from config import CHANNEL_ID

router = Router()

@router.message(CommandStart("/start"))
async def cmd_start(message: Message):
    """
    Команда /start — предлагает пользователю подписаться.
    """
    await message.answer(
        "👋 Привет! Чтобы пользоваться ботом, подпишись на наш канал:",
        reply_markup=subscription_keyboard
    )

@router.callback_query(F.data == "check_subscription")
async def check_subscription(callback: CallbackQuery):
    """
    Проверка подписки после нажатия кнопки.
    """
    bot = callback.message.bot
    user_id = callback.from_user.id

    if await is_subscribed(bot, user_id):
        await callback.message.edit_text(
            "🎉 Отлично! Подписка подтверждена. Теперь тебе доступен функционал бота."
        )
        await callback.answer()
    else:
        await callback.answer("❌ Ты ещё не подписан!", show_alert=True)
        
        
async def is_subscribed(bot, user_id: int) -> bool:
    """
    Проверка подписки пользователя.
    Бот должен быть администратором канала.
    """
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status in ("member", "creator", "administrator")
    except TelegramBadRequest:
        return False





