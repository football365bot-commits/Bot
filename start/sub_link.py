from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import CHANNEL_LINK


sub_link_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(text="Подпишитесь✅", url=CHANNEL_LINK)
    ],
    [
    InlineKeyboardButton(text="Проверить подписку🔄", callback_data="sub_done")
    ]

])