from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    # path('product/<product_id>',views.item),
    path('product/<product_id2>', views.item2),
]
