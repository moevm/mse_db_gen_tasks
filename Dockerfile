# our base image
FROM python:3.8

RUN DEBIAN_FRONTEND="noninteractive"

RUN apt-get -y update && apt-get -y upgrade

COPY ./src ./src

RUN pip install -r src/requirements.txt

RUN ["python3", "./src/init.py"]