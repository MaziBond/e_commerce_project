from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from user_auth.models import UserProfile
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    context = {
        'user_profile': user_profile,
        'user_detail': user
    }
    return render(request, 'dashboard/dashboard.html', context)
