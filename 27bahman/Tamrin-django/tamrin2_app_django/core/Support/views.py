from django.shortcuts import render
from django.http import HttpResponse


def archive(request):
    return HttpResponse("All tickets")

def new_ticket(request):
    return HttpResponse("open a ticket")
