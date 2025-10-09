from aiogram import Router, types, F
from language.lang_keyboard import language_keyboard
from start.sub_check_query import IsSubscribedQuery
from start.sub_link import sub_link_buttons  # кнопки для подписки
from create_bot import bot, CHANNEL_ID

router = Router()

@router.callback_query(F.data == "sub_done")
async def sub_done(call: types.CallbackQuery):
    
    await call.message.edit_text(
                "Спасибо за подписку!✅\nВыберите язык:",
                reply_markup=language_keyboard
            )
        else:
            await call.message.answer(
                "❌ Подпишитесь на канал, чтобы продолжить!",
                reply_markup=sub_link_buttons
            )
    