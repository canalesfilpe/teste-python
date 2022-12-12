from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100),
    telefone = models.CharField(max_length=12),
    cnh = models.CharField(max_length=20),
