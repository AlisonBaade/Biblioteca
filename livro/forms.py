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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # subscrevendo o __ini__ de sabeform
        self.fields['usuario'].widget = forms.HiddenInput()
        # faz com que o campo do usuario não apareça na hora do cadastro do livro
        

# outra maneira de fazer         
class CategoriaLivro(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(max_length=60)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget = forms.Textarea() # transformando o descricao.CharFields em TextArea