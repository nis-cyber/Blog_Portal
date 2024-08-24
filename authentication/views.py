from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
from django.contrib.auth import login as auth_login


# Create your views here.
from .froms import Authforms

def register(request):
    if request.method=="POST":
        forms=Authforms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('register')
       
                
    else:
        forms=Authforms()
    context={
        'forms':forms
    }
    return render(request,'home/register.html',context)




def login(request):
    if request.method =='POST':
        forms=AuthenticationForm(request,request.POST)
        if forms.is_valid():
            username =forms.cleaned_data.get('username')
            password =forms.cleaned_data.get('password')
            person = authenticate(request, username=username, password=password)
            if person is not None:
                auth_login(request, person)
            return redirect('dashboard')

    else:            
        forms=AuthenticationForm()
    context={
        'forms':forms
    }
    return render(request,'home/login.html',context)






def Logout(request):
    logout(request)
    return redirect('home')