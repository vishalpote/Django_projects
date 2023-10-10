from django.contrib import admin
from django.urls import path,include
from userauthApp import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
]