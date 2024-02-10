FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY req_django.txt /code/
RUN pip install --user -r req_django.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:9000
