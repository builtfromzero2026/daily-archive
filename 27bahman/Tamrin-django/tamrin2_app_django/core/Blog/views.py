from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    return HttpResponse("welcome to blog")

def cr_pst(request):
    return HttpResponse("publish a post")