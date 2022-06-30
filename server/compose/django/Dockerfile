FROM python:3.9.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
ADD requirements.txt    /app/
RUN pip install -r requirements.txt

RUN apt update -y
RUN apt install -y poppler-utils libgl1-mesa-glx libglib2.0-0 tesseract-ocr libtesseract-dev
