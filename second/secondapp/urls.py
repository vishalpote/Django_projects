from django.contrib import admin
from django.urls import path
from secondapp import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('thanku/', views.thanku,name='thanku'),
    path('submitform/', views.submitform,name='submitform'),
    path('details/<detid>', views.details,name='details'),
    # path('submitform/', views.submitform,name='submitform'),
]
