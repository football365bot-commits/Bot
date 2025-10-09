from aiogram import Router, types
from aiogram.filters import CommandStart
from create_bot import bot, CHANNEL_ID
from start.sub_link import sub_link_buttons
from language.lang_keyboard import language_keyboard

router = Router()

# -----------------------
# Функция проверки подписки
# -----------------------
async def check_subscription(user_id: int) -> bool:
    """
    Проверяет, подписан ли пользователь на канал.
    Возвращает True, если подписан, иначе False.
    """
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return member.status not in ["left", "kicked"]
    except Exception as e:
        print(f"Ошибка проверки подписки для пользователя {user_id}: {e}")
        return False

# -----------------------
# Обработчик команды /start
# -----------------------
@router.message(CommandStart())
async def start_command(message: types.Message):
    is_subscribed = await check_subscription(message.from_user.id)

    if is_subscribed:
        text = f"Добро пожаловать, {message.from_user.full_name}! 👋\nВы уже подписаны ✅\nВыберите язык:"
        keyboard = language_keyboard
    else:
        text = f"Добро пожаловать, {message.from_user.full_name}! 👋\nПроверьте подписку, чтобы продолжить 👇"
        keyboard = sub_link_buttons

    try:
        await message.answer(text, reply_markup=keyboard)
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)