from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not email or not password:
            messages.error(request, 'Email and password are required.')
            return render(request, 'authentication/register.html', {'title': 'Register'})

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'authentication/register.html', {'title': 'Register'})

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'authentication/register.html', {'title': 'Register'})

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        login(request, user)
        messages.success(request, f'Welcome {user.email}!')
        return redirect('home')

    return render(request, 'authentication/register.html', {'title': 'Register'})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'authentication/login.html', {'title': 'Login'})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')
