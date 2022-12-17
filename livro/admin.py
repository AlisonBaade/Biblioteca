from django.contrib import admin
from .models import Livros
# importando a classe Livros para aparecer na área do admin

admin.site.register(Livros)
