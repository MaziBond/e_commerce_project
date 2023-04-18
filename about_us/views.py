from django.shortcuts import render, get_list_or_404
from .models import AboutUs

def contributors(request):
    about_us = get_list_or_404(AboutUs)
    return render(request, 'about_us/about_us.html', {'about_us': about_us})
