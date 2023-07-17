from aiogram import Dispatcher
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext

from tg_bot.misc.states import Doc_state

async def document1(message: Message):
    await message.answer("sent document")
    await Doc_state.st.set()

async def document2(message: Message, state: FSMContext):
    doc = message.document.file_id
    await message.answer("Yes")
    await message.bot.send_document(chat_id=-1001940914915, document=doc, caption="Yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees")
    await state.finish()

def register_doc(dp: Dispatcher):
    dp.register_message_handler(document1, commands="doc", is_admin=True)
    dp.register_message_handler(document2, state=Doc_state.st, content_types=ContentType.DOCUMENT)