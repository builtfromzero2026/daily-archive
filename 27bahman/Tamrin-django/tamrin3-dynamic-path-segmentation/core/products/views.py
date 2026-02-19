from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

_dict = {
    "001": "PS5",
    "002": "Mobile",
    "003": "labtap"
}

def index(request):
    return HttpResponse("Hello this is a test")

# def item(request, product_id):
#     return HttpResponse(f"You enter : {product_id}")

# def item2(request, product_id2):
#     if product_id2 in _dict:
#         return HttpResponse(_dict[product_id2])
#     else:
#         return HttpResponse("item not found")       #اینکار کار قشنگی نیست بهتره که از نات فاند اچ تی تی پی ریسپانس استفاده کنیم 
    
    
    
def item2(request, product_id2):
    if product_id2 in _dict:
        return HttpResponse(_dict[product_id2])
    else:
        return HttpResponseNotFound("item not found")   #خروجیش با بالایی یکیه ولی استتوس کدشون باهم فرق داره و برای این 404 میاد