from aiogram import types, Router, F

router = Router()

@router.callback_query(F.data == "sub_done")
async def sub_done(call: types.CallbackQuery):
    await call.message.edit_text("Вы подписались 🤝")