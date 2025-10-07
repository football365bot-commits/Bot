from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from create_bot import bot, CHANNEL_USERNAME, CHANNEL_LINK


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}! \n"
        f"Чтобы продолжить, подпишитесь на наш канал: {CHANNEL_LINK}",
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
    
    await call.answer()
    
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)

        # ✅ Проверка подписки с логированием статуса
        if member.status in ["member", "administrator", "creator"]:
            await call.message.answer("Спасибо за подписку! 🎉")
        elif member.status in ["left", "kicked"]:
            await call.message.answer("Похоже, вы ещё не подписались 😕")
        else:
            await call.message.answer(f"Статус пользователя: {member.status}")

    except Exception as e:
        print(f"Ошибка проверки подписки: {e}")
        await call.message.answer(f"Не могу проверить подписку! Ошибка: {e}")