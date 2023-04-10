"""e_commerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from home.views import index
from contact_us.views import contact
from user_auth.views import (
    register, 
    user_login,
    user_logout,
    create_profile, 
    get_profile)
from product_pages.views import dashboard


urlpatterns = [
    path('', index, name='home'),
    path('contact-us/', contact, name='contact-us'),
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/',register, name='signup'),
    path('user-profile-edit/', create_profile, name='profile-edit'),
    path('user-profile/', get_profile, name='get-profile'),
    path('dashboard/', dashboard, name='dashboard')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
