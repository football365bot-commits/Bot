from aiogram.filters import BaseFilter
from aiogram.types import Message
from create_bot import bot, CHANNEL_ID

class IsSubscribed(BaseFilter):
    async def __call__(self, message:Message):
        user_id = message.from_user.id
        sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if sub.status != "left":
            return True
        else:
            await bot.send_message(
                chat_id=user_id,
                text="Подпишитесь,чтобы получить доступ!"
                repla
            )
            