from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tg_bot.models.connect_db import AdminQuery
from tg_bot.misc.states import Del_admin_state


async def del_admin1(message: Message):
    await message.answer("Enter user id")
    await Del_admin_state.st.set()


async def del_admin2(message: Message, state: FSMContext):
    user_id = message.text
    AdminQuery().delete_admin(user_id)
    await message.answer("Admin deleted")
    await state.finish()


def register_del_admin(dp: Dispatcher):
    dp.register_message_handler(del_admin1, commands="delete_admin")
    dp.register_message_handler(del_admin2, state=Del_admin_state.st)
