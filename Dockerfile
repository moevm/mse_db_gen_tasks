# our base image
FROM python:3.8

ARG DEBIAN_FRONTEND="noninteractive"

WORKDIR /src

COPY . .

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python3", "main.py"]
