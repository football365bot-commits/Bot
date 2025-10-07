from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from create_bot import bot, 

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}! \n"
        f"Чтобы продолжить, подпишитесь на наш канал: {CHANNEL_USERNAME}",
        reply_markup=check_subscription_kb
    )

# ✅ Создаём клавиатуру сразу с нужной кнопкой
check_subscription_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Проверить подписку",
                callback_data="check_subscription"
            )
        ]
    ]
)


@router.callback_query(lambda c: c.data == "check_subscription")
async def check_subscription(call: CallbackQuery):
    user_id = call.from_user.id
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ["member", "administrator", "creator"]:
            await call.message.answer("Спасибо за подписку! 🎉")
        else:
            await call.message.answer("Похоже, вы ещё не подписались 😕")
    except Exception:
        await call.message.answer(" Не могу проверить подписку,похоже канал не публичный!")
