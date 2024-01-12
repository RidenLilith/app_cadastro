from django import forms
from app_cadastro_filmes.models import *

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'Título': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Título_Pt': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Título_Original': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Gênero': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Ano': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'Produtor': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
        }

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Nome_Artístico': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Site': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'Status': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'Sexo': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'NomeEvento': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Tipo': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Ano_Inicio': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'Nacionalidade': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
        }

class InformacaoForm(forms.ModelForm):
    class Meta:
        model = Informação
        fields = '__all__'
        widgets = {
            'ID_Informacao': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'Local_Estreia': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'Sala_Exibição': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'Arrecadação_Primeiro_Ano': forms.NumberInput(attrs={'class': 'custom-input', 'required': False}),
            'Arrecadação_Total': forms.NumberInput(attrs={'class': 'custom-input', 'required': False}),
            'Título': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'ID_Edição': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edição
        fields = '__all__'
        widgets = {
            'ID_Edição': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'Data': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'Localização': forms.TextInput(attrs={'class': 'custom-input', 'required': True}),
            'NomeEvento': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'Vencedor': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'Premio': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'Categoria': forms.TextInput(attrs={'class': 'custom-input', 'required': False}),
            'Nome_Artístico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class OcorreForm(forms.ModelForm):
    class Meta:
        model = Ocorre
        fields = '__all__'
        widgets = {
            'NomeEvento': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'ID_Edição': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class ÉJuriForm(forms.ModelForm):
    class Meta:
        model = ÉJuri
        fields = '__all__'
        widgets = {
            'Nome_Artístico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'ID_Edição': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class ParticipaForm(forms.ModelForm):
    class Meta:
        model = Participa
        fields = '__all__'
        widgets = {
            'Nome_Artístico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'Título': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class IndicadoForm(forms.ModelForm):
    class Meta:
        model = Indicado
        fields = '__all__'
        widgets = {
            'Nome_Artístico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'ID_Edição': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'Título': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class PossuiForm(forms.ModelForm):
    class Meta:
        model = Possui
        fields = '__all__'
        widgets = {
            'Título': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'ID_Informação': forms.Select(attrs={'class': 'custom-input', 'required': True}),
        }

class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = '__all__'
        widgets = {
            'Nome_Artístico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'tdFilmesA': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'Ano_A': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'tdPremiosA': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
        }

class DiretorForm(forms.ModelForm):
    class Meta:
        model = Diretor
        fields = '__all__'
        widgets = {
            'Nome_Artístico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'tdFilmesD': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'Ano_D': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'tdPremiosD': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
        }

class RoteiristaForm(forms.ModelForm):
    class Meta:
        model = Roteirista
        fields = '__all__'
        widgets = {
            'Nome_Artístico': forms.Select(attrs={'class': 'custom-input', 'required': True}),
            'tdFilmesR': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'Ano_R': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
            'tdPremiosR': forms.NumberInput(attrs={'class': 'custom-input', 'required': True}),
        }
