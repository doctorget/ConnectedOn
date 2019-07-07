from django.contrib import admin
from django.urls import path
from perfis.views import index

urlpatterns = [
    path('', index),
]