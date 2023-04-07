from django.contrib.auth.backends import BaseBackend
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login


from .forms import UserCreationForm, UserLoginForm
from .models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Error registering')
            return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = custom_authenticate(email=email, password=password)
            if user:
                print(request.user.is_authenticated)
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Error logging in')
                return redirect('login')
        else:
            messages.error(request, 'Error logging in')
            return redirect('login')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_authenticate(email=None, password=None):
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
    except Exception as e:
        return None
