from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from create_bot import bot, CHANNEL_ID
from handlers.start import start_kb  # клавиатура с кнопками

class IsSubscribedMessage(BaseFilter):
    # Проверка для сообщений
    async def check_message(self, message: Message) -> bool:
        user_id = message.from_user.id
        sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if sub.status != "left":
            return True
        else:
            await message.answer(
                text="❌ Подпишитесь, чтобы получить доступ!",
                reply_markup=start_kb
            )
            return False

    # Проверка для callback
    async def check_callback(self, call: CallbackQuery) -> bool:
        user_id = call.from_user.id
        sub = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if sub.status != "left":
            return True
        else:
            await call.message.answer(
                text="❌ Подпишитесь, чтобы получить доступ!",
                reply_markup=start_kb
            )
            return False

    # __call__ позволяет использовать фильтр напрямую для CallbackQuery
    async def __call__(self, obj) -> bool:
        if isinstance(obj, CallbackQuery):
            return await self.check_callback(obj)
        elif isinstance(obj, Message):
            return await self.check_message(obj)
        return False