from aiogram.types import CallbackQuery
from aiogram import types, Router, F
from language.lang_keyboard import language_keyboard
from create_bot import bot
from create_bot import CHANNEL_ID
from start.sub_check_query import IsSubscribedQuery



router = Router()

@router.callback_query(F.data == "sub_done", IsSubscribedQuery())
async def sub_done(call: types.CallbackQuery):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
        if member.status != "left":
            await call.message.edit_text(
                "Спасибо за подписку!✅\nВыберите язык:",
                reply_markup=language_keyboard
            )
        else:
            await bot.send_message(
                chat_id=call.from_user.id,
                text="❌ Подпишитесь, чтобы продолжить!"
            )
    except Exception as e:
        print(f"Ошибка при проверке подписки в хендлере: {e}")