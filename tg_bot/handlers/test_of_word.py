from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tg_bot.misc.states import English_test
from random import randrange

from tg_bot.models.connect_db import Base

number1 = randrange(1, 15)
number2 = randrange(1, 15)
req_base1 = Base()
req_base2 = Base()
word1 = req_base1.select_word_id(number1)
word2 = req_base2.select_word_id(number2)

async def test_word1(message: Message):
    global word1
    text1 = "Ты начал тест английских слов:"
    await message.answer(text1)

    text2 = f"Переведите это слово: {word1[0]}"
    await message.answer(text2)

    await English_test.eg1.set()


async def test_word2(message: Message, state: FSMContext):
    global word1, word2

    data = str(message.text)
    data_st = message.text
    # print(type(data))
    # print(data)
    if word1[1] == data:
        await message.answer("Чела бью мудрец, правильно!")
    else:
        await message.answer("Не правильно!")
    await state.update_data(answer1=data_st)

    text = f"Второе слово {word2[0]}"
    await message.answer(text)

    await English_test.eg2.set()

async def test_word3(message: Message, state: FSMContext):
    global word2, word1
    data2 = str(message.text)

    if word2[1] == data2:
        await message.answer("Чела бью мудрец, правильно!")
        num = True
    else:
        num = False
        await message.answer("Не правильно!")
    # st_data = await state.get_data()
    # answer_first = st_data.get("answer1")
    #
    # if num is True and answer_first == word1[1]:
    #     await message.answer("Ты ответил на 100%, поздравляю!")
    # elif num is True or answer_first == word1[1]:
    #     await message.answer("Ты ответил на 50%, есть куда расти)")
    # else:
    #     await message.answer("Ты ответил на 0%, попробуй еще раз и удачи!")
    await message.answer("Тест окончен")
    await state.finish()

def register_test_words(dp: Dispatcher):
    dp.register_message_handler(test_word1, commands=["You_know"], state=None)
    dp.register_message_handler(test_word2, state=English_test.eg1)
    dp.register_message_handler(test_word3, state=English_test.eg2)