from django.urls import path
from . import views

urlpatterns = [
   path('archive/',views.archive),
   path('new-ticket/',views.new_ticket),
]