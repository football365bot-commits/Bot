from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from create_bot import bot, CHANNEL_USERNAME, CHANNEL_LINK
from filters.is_subscribed import IsSubscribed

router = Router()

# ✅ Кнопки
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

@router.callback_query(lambda c: c.data == "check_subscription")
async def check_subscription(call: CallbackQuery):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            await call.answer()
            await call.message.answer("Спасибо за подписку! 🎉 Добро пожаловать!")
        else:
            await call.answer()
            await call.message.answer(
                f"Похоже, вы ещё не подписались 😕\n"
                f"Подпишитесь здесь: {CHANNEL_LINK} и попробуйте снова!"
            )
    except Exception as e:
        await call.message.answer(f"⚠️ Ошибка проверки подписки: {e}")