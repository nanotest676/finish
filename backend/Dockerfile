FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

COPY . /code/

CMD ["gunicorn", "your_app.wsgi:application", "--bind", "0.0.0.0:8000"]