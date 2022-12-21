from django.contrib import admin
from .models import Livros, Categoria, Emprestimo
# importando as classes para realização de cadastro na área do admin

admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimo)