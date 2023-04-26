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
from django.contrib.auth import views as auth_views

from home.views import index
from contact_us.views import contact
from user_auth.views import (
    register, 
    user_login,
    user_logout,
    create_profile, 
    get_profile)
from product_pages.views import dashboard, get_all_reviews, reviews, get_single_review
from about_us.views import contributors


urlpatterns = [
    path('', index, name='home'),
    path('contact-us/', contact, name='contact-us'),
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/',register, name='signup'),
    path('user-profile-edit/', create_profile, name='profile-edit'),
    path('user-profile/', get_profile, name='get-profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('about-us/', contributors, name='about-us'),
    path('reviews/<int:product_id>/', get_all_reviews, name='get-reviews'),
    path('add-review/<int:product_id>/', reviews, name='add-review'),
    path('read-review/<int:review_id>/', get_single_review, name='read-review'),

    #reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
