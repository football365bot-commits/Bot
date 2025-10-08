from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from create_bot import bot, CHANNEL_ID

class IsSubscribed(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        try:
            member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
            return member.status in ["member", "administrator", "creator"]
        except Exception as e:
            print(f"Ошибка проверки подписки: {e}")
            return False
