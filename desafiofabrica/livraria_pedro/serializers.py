from rest_framework import serializers
from livraria_pedro import models


class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Livros
        fields = '__all__'


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'
