from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from create_bot import bot, CHANNEL_ID  # CHANNEL_ID — это ваш канал (@username или числовой ID)

class CallbackIsSubscribed(BaseFilter):
    """
    Фильтр для проверки подписки пользователя на канал через нажатие кнопки.
    """
    def __init__(self, notify: bool = False):
        """
        :param notify: если True, бот отправляет уведомление, что нужно подписаться
        """
        self.notify = notify

    async def __call__(self, call: CallbackQuery) -> bool:
        user_id = call.from_user.id
        try:
            member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
            is_subscribed = member.status in ["member", "administrator", "creator"]

            if not is_subscribed and self.notify:
                await call.message.answer(
                    "❌ Похоже, вы ещё не подписались на канал! "
                    f"Подпишитесь здесь: {CHANNEL_ID}"
                )

            return is_subscribed
        except Exception as e:
            print(f"Ошибка проверки подписки: {e}")
            if self.notify:
                await call.message.answer(
                    "❌ Не удалось проверить подписку. Попробуй позже."
                )
            return False