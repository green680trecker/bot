from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from tg_bot.misc.states import Forward_for_admin_photo


async def forward_photo1(message: Message):
    await message.answer("Started\nEnter photo")
    await Forward_for_admin_photo.f_d_p1.set()

async def forward_photo2(message: Message, state: FSMContext):
    await message.answer("Good, Enter caption to photo for channel")
    photo = message.photo[0]["file_id"]

    await state.update_data(photo=photo)
    await Forward_for_admin_photo.f_d_p2.set()

async def forward_photo3(message: Message, state: FSMContext):
    # data = await state.get_data()
    # answer1 = data.get("answer1")
    state_photo = await state.get_data()
    photo = state_photo.get("photo")
    caption = message.text
    await message.bot.send_photo(chat_id=-1001940914915, caption=caption, photo=photo)
    await state.finish()



def register_forward_photo(dp: Dispatcher):
    dp.register_message_handler(forward_photo1, commands=['send_photo_to_channel'])
    dp.register_message_handler(forward_photo2, state=Forward_for_admin_photo.f_d_p1, content_types=['photo'])
    dp.register_message_handler(forward_photo3, state=Forward_for_admin_photo.f_d_p2)