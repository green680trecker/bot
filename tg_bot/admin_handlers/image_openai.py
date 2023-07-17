from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

import openai
from tg_bot.misc.states import Image_ii
from tg_bot.config import load_config

async def func1(message: Message):
    await message.answer("describe the picture")
    await Image_ii.st.set()

async def func2(message: Message, state: FSMContext):
    openai.api_key = load_config(".env").api_token
    response = openai.Image.create(
        prompt="{}".format(message.text),
        n=2,
        size="1024x1024")
    await message.bot.send_photo(chat_id=message.chat.id, photo=response["data"][0]["url"])
    await state.finish()

def register_image_ii(dp: Dispatcher):
    dp.register_message_handler(func1, commands="image_ii")
    dp.register_message_handler(func2, state=Image_ii.st)