from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to Dashboard")    

def profile(request):
    return HttpResponse("Your Profile")