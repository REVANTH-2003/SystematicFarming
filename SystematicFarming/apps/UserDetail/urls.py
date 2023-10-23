from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("login/", Loginview.as_view(), name="login"),
    path("home/", home , name="home"),
]

