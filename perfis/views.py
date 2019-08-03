from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html', {'perfis' : Perfil.objets.all()})

def exibir(request):
    return render(request, 'perfil.html')

def exibir2(request,perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html', {"p" : perfil})
