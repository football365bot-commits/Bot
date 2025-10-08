from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from create_bot import bot, CHANNEL_USERNAME, CHANNEL_LINK, CHANNEL_ID
from filters.is_subscribed import IsSubscribed

router = Router()

# ✅ Кнопки /start
start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подписаться", url=CHANNEL_LINK)],
        [InlineKeyboardButton(text="Проверить подписку", callback_data="check_subscription")]
    ]
)

# ✅ Команда /start
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}! 👋\n"
        f"Чтобы продолжить, подпишитесь на канал.",
        reply_markup=start_kb
    )

# ✅ Callback: подписан
@router.callback_query(IsSubscribed(), lambda c: c.data == "check_subscription")
async def subscribed_callback(call: CallbackQuery):
    # Обновляем текст того же сообщения
    await call.message.edit_text("✅ Спасибо за подписку! 🎉 Добро пожаловать!")
    await call.answer()  # скрываем "загрузка..."

# ❌ Callback: не подписан
@router.callback_query(lambda c: c.data == "check_subscription")
async def not_subscribed_callback(call: CallbackQuery):
    # Обновляем сообщение, оставляем кнопки
    await call.message.edit_text(
        f"😕 Похоже, вы ещё не подписались.\nПодпишитесь здесь 👉 {CHANNEL_LINK}",
        reply_markup=call.message.reply_markup
    )
    await call.answer()  # скрываем "загрузка..."