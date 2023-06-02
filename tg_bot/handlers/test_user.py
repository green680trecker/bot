from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tg_bot.misc.states import Brain_test
async def enter_test(message: Message):
    await message.answer("Вы начали тестирование:\n"
                         "Вопрос №1.\n"
                         f"Представьте, что есть два племени на Марсе: племя Лжи и племя Истины. Марсиане из племени Лжи всегда врут, а уроженцы племени Истины всегда говорят правду. И вот вы встречаете троих марсиан и спрашиваете у первого: «К какому племени ты принадлежишь?» Он отвечает что-то на своем языке, и вы ничего не поняли. Второй странник говорит, что первый сказал,"
                         f" что он принадлежит к племени Лжи. Третий говорит, что второй человек лжет. К какому племени принадлежит третий человек?")

    await Brain_test.q1.set()


async def answer_q1(message: Message, state: FSMContext):
    answer = message.text

    # async with state.proxy() as data:
    #     data["answer1"] = answer
    await state.update_data(answer1=answer)
    text = [
        "Вопрос №2",
        "Один человек, который знал два числа, рассказал сумму этих чисел человеку S и их произведение человеку P.После чего между S и P случился следующий диалог:\n",
        "S: Я не знаю, что это за числа.",
        "P: Я также не знаю, что это за числа.",
        "S: Теперь я знаю, что это за числа.",
        "Р: Теперь я тоже знаю, что это за числа."
    ]


    await message.answer("\n".join(text))

    await Brain_test.q2.set()


async def answer_q2(message: Message, state: FSMContext):
    data = await state.get_data()

    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Благодарю за ваши ответы")
    await message.answer(f"Ваш ответ №1: {answer1}")
    await message.answer(f"Ваш ответ №2: {answer2}")

    await message.answer("Ответ на вопрос №1:\n"
                         "К племени Истины. Предположим, первый человек из племени Истины,\n"
                         " тогда он сказал, что он из племени Истины, и в этом случае второй человек лжет.\n"
                         " Если предположить, что первый человек из племени Лжи, то как лжец, он должен был сказать, что он из племени Истины, то есть и в этом случае второй – лжет.\n"
                         " Таким образом в любом случае третий – из племени Истины.")

    await message.answer("Ответ на вопрос №2:\n"
                         "Это числа 2 и 2.\n"
                         "S досталось число 4, что означает 1 + 3 или 2 + 2. Так вот почему он не был уверен в числах.\n"
                         "P также досталось 4, произведение 1 * 4 и 2 * 2.")
    await state.finish()


def register_test(dp: Dispatcher):
    dp.register_message_handler(enter_test, commands=["test"], state=None)
    dp.register_message_handler(answer_q1, state=Brain_test.q1)
    dp.register_message_handler(answer_q2, state=Brain_test.q2)







