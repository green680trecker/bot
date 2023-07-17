from aiogram import Dispatcher
from aiogram.types import Message


async def user_help(message: Message):
    Help_command = """
    /song
    /test
    /coffee
    /show_word
    /You_know
    /ii
    /image_ii
    """
    await message.answer(f"<b>All commands:</b>\n {Help_command}")


def register_help(dp: Dispatcher):
    dp.register_message_handler(user_help, commands=["help"])