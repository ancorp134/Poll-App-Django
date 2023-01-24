from django.contrib import admin
from django.urls import path
from .views import Create_Poll



urlpatterns = [
    path('create_poll/' , Create_Poll),
]