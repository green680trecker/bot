from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import CallbackQuery
from random import choice


from tg_bot.keyboards.all_inlinekeyboard import Inner_board

async def collide(message: Message):
    fade = ["https://i.insider.com/5a25b4ef3339b009268b45d3?width=700"]
    # x = Inner_board.inner_keyboard_data(text="touch me", url=choice(fade))
    # y = Inner_board.inner_keyboard_data(text="My Youtube", url="https://www.youtube.com/channel/UCcm00p5w8nPQ2INFv8waXJg")

    await message.answer_photo(photo=choice(fade), caption="I like it)", reply_markup=Inner_board.keyboard_coffee())

async def answer_collide(callback: CallbackQuery):
    if callback.data == "touch":
        await callback.answer("Its good")


def register_collide(dp: Dispatcher):
    dp.register_message_handler(collide, commands=["coffee"], state="*")
    dp.register_callback_query_handler(answer_collide)