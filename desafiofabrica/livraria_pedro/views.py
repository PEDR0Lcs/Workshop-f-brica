from django.shortcuts import render
from serializers import LivrariaSerializer
from .models import Livros
from rest_framework import viewsets
from livraria_pedro import  LivrosViewSet

class LivrosViewSet(viewsets.ModelViewSet) :
    queryset= Livros.objects.all()
    serializer_class= LivrariaSerializer

