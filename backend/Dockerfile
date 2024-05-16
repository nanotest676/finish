FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
