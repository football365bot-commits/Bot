from aiogram.filters import BaseFilter
from aiogram.types import Message
from create_bot import bot, CHANNEL_ID


class IsSubscribedMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        try:
            sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
            return sub.status != "left"
        except Exception as e:
            print(f"Ошибка при проверке подписки: {e}")
            return False