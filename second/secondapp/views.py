from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from secondapp.models import ContactApp
from secondoneapp.models import secondoneappModules
def home(request):
    return render(request,'pages/home.html')

def submitform(request):
        data={'total':'','per':''}
        if request.method=='POST':
            if request.POST.get('num5')=="":
                 return render (request,'pages/submitform.html',{'error':True})
            else:
                # s1=eval(request.POST.get('num1'))
                # s2=eval(request.POST.get('num2'))
                # s3=eval(request.POST.get('num3'))
                # s4=eval(request.POST.get('num4'))
                s5=eval(request.POST.get('num5'))

                # total=s1+s2+s3+s4+s5
                # print(total)
                # per=(total/500)*100
           
            return render (request,'pages/submitform.html',{'total':'','per':''})
        # return HttpResponse(request)

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    contactData=ContactApp.objects.all().order_by('name')[:]
    if request.method=="GET":
         x=request.GET.get('searchfilter')
         if x!=None:
            #    contactData=ContactApp.objects.filter(name=x)
               contactData=ContactApp.objects.filter(name__icontains=x)
              
    secondappData=secondoneappModules.objects.all()
    data={
           'contactData':contactData,
           'secondappData':secondappData,
      }
    return render(request,'pages/contact.html',data)
def details(request,detid):
     details=secondoneappModules.objects.get(id=detid)
     return render(request,'pages/details.html',{'details':details})
def login(request):
    data={}
    try:
            email=request.POST['email']
            password=request.POST['password']
            print("Email:"+ email)
            print("Password:" +password)

            data={
                 'email':email,
                 'passwoed':password
            }
            url='/thanku/?data={}'.format(data)
            return redirect(url)
    except:
         pass
    return render(request,'pages/login.html',data)

def signup(request):
    return render(request,'pages/signup.html')

def thanku(request):
    if request.method=="GET":
         data=request.GET.get('data')
    return render(request,'pages/thanku.html',{'data':data})