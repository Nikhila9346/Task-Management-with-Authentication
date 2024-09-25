from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']

        if p1 == p2:
            if User.objects.filter(username = user).exists():
                context={
                    'error': "USER ALREADY EXISTS"
                }
                return render(request, 'signup.html', context)
            else:
                User.objects.create_user(
                    username=user,
                    email = email,
                    password=p1
                )
                return redirect('login')
    return render(request, 'signup.html')
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        p = request.POST['password']

        user = authenticate(request, username = username, password = p)

        if user is not None:
            login(request, user)
            return redirect('home')
        

    return render(request, 'login.html')
    

def logout_user(request):
    logout(request)
    return redirect('login')
    
