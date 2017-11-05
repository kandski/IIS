FROM python:3.6-alpine
COPY requirements.txt /code/

RUN apk add --update --no-cache mariadb-client-libs \
	&& apk add --no-cache --virtual .build-deps \
		mariadb-dev \
		gcc \
		musl-dev \
	&& pip install mysqlclient\
	&& apk del .build-deps
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip install psycopg2

ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code/
