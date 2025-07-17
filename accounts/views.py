from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import logout,login,authenticate
# Create your views here.


def signupaccount(request):
    if request.method == 'GET':
        return render(request,'signupaccount.html',{'form':UserCreationForm})
    else:
        try:
            if len(request.POST['password1']) == 0:
                return render(request,'signupaccount.html',{'form':UserCreationForm,'error':' PASSWORD MUST BE FILLED '})
            elif request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                return redirect('home')   
            else:
                return render(request,'signupaccount.html',{'form':UserCreationForm,'error':' PASSWORD DO NOT MATCH '})
        except IntegrityError:
                return render(request,'signupaccount.html',{'form':UserCreationForm,'error':' USER ALREADY EXISTS '})
        


def logoutaccount(request):
    logout(request)
    return redirect('home')


def loginaccount(request):
    if request.method == 'GET':
        return render(request,'loginaccount.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username = request.POST['username'],
                                    password = request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html',{'form':AuthenticationForm,'error':'Username or Password do not match'})
        else:
            login(request,user)
            return redirect('home')