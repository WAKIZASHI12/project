FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install --upgrade pip

RUN pip install django

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
