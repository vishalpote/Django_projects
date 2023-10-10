from django.contrib import admin
from django.urls import path
from Ass3App import views
urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login,name="home"),
    path("register/",views.register,name="home"),
    path("thanku/",views.thanku,name="home"),
]
