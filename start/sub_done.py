from aiogram import Router, types, F
from language.lang_keyboard import language_keyboard
from start.sub_link import sub_link_buttons
from create_bot import bot, CHANNEL_ID
from start.sub_check_query import IsSubscribedQuery

router = Router()

@router.callback_query(F.data == "sub_done", IsSubscribedQuery())
async def sub_done(call: types.CallbackQuery):
    member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
    
    if member.status != "left":
        # Пользователь подписан — показываем выбор языка
        await call.message.edit_text(
            "Спасибо за подписку!✅\nВыберите язык:",
            reply_markup=language_keyboard
        )
    else:
        # Пользователь не подписан — показываем сообщение с кнопкой подписки
        await call.message.answer(
            "❌ Подпишитесь на канал, чтобы продолжить!",
            reply_markup=sub_link_buttons
        )