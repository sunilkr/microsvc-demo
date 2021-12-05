FROM python:3-alpine

RUN apk update && apk add --no-cache sqlite python3-dev gcc g++ libc-dev libffi-dev

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]