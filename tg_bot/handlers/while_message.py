from aiogram import Dispatcher
from aiogram.types import Message
from datetime import datetime
from time import sleep
async def remind(message: Message):
    await message.answer("Successful start:)")
    await message.answer_animation(animation="CAACAgIAAxkBAAEJOYVkfsiDTsQiIz-oSOzdftpTadWOLwACFx0AAq40oEqPBtTPCfd00y8E")
    count = 0
    while True:
        x = str(datetime.now())
        if x[11:13] >= str(13) and count == 0:
            count += 1
            await message.answer("It's time to eat")
            await message.answer_animation(animation="CAACAgIAAxkBAAEJOYlkfsl-6yxBjlfLj7XInA0ayoF5wQAC2h4AAjozoEppFTmjmR9siC8E")
        elif x[11:13] >= str(15):
            await message.answer("It's time to study")
            await message.answer_animation(animation="CAACAgIAAxkBAAEJOYtkfsnoNwsfoljy0DbglpmXjTnVzgAC9hwAAvK66Et76XL_ZIVRBi8E")
            break
        sleep(60 * 10)


def register_remind(dp: Dispatcher):
    dp.register_message_handler(remind, state="*", is_admin=True)

# print(x[11:16])
# print(x[11:13])