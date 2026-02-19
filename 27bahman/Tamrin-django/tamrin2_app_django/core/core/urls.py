from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Dashboard.urls')),
    path('blog/', include('Blog.urls')),
    path('support/', include('Support.urls'))
]
