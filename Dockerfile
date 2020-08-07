FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Jeong <wjdwlgh_34@naver.com>"

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir fastapi
RUN pip install -r requirements.txt

COPY ./app /app