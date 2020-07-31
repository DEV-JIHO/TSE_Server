FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install --no-cache-dir fastapi
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY ./app /app