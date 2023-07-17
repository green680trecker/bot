from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tg_bot.keyboards.all_inlinekeyboard import Inner_board


async def test_inline1(message: Message):
    await message.answer("Do you want buy something new?", reply_markup=Inner_board().start_inlineboar("Yes", "No"))


async def test_inline2(call: CallbackQuery):
    if call.data == "Yes":
        await call.bot.edit_message_text(chat_id=call.from_user.id,
                                         message_id=call.message.message_id,
                                         text="Choose",
                                         reply_markup=Inner_board().start_inlineboar("current", "available"))
    elif call.data =="No":
        await call.bot.edit_message_text(chat_id=call.from_user.id,
                                         message_id=call.message.message_id,
                                         text="Good, what do you want?",
                                         reply_markup=Inner_board().start_inlineboar("Well"))
    elif call.data == "current":
        await call.answer(text="текущий")

    elif call.data == "available":
        await call.answer(text="доступный")


def register_inline_button(dp: Dispatcher):
    # dic_t = {"one": "fitst", "two": "second"}
    dp.register_message_handler(test_inline1, commands="bt")
    dp.register_callback_query_handler(test_inline2)

