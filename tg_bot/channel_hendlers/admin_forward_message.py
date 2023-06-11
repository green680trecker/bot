from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tg_bot.misc.states import Forward_for_admin_message
async def forward_message1(message: Message):
    await message.answer("Started\nEnter message for channel")
    await Forward_for_admin_message.f_d.set()



async def forward_message2(message: Message, state: FSMContext):
    message_id = message.message_id
    await message.bot.forward_message(chat_id=-1001940914915, from_chat_id=748322764, message_id=message_id, protect_content=True)
    await state.finish()



def register_forward_message(dp: Dispatcher):
    dp.register_message_handler(forward_message1, commands=['message_is_in_channel'])
    dp.register_message_handler(forward_message2, state=Forward_for_admin_message.f_d)