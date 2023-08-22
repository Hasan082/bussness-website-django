from django.urls import path
from adminPanel import views
from adminPanel.allviews import homeviews


urlpatterns = [
    path('dashboard', views.index, name="dashboard"),
    path('register', views.reg_user, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('about-add', views.about_add, name="aboutadd"),
    path('about-show', views.about_show, name="aboutshow"),
    path('about-edit/<int:id>/edit', views.aboutedit, name='aboutedit'),
    path('about-update/<int:id>/', views.aboutupdate, name='aboutupdate'),
    path('about-delete/<int:id>/delete', views.about_delete, name='about_delete'),
    path('speaker/', homeviews.homespeaker, name='homespeaker' ),
]
