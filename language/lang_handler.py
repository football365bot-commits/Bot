from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from .Keyboard import language_keyboard

router = Router()

# Словарь для хранения выбранного языка пользователем
# key = user_id, value = lang_code
user_languages = {}

# Словарь переводов для примера
translations = {
    "en": {"welcome": "Welcome! 👋", "language_selected": "You selected English 🇺🇸"},
    "ru": {"welcome": "Добро пожаловать! 👋", "language_selected": "Вы выбрали русский 🇷🇺"},
    "es": {"welcome": "¡Bienvenido! 👋", "language_selected": "Has seleccionado Español 🇪🇸"},
    "fr": {"welcome": "Bienvenue! 👋", "language_selected": "Vous avez choisi Français 🇫🇷"},
    "de": {"welcome": "Willkommen! 👋", "language_selected": "Sie haben Deutsch gewählt 🇩🇪"},
    "it": {"welcome": "Benvenuto! 👋", "language_selected": "Hai scelto Italiano 🇮🇹"},
    "pt": {"welcome": "Bem-vindo! 👋", "language_selected": "Você selecionou Português 🇵🇹"},
    "zh": {"welcome": "欢迎! 👋", "language_selected": "您选择了中文 🇨🇳"},
    "ja": {"welcome": "ようこそ! 👋", "language_selected": "日本語を選択しました 🇯🇵"},
    "ko": {"welcome": "환영합니다! 👋", "language_selected": "한국어를 선택했습니다 🇰🇷"}
}

# Отправка клавиатуры выбора языка
@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer(
        "Пожалуйста, выберите язык / Please select your language:",
        reply_markup=language_keyboard
    )

# Обработка выбора языка
@router.callback_query(F.data.startswith("lang_"))
async def language_selected(call: CallbackQuery):
    lang_code = call.data.split("_")[1]
    user_languages[call.from_user.id] = lang_code  # сохраняем выбор

    await call.answer()  # скрываем "Загрузка..."
    await call.message.edit_text(translations[lang_code]["language_selected"])