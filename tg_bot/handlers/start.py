from aiogram import Dispatcher
from aiogram.types import Message
from tg_bot.models.connect_db import NewUser
from tg_bot.keyboards.all_replykeyboard import Reply_board


async def user_start(message: Message):
    user_id = int(message.from_user.id)
    username = str(message.from_user.username)
    NewUser().add_user(user_id=user_id, username=username)
    await message.answer(f"Hello, {message.from_user.first_name}!",
                         reply_markup=Reply_board(one_time_keyboard=True).replay_keyboard("/help"))


def register_start(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"])






