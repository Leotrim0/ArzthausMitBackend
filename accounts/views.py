from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please provide valid credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')
    else:
        messages.error(request, 'You must be logged in!')
        return redirect('login')