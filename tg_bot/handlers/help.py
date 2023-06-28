from aiogram import Dispatcher
from aiogram.types import Message


async def user_help(message: Message):
    Help_command = """
    /new_words
    /song
    /test
    /coffee
    /show_word
    /new_word
    /You_know
    /message_is_in_channel
    /send_photo_to_channel
    """
    await message.answer(f"All commands:\n {Help_command}")


def register_help(dp: Dispatcher):
    dp.register_message_handler(user_help, commands=["help"], state="*")