from django.contrib import admin
from django.urls import path
from .views import Create_Poll , register_user , profile_view
from .forms import LoginForm
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('create_poll/' , Create_Poll),
    path('register_user/',register_user),
    path('accounts/login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html' , authentication_form = LoginForm)),
    path('accounts/profile/',profile_view),
]