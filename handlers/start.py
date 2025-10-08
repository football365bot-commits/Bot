from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from create_bot import bot, CHANNEL_LINK
from filters.is_subscribed import IsSubscribedMessage

router = Router()

# ✅ Клавиатура с кнопками
start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подписаться", url=CHANNEL_LINK)],
        [InlineKeyboardButton(text="Проверить подписку", callback_data="check_subscription")]
    ]
)

# ✅ /start
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}! 👋\n"
        f"Чтобы продолжить, подпишитесь на канал.",
        reply_markup=start_kb
    )

# ✅ Callback «Проверить подписку» с фильтром
@router.callback_query(IsSubscribedMessage(), lambda c: c.data == "check_subscription")
async def subscribed_callback(call: CallbackQuery):
    await call.answer()  # скрывает «Загрузка...»
    await call.message.answer("Спасибо за подписку! 🎉 Добро пожаловать!")

# ❌ Callback, если не подписан
@router.callback_query(lambda c: c.data == "check_subscription")
async def not_subscribed_callback(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        f"Похоже, вы ещё не подписались 😕\n"
        f"Подпишитесь здесь: {CHANNEL_LINK} и попробуйте снова!",
        reply_markup=start_kb
    )