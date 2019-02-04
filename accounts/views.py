from django.contrib.auth.management import get_default_username
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
from pip._vendor.requests import request


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Password Not Match'})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username & Password NOT Match.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')