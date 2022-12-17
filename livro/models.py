from django.db import models
from datetime import date # importado o date da biblioteca para pegar o dia de hoje

class Livros(models.Model):
    nome            = models.CharField(max_length = 100)
    autor           = models.CharField(max_length = 30)
    co_autor        = models.CharField(max_length = 30, blank = True) # blank = True torna não obrigatório o preenchimento do campo mas retorna string vazia
    data_cadastro   = models.DateField(default = date.today) # importa a data do dia automaticamente no campo
    emprestado      = models.BooleanField(default = False)
    nome_emprestado = models.CharField(max_length = 30, blank = True)
    data_emprestimo = models.DateTimeField(blank = True, null = True) # necessita tambem do null para poder não ser um campo de preenchimento obrigatório
    data_devolucao  = models.DateTimeField(blank = True, null = True) # necessita tambem do null para poder não ser um campo de preenchimento obrigatório
    tempo_duracao   = models.DateField(blank = True, null = True)     # necessita tambem do null para poder não ser um campo de preenchimento obrigatório
    
    class Meta:
        verbose_name = 'Livro'
        # serve para configurações da classe Livros    
        # classe criada dentro da classe Livros pois no banco aparecia no plural = Livross
        # com a classe meta o nome fica normal = Livros
    
    def __str__(self):
        return self.nome
    
