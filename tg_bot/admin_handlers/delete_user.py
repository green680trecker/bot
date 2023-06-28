from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tg_bot.models.connect_db import AdminQuery
from tg_bot.misc.states import Del_user_state


async def del_user1(message: Message):
    await message.answer("Enter user id")
    await Del_user_state.st.set()


async def del_user2(message: Message, state: FSMContext):
    user_id = message.text
    AdminQuery().delete_user(user_id)
    await message.answer("User deleted")
    await state.finish()


def register_del_user(dp: Dispatcher):
    dp.register_message_handler(del_user1, commands="delete_user")
    dp.register_message_handler(del_user2, state=Del_user_state.st)