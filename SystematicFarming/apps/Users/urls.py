from django.urls import path 
from .views import *

urlpatterns = [
    path("login/", Loginview, name="login"),
    path("register/", register, name="register"),
    path("home/", home, name="home"),
]