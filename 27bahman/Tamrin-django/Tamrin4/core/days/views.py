from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


dict = {
    '0':"saturday",
    '1':"sunday",
    '2':"monday",
    '3':"tuesday",
    '4':"wednesday",
    '5':"thursday",
    '6':"Friday",
}

def home(request):
    return HttpResponse("Hi this is for test with weekdays...")

def index(request, numberday):
    if numberday in dict:
        return HttpResponse(dict[numberday])
    else:
        return HttpResponseNotFound("Item not found...plz enter a true number!")