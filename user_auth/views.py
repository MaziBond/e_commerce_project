from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserCreationForm, UserLoginForm, UserUpdateForm, UserProfileUpdateForm
from .models import User, UserProfile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Error registering')
            return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})


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
                return redirect('dashboard')
            else:
                messages.error(request, 'Error logging in')
                return redirect('login')
        else:
            messages.error(request, 'Error logging in')
            return redirect('login')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def custom_authenticate(email=None, password=None):
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
    except Exception as e:
        return None

@login_required(login_url='login')
def create_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, 
                                            request.FILES,
                                            instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated successfully')
            return redirect('get-profile')
        else:
            messages.error(request, 'An error occurred while updating your profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.userprofile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user/profile_edit.html', context)

@login_required(login_url='login')
def get_profile(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    context = {
        'user_profile': user_profile,
        'user_detail': user
    }
    return render(request, 'user/profile_detail.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')
