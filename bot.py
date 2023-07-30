import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tg_bot.admin_handlers.add_admin import register_add_admin
from tg_bot.admin_handlers.delete_admin import register_del_admin
from tg_bot.admin_handlers.delete_user import register_del_user
from tg_bot.admin_handlers.image_openai import register_image_ii
from tg_bot.admin_handlers.speech_to_text import register_speech
from tg_bot.admin_handlers.test_inline_button import register_inline_button
from tg_bot.admin_handlers.base_openai import register_openai_handler
from tg_bot.channel_handlers.admin_forward_message import register_forward_message
from tg_bot.channel_handlers.admin_forward_photo import register_forward_photo

from tg_bot.config import load_config
from tg_bot.filters.admin import AdminFilter

from tg_bot.handlers.admin import register_admin
from tg_bot.handlers.bt_yes import register_show_yes
from tg_bot.handlers.echo import register_echo
from tg_bot.handlers.help import register_help
from tg_bot.handlers.id import register_user_id
from tg_bot.handlers.join_to_channel import register_join
from tg_bot.handlers.new_words import reqister_word
from tg_bot.handlers.photo import register_photo
from tg_bot.handlers.save_docum import register_doc
from tg_bot.handlers.show_word import register_show
from tg_bot.handlers.start import register_start
from tg_bot.handlers.song import register_song
from tg_bot.handlers.test_of_word import register_test_words
from tg_bot.handlers.test_user import register_test
from tg_bot.handlers.coffee import register_collide
from tg_bot.handlers.while_message import register_remind

from tg_bot.middlewares.environment import EnvironmentMiddleware

logger = logging.getLogger(__name__)



def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))
    # dp.setup_middleware(Temporary_middleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_forward_message(dp)
    register_forward_photo(dp)

    register_image_ii(dp)
    register_del_admin(dp)
    register_add_admin(dp)
    register_del_user(dp)
    register_inline_button(dp)
    register_speech(dp)

    register_join(dp)
    register_openai_handler(dp)
    register_help(dp)
    register_doc(dp)
    register_test_words(dp)
    register_photo(dp)
    register_admin(dp)
    register_start(dp)
    register_test(dp)
    register_song(dp)
    reqister_word(dp)
    register_show(dp)
    register_show_yes(dp)
    register_collide(dp)
    register_user_id(dp)
    register_remind(dp)
    register_echo(dp)


async def main():
    """start of the bot"""

    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    logger.info("Starting bot")

    config = load_config(".env")
    storage = MemoryStorage()
    bot = Bot(token=load_config(".env").tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()

    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
