from django.shortcuts import render, redirect
from app_cadastro_filmes.forms import *
from app_cadastro_filmes.models import *

def movies(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('home')  # Redireciona para a página inicial após o cadastro
    else:
        form = FilmeForm()

    return render(request, 'usuarios/movies.html', {'form': form})

def home(request):
    return render(request, "usuarios/home.html")
def events(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventoForm()
    return render(request, 'usuarios/events.html', {'form': form})

def persons(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ou redirecione para a página desejada
    else:
        form = PessoaForm()

    return render(request, 'usuarios/persons.html', {'form': form})

def editions(request):
    if request.method == 'POST':
        form = EdicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Ou redirecione para a página desejada
    else:
        form = EdicaoForm()

    return render(request, 'usuarios/editions.html', {'form': form})

def directors(request):
    if request.method == 'POST':
        form = DiretorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DiretorForm()

    return render(request, 'usuarios/directors.html', {'form': form})

def roteirists(request):
    if request.method == 'POST':
        form = RoteiristaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoteiristaForm()

    return render(request, 'usuarios/roteirists.html', {'form': form})

def actors(request):
    if request.method == 'POST':
        form = AtorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AtorForm()

    return render(request, 'usuarios/actors.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import InformacaoForm

def info(request):
    if request.method == 'POST':
        form = InformacaoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecione para a página desejada após salvar os dados
            return redirect('info')
    else:
        form = InformacaoForm()

    return render(request, 'usuarios/info.html', {'form': form})

def visualizar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'visualizacoes/visualizar_filmes.html', {'filmes': filmes})

def visualizar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'visualizacoes/visualizar_eventos.html', {'eventos': eventos})

