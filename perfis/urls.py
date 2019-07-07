from django.contrib import admin
from django.urls import path, re_path
from perfis import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'perfis/', views.exibir),
    path(r'<int:perfil_id>/', views.exibir)
]