from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=10),
    marca = models.CharField(max_length=30),
    veiculo = models.CharField(max_length=100),
    km_troca_oleo = models.CharField(max_length=6),
