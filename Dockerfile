# our base image
FROM python:3.8
COPY src/requirements.txt .

RUN apt-get -y update && apt-get -y upgrade

COPY ./src ./src

RUN ["python3", "./src/app.py"]