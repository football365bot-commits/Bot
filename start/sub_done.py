from aiogram import Router, types, F
from language.lang_keyboard import language_keyboard
from start.sub_link import sub_link_buttons
from create_bot import bot, CHANNEL_ID

router = Router()

@router.callback_query(F.data == "sub_done")
async def sub_done(call: types.CallbackQuery):
    """
    Callback для кнопки "Проверить подписку"
    """
    await call.answer()  # убираем кружок Telegram

    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
        is_subscribed = member.status != "left"
    except Exception:
        is_subscribed = False

    if is_subscribed:
        await call.message.edit_text(
            "Спасибо за подписку! ✅\nВыберите язык:",
            reply_markup=language_keyboard
        )
    else:
        await call.message.edit_text(
            "❌ Подпишитесь на канал, чтобы продолжить!",
            reply_markup=sub_link_buttons
        )

