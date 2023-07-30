from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

import openai
from tg_bot.misc.states import Base_ii
from tg_bot.config import load_config


async def func1(message: Message):
    await message.answer("Good, write something to ii")
    await Base_ii.st.set()


async def func2(message: Message, state: FSMContext):
    openai.api_key = load_config(".env").api_token
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="{}".format(message.text),
        max_tokens=200,
        temperature=0
    )
    await message.answer("{}".format(response["choices"][0]["text"]))
    await state.finish()


def register_openai_handler(dp: Dispatcher):
    dp.register_message_handler(func1, commands="ii")
    dp.register_message_handler(func2, state=Base_ii.st)
