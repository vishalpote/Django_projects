from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from mysqlapp.models import signupModel,loginModel
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def login(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        loguser=loginModel(name=name,password=password)
        loguser.save()
    return render(request,'pages/login.html')

def logout(request):
    return render(request,'pages/logout.html')

def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        signupmodel=signupModel(name=name, password=password, email=email)
        signupmodel.save()
    return render(request,'pages/signup.html')
    