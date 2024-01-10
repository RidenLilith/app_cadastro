from django import forms
from app_cadastro_filmes.models import *

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'  # Pode ajustar conforme necessário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'titulo_pt': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'titulo_original': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'genero': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'ano': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'produtor': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
        }

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'  # Pode ajustar conforme necessário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'nome_artistico': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'site': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),  # Se desejar, ajuste conforme necessário
            'status': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),  # Se desejar, ajuste conforme necessário
            'sexo': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),  # Se desejar, ajuste conforme necessário
        }



class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'  # Pode ajustar conforme necessário
        widgets = {
            'nome_evento': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'tipo': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'ano_inicio': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'nacionalidade': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
        }

class InformacaoForm(forms.ModelForm):
    class Meta:
        model = Informacao
        fields = '__all__'
        widgets = {
            'id_informacao': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'local_estreia': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'sala_exibicao': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'arrecadacao_primeiro_ano': forms.NumberInput(attrs={'class': 'custom-input', 'required': False}),
            'arrecadacao_total': forms.NumberInput(attrs={'class': 'custom-input', 'required': False}),
            'titulo': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'id_edicao': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = '__all__'
        widgets = {
            'data': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'localizacao': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'nome_evento': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'vencedor': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'premio': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'categoria': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'nome_artistico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class DiretorForm(forms.ModelForm):
    class Meta:
        model = Diretor
        fields = '__all__'  # Pode ajustar conforme necessário
        widgets = {
            'nome_artistico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'td_filmes_d': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'ano_d': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'td_premios_d': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
        }

class RoteiristaForm(forms.ModelForm):
    class Meta:
        model = Roteirista
        fields = '__all__'  # Pode ajustar conforme necessário
        widgets = {
            'nome_artistico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'td_filmes_r': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'ano_r': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'td_premios_r': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
        }

class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = '__all__'  # Pode ajustar conforme necessário
        widgets = {
            'nome_artistico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'td_filmes_a': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'ano_a': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'td_premios_a': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
        }