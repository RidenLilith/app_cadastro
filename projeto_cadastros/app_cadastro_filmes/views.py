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
    return render(request, 'usuarios/events.html')

def persons(request):
    return render(request, 'usuarios/persons.html')

def editions(request):
    return render(request, 'usuarios/editions.html')

def directors(request):
    return render(request, 'usuarios/directors.html')

def roteirists(request):
    return render(request, 'usuarios/roteirists.html')

def actors(request):
    return render(request, 'usuarios/actors.html')

def info(request):
    return render(request, 'usuarios/info.html')
