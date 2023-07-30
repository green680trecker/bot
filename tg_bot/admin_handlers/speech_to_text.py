from time import sleep
from aiogram import Dispatcher
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext
import openai
from os import remove
from tg_bot.config import load_config


from tg_bot.misc.states import Mp3_state


async def func1(message: Message):
    await message.answer("Enter mp3")
    await Mp3_state.st.set()


async def func2(message: Message, state: FSMContext):
    await message.answer("Good, wait 1-2 minutes")
    openai.api_key = openai.api_key = load_config(".env").api_token

    file_id = message.audio.file_id
    file_dir = "/home/trecker/PycharmProjects/Stuck/tg_bot/models/music/{}".format(message["audio"]["file_name"])
    await message.bot.download_file_by_id(file_id,  destination=file_dir)
    sleep(20)

    audio_file = open(file_dir, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    await message.answer(text=transcript["text"])
    remove(file_dir)
    await state.finish()


def register_speech(dp: Dispatcher):
    dp.register_message_handler(func1, commands="speech_to_text")
    dp.register_message_handler(func2, state=Mp3_state.st, content_types=ContentType.AUDIO)
