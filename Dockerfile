FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./bot.py" ]
#FROM ubuntu:22.04
#COPY . /app
#RUN make /app
#CMD python /app/app.py