from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tg_bot.models.connect_db import AdminQuery
from tg_bot.misc.states import Add_state

async def add_admin1(message: Message):
    await message.answer("Enter user id")
    await Add_state.st.set()


async def add_admin2(message: Message, state: FSMContext):
    user_id = message.text
    AdminQuery(user_id).add_admin()
    await message.answer("Admin added")
    await state.finish()


def register_add_admin(dp: Dispatcher):
    dp.register_message_handler(add_admin1, commands="add_admin")
    dp.register_message_handler(add_admin2, state=Add_state.st)

