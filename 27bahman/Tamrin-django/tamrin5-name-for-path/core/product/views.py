from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
int_dict = {
    1:"PS5",
    2:"Laptop",
    3:"Mobile",
}
text_dict = {
    "1st":1,
    "2nd":2,
    "3rd":3,
}

def index(request):
    return HttpResponse("welcome to my website.")

def int_item(request, product_id):
    if product_id in int_dict:
        return HttpResponse(int_dict[product_id])
    return HttpResponse("Item not found. ")

def text_item(request, product_id):
    if product_id in text_dict:
        return HttpResponseRedirect(reverse('product-int', args = [text_dict[product_id]]))
    return HttpResponse("Item not found.")