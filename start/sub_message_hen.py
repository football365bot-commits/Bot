from aiogram import Router, types
from start.sub_link import sub_link_buttons

router = Router()

@router.message()
async def handle_unsubscribed(message: types.Message):
    await message.answer(
        "❌ Подпишитесь на канал, чтобы продолжить!",
        reply_markup=sub_link_buttons
    )