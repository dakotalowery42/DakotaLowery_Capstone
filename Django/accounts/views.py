from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User


def user_register(request):
    if request.method == 'POST':
        try:
            user_exists = User.objects.get(username=request.POST['username'])
            return render (request, 'register/UserAlreadyExists.html')
        except User.DoesNotExist:
            new_user = User(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('login')
    return render(request, 'register/register.html')


def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']

        )
        if user is not None:
            login(request, user)
            return redirect('proposals')
    return render(request, 'register/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')
