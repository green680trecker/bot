from aiogram import Dispatcher
from aiogram.types import Message, ChatInviteLink
from datetime import datetime, timedelta

async def func1(message: Message):
    print(message)
    expire_data = datetime.now() + timedelta(days=1)
    link = await message.bot.create_chat_invite_link(chat_id=-1001940914915, expire_date=expire_data, creates_join_request=True)
    await message.answer(text=link["invite_link"])




def register_join(dp: Dispatcher):
    dp.register_message_handler(func1, commands=["sos"])
    # dp.register_chat_join_request_handler(func1)





