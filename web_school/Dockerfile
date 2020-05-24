FROM python:3

ENV PYTHONUNBUFFERED 1

MAINTAINER vasiazozulia

RUN mkdir /webschool_backend
WORKDIR /webschool_backend
COPY . /webschool_backend/
RUN pip install -r req.txt
RUN python manage.py runserver 0.0.0.0:8000
