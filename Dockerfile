FROM python:3.13.0-slim

ENV TZ=Europe/London

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./bot/bot.py"]