from aiogram import Dispatcher
from aiogram.types import Message

from tg_bot.keyboards.all_inlinekeyboard import Inner_board


async def bot_echo(message: Message):
    text = [
        "Неверная команда"
    ]

    # await message.answer('\n'.join(text))
    x = Inner_board("/help")
    await message.answer("Неверная команда")
                         # , reply_markup=x.inner_keyboard())


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, state="*")
