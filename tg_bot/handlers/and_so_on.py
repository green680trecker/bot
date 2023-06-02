import time

from aiogram import Dispatcher
from aiogram.types import Message


async def new_words(message: Message):
    words = ['Hide - скрывать', "tool - инструменты", "view - вид", "promise - обещать", "purpose - цель",
             "heaven - небеса", "solve - решать", "hold - держать", "favorite - любимый",
             "soldier - солдат", "follow - следовать"]
    for i in words:
        time.sleep(0.5)
        await message.answer(text=i, parse_mode="HTML")


def register_words(dp: Dispatcher):
    dp.register_message_handler(new_words, commands=["new_words"], state="*")
