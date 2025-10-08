# issubscribet.py

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from create_bot import bot, CHANNEL_ID

class IsSubscribed(BaseFilter):
    """
    Фильтр для проверки, подписан ли пользователь на канал.
    Используется для CallbackQuery.
    """

    async def __call__(self, call: CallbackQuery) -> bool:
        try:
            member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
            # Пользователь подписан, если его статус member, administrator или creator
            return member.status in ["member", "administrator", "creator"]
        except TelegramBadRequest:
            # Пользователь не найден в канале → не подписан
            return False
        except Exception as e:
            # Логируем непредвиденные ошибки
            print(f"[IsSubscribed] Ошибка проверки подписки для {call.from_user.id}: {e}")
            return False