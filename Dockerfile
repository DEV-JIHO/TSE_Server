FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Jeong <wjdwlgh_34@naver.com>"

RUN pip install --no-cache-dir fastapi
RUN pip install -r module/requirements.txt

COPY ./app /app