
from django.contrib import admin
from django.urls import path, include
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hzadmin/',include('hzadmin.urls')),
    path('cainiao/',include('cainiao.urls')),
]
        