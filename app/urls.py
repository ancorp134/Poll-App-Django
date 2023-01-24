from django.contrib import admin
from django.urls import path
from .views import Create_Poll , register_user



urlpatterns = [
    path('create_poll/' , Create_Poll),
    path('register_user/',register_user),
]