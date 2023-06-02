from aiogram import Dispatcher
from aiogram.types import Message
from tg_bot.keyboards.all_replykeyboard import ReplyKeyboardRemove


async def user_help(message: Message):
    Help_command = """
    /start
    /new_words
    /song
    /test
    /coffee
    /show_word
    /new_word
    /You_know
    """
    await message.answer(f"All commands:\n {Help_command}", reply_markup=ReplyKeyboardRemove())


def register_help(dp: Dispatcher):
    dp.register_message_handler(user_help, commands=["help"], state="*")