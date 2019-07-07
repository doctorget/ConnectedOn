from django.db import models

class Perfil(models.Model):

    nome = models.CharField(max_lenght=255, null=False)
    email = models.CharField(max_lenght=255, null=False)
    telefone = models.CharField(max_lenght=15, null=False)
    nome_empresa = models.CharField(max_lenght=255, null=False)
