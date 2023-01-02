from django.db import models
from datetime import date # importado o date da biblioteca para pegar o dia de hoje
import datetime
from usuarios.models import Usuario


class Categoria(models.Model):
    nome = models.CharField(max_length = 30)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome
    

class Livros(models.Model):
    nome            = models.CharField(max_length = 100)
    autor           = models.CharField(max_length = 30)
    co_autor        = models.CharField(max_length = 30, blank = True) # blank = True torna não obrigatório o preenchimento do campo mas retorna string vazia
    data_cadastro   = models.DateField(default = date.today) # importa a data do dia automaticamente no campo
    emprestado      = models.BooleanField(default = False)
    categoria       = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING) # se eu apagar a categoria não acontece nada com o livro
    usuario         = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Livro'
        # serve para configurações da classe Livros    
        # classe criada dentro da classe Livros pois no banco aparecia no plural = Livross
        # com a classe meta o nome fica normal = Livros
    
    def __str__(self):
        return self.nome
    #define para que apareça o nome do usuario e não um objeto no admin

  
class Emprestimo(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    nome_emprestado_anonimo = models.CharField(max_length = 30, blank = True, null = True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now()) 
    data_devolucao  = models.DateTimeField(blank = True, null = True) # necessita tambem do null para poder não ser um campo de preenchimento obrigatório
    livro = models.ForeignKey(Livros, on_delete = models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices = choices, blank= True, null=True)
    
    def __str__(self):
        return f"{self.nome_emprestado} | {self.livro}"
    

