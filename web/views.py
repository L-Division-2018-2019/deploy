from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from web.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # context = {
    #     "variable":"this is sent"
    # }
   
    return render(request,'index.html')
    # return HttpResponse("This is homepage")

def about(request):
    # return HttpResponse("This is aboutpage")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is services page")
    return render(request,'services.html')

def contact(request):
    # return HttpResponse("This is contact page")

    if request.method =="POST":
        jobrole = request.POST.get('jobrole')
        quali = request.POST.get('quali')
        speci = request.POST.get('speci')
        loca = request.POST.get('loca')
        sal = request.POST['sal']
        contact = Contact(jobrole=jobrole,quali=quali,speci=speci,loca=loca,sal=sal, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request,'contact.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        #check user has entered correct credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/admin")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def job1(request):
    # return HttpResponse("This is services page")
    return render(request,'job1.html')

def job2(request):
    # return HttpResponse("This is services page")
    return render(request,'job2.html')

def job3(request):
    # return HttpResponse("This is services page")
    return render(request,'job3.html')
