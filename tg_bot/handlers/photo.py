from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tg_bot.misc.states import St_photo


async def user_photo1(message: Message):
    await message.answer(text="I need photo")
    await St_photo.ph.set()

async def user_photo2(message: Message, state: FSMContext):
    x = message.photo
    print(message.photo)
    print(x[0]["file_id"])
    await state.finish()


def register_photo(dp: Dispatcher):
    dp.register_message_handler(user_photo1, commands=["photo"])
    dp.register_message_handler(user_photo2, state=St_photo.ph, content_types=['photo'])
    # , content_types = ['photo']