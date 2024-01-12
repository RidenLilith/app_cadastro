from django.db import models

class Pessoa(models.Model):
    Nome = models.CharField(max_length=255)
    Nome_Artístico = models.CharField(max_length=255, primary_key=True)
    Site = models.CharField(max_length=255)
    Status = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    class Meta:
        db_table = 'Pessoa'

class Evento(models.Model):
    NomeEvento = models.CharField(max_length=255, primary_key=True)
    Tipo = models.CharField(max_length=255)
    Ano_Inicio = models.IntegerField()
    Nacionalidade = models.CharField(max_length=255)
    class Meta:
        db_table = 'Evento'

class Filme(models.Model):
    Título = models.CharField(max_length=255, primary_key=True)
    Título_Pt = models.CharField(max_length=255)
    Título_Original = models.CharField(max_length=255)
    Gênero = models.CharField(max_length=255)
    Ano = models.IntegerField()
    Produtor = models.CharField(max_length=255)
    class Meta:
        db_table = 'Filme'

class Edição(models.Model):
    ID_Edição = models.IntegerField(primary_key=True)
    Data = models.CharField(max_length=255)
    Localização = models.CharField(max_length=255)
    NomeEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Vencedor = models.CharField(max_length=255)
    Premio = models.CharField(max_length=255)
    Categoria = models.CharField(max_length=255)
    Nome_Artístico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Edição'

class Informação(models.Model):
    ID_Informação = models.IntegerField(primary_key=True)
    Local_Estreia = models.CharField(max_length=255)
    Sala_Exibição = models.CharField(max_length=255)
    Arrecadação_Primeiro_Ano = models.BigIntegerField()
    Arrecadação_Total = models.BigIntegerField()
    Título = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ID_Edição = models.ForeignKey(Edição, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Informação'


class Ocorre(models.Model):
    NomeEvento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    ID_Edição = models.ForeignKey(Edição, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['NomeEvento', 'ID_Edição']]
        db_table = 'Ocorre'

class ÉJuri(models.Model):
    Nome_Artístico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    ID_Edição = models.ForeignKey(Edição, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['Nome_Artístico', 'ID_Edição']]
        db_table = 'ÉJuri'

class Participa(models.Model):
    Nome_Artístico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    Título = models.ForeignKey(Filme, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['Nome_Artístico', 'Título']]
        db_table = 'Participa'

class Indicado(models.Model):
    Nome_Artístico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    ID_Edição = models.ForeignKey(Edição, on_delete=models.CASCADE)
    Título = models.ForeignKey(Filme, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['Nome_Artístico', 'ID_Edição', 'Título']]
        db_table = 'Indicado'

class Possui(models.Model):
    Título = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ID_Informação = models.ForeignKey(Informação, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['Título', 'ID_Informação']]
        db_table = 'Possui'

class Ator(models.Model):
    Nome_Artístico = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    tdFilmesA = models.IntegerField()
    Ano_A = models.IntegerField()
    tdPremiosA = models.IntegerField()
    class Meta:
        db_table = 'Ator'

class Diretor(models.Model):
    Nome_Artístico = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    tdFilmesD = models.IntegerField()
    Ano_D = models.IntegerField()
    tdPremiosD = models.IntegerField()
    class Meta:
        db_table = 'Diretor'


class Roteirista(models.Model):
    Nome_Artístico = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    tdFilmesR = models.IntegerField()
    Ano_R = models.IntegerField()
    tdPremiosR = models.IntegerField()
    class Meta:
        db_table = 'Roteirista'
