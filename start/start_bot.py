from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! 👋 Добро пожаловать!")