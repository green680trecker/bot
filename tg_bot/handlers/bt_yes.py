from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tg_bot.keyboards.all_replykeyboard import ReplyKeyboardRemove
from tg_bot.misc.states import Show_word
from tg_bot.models.connect_db import Base


async def button_yes(message: Message):
    await message.answer("Введите число")
    await Show_word.st_show.set()

async def button_yes2(message: Message, state: FSMContext):
    data = await state.get_data()

    x = Base()
    shows = x.select_words(limit=data)
    for show in shows:
        await message.answer(f"{show[0]} - {show[1]}", reply_markup=ReplyKeyboardRemove())
    await state.finish()



def register_show_yes(dp: Dispatcher):
    dp.register_message_handler(button_yes, text="Yes", state=None)
    dp.register_message_handler(button_yes2, state=Show_word.st_show)

