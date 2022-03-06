# our base image
FROM python:3.8

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install git

COPY ./src ./src

RUN ["python3", "./src/init.py"]