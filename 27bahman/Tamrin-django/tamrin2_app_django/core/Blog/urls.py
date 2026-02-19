from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog),
    path('create-post/',views.cr_pst)
]