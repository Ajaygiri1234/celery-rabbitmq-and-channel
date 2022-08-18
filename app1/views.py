from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add
import time
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here
def index(request):
    print("okay")
    # add.delay(c=2)
    schedule, _ = CrontabSchedule.objects.get_or_create(
    minute='*',
    hour='*',
    day_of_week='*',
    day_of_month='*',
    month_of_year='*',
    
)
    c=["1","ajay"]
    PeriodicTask.objects.create(
        crontab=schedule,
        name='second33_task',
        task='app1.tasks.add',
        # args=json.dumps([c])
        kwargs=json.dumps({'c':c})
        # one_off= False one_off = True for single time run
    )
    print("============================================================")
    qs = PeriodicTask.objects.get(name='second_task')
    qs_json = serializers.serialize('json', [qs])
    print(qs_json)
    
    
    
    return HttpResponse("ajay")



def chat(request):
    return render(request,'app1/index.html')