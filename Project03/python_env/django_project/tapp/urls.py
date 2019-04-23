from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('sessionincr/', views.sessionIncrease , name = 'tapp-sessionIncrease'),
    path('sessionget/', views.sessionGet , name 'tapp-sessionGet'),
    path('useradd/', views.userAdd , name = 'tapp-userAdd'),
    path('loginuser/', views.loggedUser , name = 'tapp-loggedUser'),
    path('usersinfo/', views.usersInfo , name = 'tapp-usersInfo'),
    path('login/', login, {'template_name': 'tapp/login.html'}),
]
