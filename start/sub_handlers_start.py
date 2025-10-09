from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message
from create_bot import bot
from start.sub_link import sub_link_buttons  # ← твоя клавиатура

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}! 👋\n"
        "Проверьте подписку, чтобы продолжить 👇",
        
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)

    if member.status != "left":
        await call.message.edit_text(
            "Спасибо за подписку!✅\nВыберите язык:",
            reply_markup=await kb.language_keyboard()
        )
    else:
        await call.message.edit_text(
            "❌ Подпишитесь на канал, чтобы продолжить!",
        reply_markup=sub_link_buttons  # ← используем твою клавиатуру
    )