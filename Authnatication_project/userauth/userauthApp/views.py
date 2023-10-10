from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout;
from django.contrib import messages,auth
# Create your views here.
def home(request):
    return render(request,"pages/home.html")

def login(request):
    if request.method =="POST" :
        name = request.POST.get('name')
        password = request.POST.get('password')
        loginuser=auth.authenticate(request,username=name,password=password)
        if loginuser is not None:
            auth.login(request,loginuser)
            messages.success(request,"login successful")
            return redirect('home')
        else:
            messages.error(request,"Login failed")
            return redirect('login')
             
    return render(request,"pages/login.html")

def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        signuser=User.objects.create(username=name, email=email, password=password)
        signuser.save()
        return redirect('login')
    return render(request,"pages/signup.html")

def logout(request):
    return render(request,"pages/logout.html")