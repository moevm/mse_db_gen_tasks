# our base image
FROM python:3.8

ARG DEBIAN_FRONTEND="noninteractive"

RUN mkdir /src
RUN mkdir src/results

WORKDIR /src

COPY . .

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python3", "main.py"]
