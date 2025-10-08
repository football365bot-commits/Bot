from aiogram.filters import CommandStart
from aiogram import Router, F
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

@router.callback_query(F.data == "check_subscription")
async def check_subscription(call.CallbackQuery):
    await call.message.edit_text("Вы подписались🎉")