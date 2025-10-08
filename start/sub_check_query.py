from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from create_bot import bot, CHANNEL_ID
from start.sub_link import sub_link_buttons


class IsSubscribedQuery(BaseFilter):
    async def __call__(call: CallbackQuery) -> bool:
        user_id = call.from_user.id
        try:
            # ✅ Проверяем, подписан ли пользователь
            sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

            if sub.status != "left":
                await call.message.answer(
                    Спасибо за подписку!✅ 
                    Выберите язык:",
                    reply_markup=
                    language_keyboard
                
                return True
            else:
                await bot.send_message(
                    chat_id=user_id,
                    text="❌ Подпишитесь, чтобы продолжить!",
                    reply_markup=sub_link_buttons
                )
                return False

        except Exception as e:
            print(f"Ошибка проверки подписки: {e}")
            await bot.send_message(
                chat_id=user_id,
                text="⚠️ Не удалось проверить подписку. Попробуйте позже."
            )
            return False