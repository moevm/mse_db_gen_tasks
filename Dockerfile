# our base image
FROM python:3.8

ARG DEBIAN_FRONTEND="noninteractive"

COPY ./src ./src

RUN pip install -r src/requirements.txt

RUN ["python3", "./src/init.py"]