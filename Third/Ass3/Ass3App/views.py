from django.shortcuts import render,redirect
from Ass3App.models import loginModel,registerModel
from django.contrib import auth,messages
# from django.contrib.auth.models import login,register
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def register(request):
    if request.method == 'POST':
        name=request.POST["name"]
        email=request.POST["email"]
        password=request.POST["password"]
        if registeruser.objects.filter(name=name).exists():
            return redirect('register')
        else:
            registeruser=registerModel(email=email,password=password,name=name)
            registeruser.save()
        return redirect('login')

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        loginuser=auth.authenticate(email=email,password=password)
        
        if loginuser is not None :
            auth.login(request, loginuser)
            return redirect('home')
        else :
            return redirect('login')
    else :
        return render(request,'pages/login.html')
        
        
    

def thanku(request):
    return render(request, 'pages/thanku.html')


    