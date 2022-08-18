from celery import shared_task
import time
from .models import Book
from celerytest.celery import app
from django_celery_beat.models import CrontabSchedule, PeriodicTask

@shared_task
def add(c):

    a=Book()
    a.title=c[1]
    a.save()
    

    print("okay")
    print("hello")
    return 1
    
    