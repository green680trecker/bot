from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    text = """
Welcome to the family my Lord

<b>channel commands</b>:
    /send_photo_to_channel
    /message_is_in_channel
<b>admin commands</b>:
    /delete_user
    /add_admin
    /delete_admin
<b>Other commands</b>:
    /lesson 
    /new_word
    /ii
    /image_ii
    /speech_to_text"""
    await message.answer(text=text)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], is_admin=True)