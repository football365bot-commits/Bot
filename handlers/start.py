from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from create_bot import bot, CHANNEL_USERNAME, CHANNEL_ID
from filters.is_subscribed import IsSubscribed

router = Router()

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
@router.callback_query(lambda c: c.data == "check_subscription")
async def check_subscription_callback(call: CallbackQuery):
    await call.answer()  # скрываем "Загрузка..."
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)
        if member.status in ["member", "administrator", "creator"]:
            await call.message.answer("Спасибо за подписку! 🎉 Добро пожаловать!")
        else:
            await call.message.answer(
                f"Похоже, вы ещё не подписались 😕\n"
                f"Подпишитесь здесь: {CHANNEL_LINK} и попробуйте снова!"
            )
    except Exception as e:
        await call.message.answer(f"Не могу проверить подписку! Ошибка: {e}")
        print(f"Ошибка проверки подписки: {e}")