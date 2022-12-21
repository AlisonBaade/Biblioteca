# esse arquivo não é padrão
from django import forms
from .models import Livros
from django.db import models
from datetime import date
from .models import Categoria

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
    # ('nome', 'autor', 'co_autor', 'data_cadastro', 'emprestado', 'categoria')