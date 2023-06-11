from aiogram import Dispatcher
from aiogram.types import Message

async def start_channel(message: Message):
    await message.bot.send_message(chat_id=-1001940914915, text=f"Hi, {message.from_user.first_name} 🤝")

    # await message.answer(text=message.from_user.id)




def register_start_channel(dp: Dispatcher):
    dp.register_message_handler(start_channel, text="Hi")



