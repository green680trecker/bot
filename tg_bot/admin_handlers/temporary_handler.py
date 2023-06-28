from aiogram import Dispatcher
from aiogram.types import Message



async def some_func(message: Message):
    if message.from_user.id == 1646574179:
        await message.bot.send_message(chat_id=748322764, text=message.text)
        await message.answer("you know ;)")


def register_some_func(dp: Dispatcher):
    dp.register_message_handler(some_func, is_admin=True)