from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import CHANNEL_LINK  # ссылка на канал

# Создаём inline-клавиатуру
sub_link_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписаться✅", url=CHANNEL_LINK)  # кнопка с ссылкой на канал
        ],
        [
            InlineKeyboardButton(text="Проверить подписку🔄", callback_data="sub_link")  # кнопка для проверки подписки
        ]
    ]
)