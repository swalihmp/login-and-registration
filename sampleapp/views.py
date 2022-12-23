from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

from django.contrib.sessions.models import Session


@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['uid']
        pass1=request.POST['upass']
        user=authenticate(username=username,password=pass1)
        
        if(username==""):
           messages.info(request,'User Name must be enterd')
        elif(pass1==""):
            messages.info(request,'Password Must be Entered')
        
        else:   
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'User Name or Password is Incorrect.....')
                return redirect('login')

    return render(request,'login.html')

def SignupPage(request):
    if request.user.is_authenticated:
         return redirect('home')
    if request.method=='POST':
        uname=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
    