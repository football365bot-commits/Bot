from aiogram import Router, types
from start.sub_link import sub_link_buttons
from aiogram.types import Message 
from start.sub_check_message import IsSubscribedMessage


router = Router()

@router.message(IsSubscribedMessage())
async def handle_unsubscribed(message: types.Message):
    await message.answer(
        "❌ Подпишитесь на канал, чтобы продолжить!",
        reply_markup=sub_link_buttons
    )