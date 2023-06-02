from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from tg_bot.misc.states import Add_word
from tg_bot.models.connect_db import Base


async def new_word(message: Message):
    await message.answer("Введите слова через пробел:\n word слово")
    await Add_word.firstandlast.set()


async def new_word2(message: Message, state: FSMContext):
    await message.answer("Thank you!")
    data = message.text
    res = data.split()
    bd = Base()
    bd.insert_words(res[0], res[1])
    await state.finish()

def reqister_word(dp: Dispatcher):
    dp.register_message_handler(new_word, commands=["new_word"], state=None)
    dp.register_message_handler(new_word2, state=Add_word.firstandlast)