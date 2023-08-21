from django.urls import path
from frontendApp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name='about'),
]
