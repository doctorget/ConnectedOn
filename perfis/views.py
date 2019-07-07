from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request,perfil_id):
    perfil = Perfil()

    if perfil_id == '2':
       perfil = Perfil('Samuel Soares', 'samuel@samuel.com.br', '77777777', 'everis')

    if perfil_id == '4':
       perfil = Perfil('Romulo caetano', 'Romulo@troco.com.br', '74455443', 'stefanini')
    return render(request, 'perfil.html', {"p" : perfil})
