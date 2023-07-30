FROM python:3

WORKDIR /app

RUN mkdir /home/bot
RUN mkdir /home/bot/log
ENV ?
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./bot.py" ]

