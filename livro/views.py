from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario) # FILTRANDO APENAS OS LIVROS DO USUARIO QUE ESTÁ LOGADO  
        # (usuario = usuario) 1º usuario class Livros das models| | 2º variavel usuario da def home 
        return render(request, 'home.html', {'livros': livros})   
    else:
        return redirect('/auth/login/?status=2')
    
def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)#get pega o id que for igual ao id
        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro = livros) # filter() vai filtra tudo independendo do usuario
            return render(request, 'ver_livro.html', {'livro': livros, 'categoria_livro': categoria_livro, 'emprestimos': emprestimos})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')
