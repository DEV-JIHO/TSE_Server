FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Jeong <wjdwlgh_34@naver.com>"

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir fastapi
RUN pip install -r /usr/src/app/requirements.txt
RUN rm -rf /root/.cache/pip
RUN pip install mysqlclient

COPY . /usr/src/app/