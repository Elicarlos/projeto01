
from django.db import models

# Create your models here.

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.FloatField()

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
