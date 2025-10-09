from aiogram.types import CallbackQuery
from aiogram import Router, F
from language.lang_keyboard import language_keyboard
from start.sub_check_query import IsSubscribedQuery

router = Router()

@router.callback_query(F.data == "sub_done", IsSubscribedQuery())
async def sub_done(call: CallbackQuery):
    # Подписка уже проверена фильтром
    await call.message.edit_text(
        "Спасибо за подписку!✅\nВыберите язык:",
        reply_markup=language_keyboard
    )