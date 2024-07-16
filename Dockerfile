FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y  \
    netcat-traditional
RUN pip install poetry

WORKDIR /usr/src
COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
