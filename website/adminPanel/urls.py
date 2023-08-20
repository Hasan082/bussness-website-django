from django.urls import path
from adminPanel import views

urlpatterns = [
    path('dashboard', views.index, name="dashboard"),
    path('register', views.reg_user, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
]
