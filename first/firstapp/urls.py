from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
