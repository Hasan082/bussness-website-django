
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminPanel.urls')),
    path('', include('frontendApp.urls')),
]
