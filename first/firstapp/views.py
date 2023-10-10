from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def service(request):
    return render(request,'pages/service.html')

def login(request):
    return render(request,'pages/login.html')

def logout(request):
    return render(request,'pages/logout.html')