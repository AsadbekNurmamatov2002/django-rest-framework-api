FROM python:3.8.13-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --upgrede pip && pip install -r requirements.txt
COPY . .

EXPOSE 8000