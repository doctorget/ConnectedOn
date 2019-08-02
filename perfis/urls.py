from django.contrib import admin
from django.urls import path, re_path
from perfis import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/', views.exibir, name='exibir'),
    path('perfis/<perfil_id>', views.exibir2)
]