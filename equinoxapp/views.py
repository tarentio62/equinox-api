from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse("hello word")

def detail(request, record_id):
    return HttpResponse("Tu affiche le record %s." % record_id)

def steps(request, record_id):
    response = "tu affiche les steps du record %s."
    return HttpResponse(response % record_id)

def createStep(request, record_id):
    return HttpResponse("tu creer une step pour le record %s." % record_id)

# Create your views here.
