from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message
from create_bot import bot

router = Router()



@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}! 👋\n")