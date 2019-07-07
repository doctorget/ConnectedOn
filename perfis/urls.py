from django.contrib import admin
from django.urls import path, re_path
from perfis import views

urlpatterns = [
    path(r'', views.index),
    path(r'perfis/', views.exibir),
    re_path(r'^perfis/(?P<perfil_id>\d+)$', views.exibir)
]