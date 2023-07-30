
# print(["audio"]["file_name"])

#
# import openai
# from tg_bot.config import load_config
#
# openai.api_key = openai.api_key = load_config(".env").api_token
#
# audio_file = open("/home/trecker/PycharmProjects/Stuck/Imagine-Dragons_-_Bad-Liar.mp3.mp3", "rb")
#
# transcript = openai.Audio.transcribe("whisper-1", audio_file)
# print(transcript["text"])

# FROM rocker/r-ver:4.2.1
#
# RUN mkdir /home/bot
# RUN mkdir /home/bot/log
#
# ENV R_TELEGRAM_BOT_botname ТОКЕН_ВАШЕГО_БОТА
#
# COPY bot.R /home/bot/bot.R
#
# RUN R -e "install.packages(c('telegram.bot', 'stringr', 'future', 'promises','fastmap', 'lgr'))"
#
# CMD cd /home/bot \
#   &&  R -e "source('/home/bot/bot.R')"