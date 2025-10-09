from aiogram import Router, types
from start.sub_link import sub_link_buttons
from language.lang_keyboard import language_keyboard
from create_bot import bot, CHANNEL_ID
from start.sub_check_message import IsSubscribedMessage

router = Router()

@router.message(IsSubscribedMessage())
async def handle_subscribed(message: types.Message):
    # Пользователь подписан — показываем выбор языка
    await message.answer(
        "Спасибо за подписку!✅\nВыберите язык:",
        reply_markup=language_keyboard
    )

@router.message(~IsSubscribedMessage())  # Обратный фильтр для неподписанных
async def handle_unsubscribed(message: types.Message):
    await message.answer(
        "❌ Подпишитесь на канал, чтобы продолжить!",
        reply_markup=sub_link_buttons
    )