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