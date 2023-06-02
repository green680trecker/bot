from aiogram import Dispatcher
from aiogram.types import Message

from tg_bot.keyboards.all_replykeyboard import Reply_board


async def user_start(message: Message):

    await message.answer(f"Hello, {message.from_user.first_name}!", reply_markup=Reply_board.replay_keyboard("/help", "/id"))




def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")





