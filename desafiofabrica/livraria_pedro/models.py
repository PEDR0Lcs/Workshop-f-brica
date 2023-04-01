from django.db import models
from uuid import uuid4


class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    valor = models.FloatField(max_length=50)
    lancamento = models.DateField()


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
