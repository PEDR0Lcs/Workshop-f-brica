from django.contrib import admin
from .models import Livros

class Livro(admin.ModelAdmin) :
    list_display= ('id_livro','titulo','autor','valor','lancamento')
