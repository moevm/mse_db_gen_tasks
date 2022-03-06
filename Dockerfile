# our base image
FROM python:3.8

ARG DEBIAN_FRONTEND="noninteractive"

COPY . .

RUN pip install -r ./requirements.txt

RUN ["python3", "./main.py"]
