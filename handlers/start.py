from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.filters.text import Text
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from create_bot import bot, CHANNEL_USERNAME, CHANNEL_ID
from filters.is_subscribed import IsSubscribed
from aiogram.exceptions import TelegramBadRequest

router = Router()

# 🔹 Ссылка на канал
CHANNEL_LINK = f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}"

# ✅ Кнопка проверки подписки
check_subscription_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Проверить подписку", callback_data="check_subscription")]
    ]
)

# ✅ /start
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}! 👋\n"
        f"Чтобы продолжить, подпишитесь на канал: {CHANNEL_USERNAME}",
        reply_markup=check_subscription_kb
    )

# ✅ Callback для проверки подписки
@router.callback_query(IsSubscribed(), Text("check_subscription"))
async def check_subscription_callback(call: CallbackQuery):
    await call.answer()  # скрываем "Загрузка..."
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            await call.message.edit_text(
                "Спасибо за подписку! 🎉 Добро пожаловать!"
            )
        else:
            await call.message.edit_text(
                f"Похоже, вы ещё не подписались 😕\n"
                f"Подпишитесь здесь: {CHANNEL_LINK} и попробуйте снова!",
                reply_markup=check_subscription_kb
            )
    except TelegramBadRequest:
        # Если пользователь не найден в канале
        await call.message.edit_text(
            f"Похоже, вы ещё не подписались 😕\n"
            f"Подпишитесь здесь: {CHANNEL_LINK} и попробуйте снова!",
            reply_markup=check_subscription_kb
        )
    except Exception as e:
        await call.message.edit_text(f"Не могу проверить подписку! Ошибка: {e}")
        print(f"Ошибка проверки подписки: {e}")