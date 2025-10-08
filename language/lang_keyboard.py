from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура выбора языка (по 2 кнопки в ряду)
language_keyboard = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data="lang_en"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")
        ],
        [
            InlineKeyboardButton(text="🇪🇸 Español", callback_data="lang_es"),
            InlineKeyboardButton(text="🇫🇷 Français", callback_data="lang_fr")
        ],
        [
            InlineKeyboardButton(text="🇩🇪 Deutsch", callback_data="lang_de"),
            InlineKeyboardButton(text="🇮🇹 Italiano", callback_data="lang_it")
        ],
        [
            InlineKeyboardButton(text="🇵🇹 Português", callback_data="lang_pt"),
            InlineKeyboardButton(text="🇨🇳 中文", callback_data="lang_zh")
        ],
        [
            InlineKeyboardButton(text="🇯🇵 日本語", callback_data="lang_ja"),
            InlineKeyboardButton(text="🇰🇷 한국어", callback_data="lang_ko")
        ]
    ]
)