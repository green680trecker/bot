from aiogram import Dispatcher
from aiogram.types import Message
from tg_bot.keyboards.all_replykeyboard import ReplyKeyboardRemove


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
    await message.answer(f"All commands:\n {Help_command}", reply_markup=ReplyKeyboardRemove())


def register_help(dp: Dispatcher):
    dp.register_message_handler(user_help, commands=["help"], state="*")

# <ol>
#         <li>/start</li>
#         <li>/new_words</li>
#         /<li>song</li>
#         <li>/test</li>
#         <li>/coffee</li>
#         <li>/show_word</li>
#         <li>/new_word</li>
#         <li>/You_know</li>
# </ol>