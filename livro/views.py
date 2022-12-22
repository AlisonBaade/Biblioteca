from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro, CategoriaLivro
from django import forms

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario) # FILTRANDO APENAS OS LIVROS DO USUARIO QUE ESTÁ LOGADO  
        # (usuario = usuario) 1º usuario class Livros das models| | 2º variavel usuario da def home
        status_categoria = request.GET.get('cadastro_categoria')
        form = CadastroLivro()
        
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        
        form_categoria = CategoriaLivro()
        
        return render(request, 'home.html', {'livros': livros,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form,
                                             'status_categoria': status_categoria,
                                             'form_categoria': form_categoria})   
    else:
        return redirect('/auth/login/?status=2')
    
def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)#get pega o id que for igual ao id
        if request.session.get('usuario') == livros.usuario.id:
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimo.objects.filter(livro = livros) # filter() vai filtra tudo independendo do usuario
            form = CadastroLivro()
            
            form.fields['usuario'].initial = request.session['usuario'] # filtrando apenas as categorias do usuario logado
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            
            form_categoria = CategoriaLivro()

            return render(request, 'ver_livro.html', {'livro': livros, 'categoria_livro': categoria_livro,
                                                      'emprestimos': emprestimos,
                                                      'usuario_logado': request.session.get('usuario'),
                                                      'form': form,
                                                      'id_livro': id,
                                                      'form_categoria': form_categoria})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')


def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        
        if form.is_valid():
            form.save() # salvando o formulario 
            return redirect('/livro/home') # após realizar o cadastro redireciona para a home
        else:
            return HttpResponse('DADOS INVÁLIDOS')
        
def excluir_livro(request, id):
    livro  = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')

def cadastrar_categoria(request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    
    
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuario.objects.get(id = id_usuario)
        
        categoria = Categoria(nome = nome, descricao = descricao, usuario = user)
        categoria.save()
        return redirect('/livro/home?cadastro_categoria=1')
    else:
        return HttpResponse('Erro')