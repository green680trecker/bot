from aiogram import Dispatcher
from aiogram.types import Message
import time


async def song(message: Message):
    x = ['Одолжи', 'мне', 'зима', 'одолжи', 'чистоты', 'и', 'отдоновения', 'белоснежных', 'снегов', 'безо', 'лжы', 'Я',
         'прошу', 'тебя', 'об', 'одолжении']

    for i in x:
        time.sleep(0.5)
        if i == 'Я':
            time.sleep(0.7)
        elif i == 'белоснежных':
            time.sleep(0.6)
        await message.answer(text=i)


def register_song(dp: Dispatcher):
    dp.register_message_handler(song, commands=["song"], state="*")