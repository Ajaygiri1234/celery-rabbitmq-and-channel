FROM python:3 as python-base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


FROM python-base as celery
# install chromedriver
RUN apt-get install -yqq unzip

# Set work directory
COPY . /code/
WORKDIR /code

# Install dependencies

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
# RUN pip3 install celery
# Run pip3 install django-celery-beat
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py migrate django_celery_beat
# Copy Project


FROM python-base as web
run ls
COPY . ./code/
WORKDIR ./code
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
# RUN virtualenv venv
# RUN venv/Scripts/activate
# Run Pip install django
 RUN pip3 install celery
 Run pip3 install django_celery_beat
 RUN python manage.py makemigrations
 RUN python manage.py migrate
 RUN python manage.py migrate django_celery_beat
# RUn pip install rabbitmq




CMD ["python", "manage.py","runserver","0.0.0.0:8000"]