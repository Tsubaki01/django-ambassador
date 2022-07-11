FROM python:3.9.13

WORKDIR /app

COPY requirements.txt ${PWD}

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000