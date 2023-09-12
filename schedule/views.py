from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Schedule
import json


# Create your views here.
def index(request):
    return HttpResponse("Olá, Você está quase fazendo um agendamento...")


def schedules(request):
    schedules = Schedule.objects.all()

    response = []
    for s in schedules:
        schedule = {
            'owner': s.owner,
            'guest': s.guest,
            'service': s.service,
            'schedule': str(s.schedule),
        }

        response.append(schedule)

    return HttpResponse(json.dumps(response))
