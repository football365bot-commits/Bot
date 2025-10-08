from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from create_bot import bot, CHANNEL_ID
from start.sub_link import sub_link_buttons


class IsSubskcribedQuery(BaseFilter):
    async def __call__(self, call: CallbackQuery):
        user_id = call.from_user.id
        sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id
        if sub.status != "left":
            return True 
        else:
            await bot.send_message(
                chat_id=user_id,
                text="Подпишитесь чтобы продолжить!",
                reply_markup=sub_link_buttons
            )
