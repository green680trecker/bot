from aiogram import Dispatcher
from aiogram.types import Message



async def user_id(message: Message):
    await message.answer(text=message.from_user.id)
    # await message.answer(text=message.chat.id)
    # await bot.send_message(chat_id=message.chat.id, text=f"Your id: {message.from_user.id}")


def register_user_id(dp: Dispatcher):
    dp.register_message_handler(user_id, commands=["id"], state="*")

