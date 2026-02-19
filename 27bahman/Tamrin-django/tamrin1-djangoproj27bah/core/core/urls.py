#تمرین اول -> ایجاد ویو و وصل کردن ان به اینجا 
# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home),
#     path('about-us/',views.about_us),
#     path('contact-us/',views.contact_us),
#     path('services/',views.services),
#     path('faq/', views.faq),
#     path('terms/',views.terms),
#     path('status/',views.status_page)
# ]
#___________________________________________________
#تمرین دوم-> ساخت اپ 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    
]
