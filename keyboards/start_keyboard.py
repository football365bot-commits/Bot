from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_ID

subscription_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Подписаться на канал",
                url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Проверить подписку",
                callback_data="check_subscription"
            )
        ]
    ]
)