# our base image
FROM python:3.8

ARG DEBIAN_FRONTEND="noninteractive"

COPY . .

RUN pip install -r ./requirements.txt

CMD ["python3", "./run_gen.py"]
