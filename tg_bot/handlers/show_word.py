from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

from tg_bot.keyboards.all_replykeyboard import Reply_board
from tg_bot.models.connect_db import Word


async def show_w(message: Message):
    await message.answer("Хотите указать количество слов?", reply_markup=Reply_board(one_time_keyboard=True).replay_keyboard("Yes", "Show_all"))





async def answer_collide(message: Message):
        shows = Word().select_words(all=True)
        for show in shows:
            await message.answer(f"{show[0]} - {show[1]}")



def register_show(dp: Dispatcher):
    dp.register_message_handler(show_w, commands=["show_word"])
    dp.register_message_handler(answer_collide, text="Show_all")
    # dp.register_callback_query_handler(answer_collide)