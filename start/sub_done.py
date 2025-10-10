from aiogram import Router, types, F
from create_bot import bot, CHANNEL_ID
from start.sub_link import sub_link_buttons
from language.lang_keyboard import language_keyboard

router = Router()

@router.callback_query(F.data == "sub_done")
async def sub_done(call: types.CallbackQuery):
    """
    Обработчик нажатия кнопки "Проверить подписку"
    """
    await call.answer("Проверяем подписку...", show_alert=False)

    try:
        # Получаем информацию о пользователе в канале
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
        is_subscribed = member.status not in ["left", "kicked"]
    except Exception as e:
        print("Ошибка проверки подписки:", e)
        is_subscribed = False

    if is_subscribed:
        text = "Спасибо за подписку! ✅\nВыберите язык:"
        reply_markup = language_keyboard
    else:
        text = "❌ Подпишитесь на канал, чтобы продолжить!"
        reply_markup = sub_link_buttons

    # Пытаемся отредактировать сообщение, если нельзя — просто отправляем новое
    try:
        await call.message.edit_text(text, reply_markup=reply_markup)
    except:
        await call.message.reply(text, reply_markup=reply_markup)