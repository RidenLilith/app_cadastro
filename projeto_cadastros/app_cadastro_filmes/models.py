from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    nome_artistico = models.CharField(max_length=255, primary_key=True)
    site = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=50, blank=True)
    sexo = models.CharField(max_length=50, blank=True)

    def _str_(self):
        return self.nome_artistico
    

class Evento(models.Model):
    nome_evento = models.CharField(max_length=255, primary_key=True)
    tipo = models.CharField(max_length=255, blank=True)
    ano_inicio = models.IntegerField(blank=True, null=True)
    nacionalidade = models.CharField(max_length=255, blank=True)

    def _str_(self):
        return self.nome_evento

class Filme(models.Model):
    titulo = models.CharField(max_length=255, primary_key=True)
    titulo_pt = models.CharField(max_length=255, blank=True)
    titulo_original = models.CharField(max_length=255, blank=True)
    genero = models.CharField(max_length=255, blank=True)
    ano = models.IntegerField(blank=True, null=True)
    produtor = models.CharField(max_length=255, blank=True)

class Edicao(models.Model):
    id_edicao = models.IntegerField(primary_key=True)
    data = models.CharField(max_length=255, blank=True)
    localizacao = models.CharField(max_length=255, blank=True)
    nome_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    vencedor = models.CharField(max_length=255, blank=True)
    premio = models.CharField(max_length=255, blank=True)
    categoria = models.CharField(max_length=255, blank=True)
    nome_artistico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

class Informacao(models.Model):
    id_informacao = models.IntegerField(primary_key=True)
    local_estreia = models.CharField(max_length=255, blank=True)
    sala_exibicao = models.CharField(max_length=255, blank=True)
    arrecadacao_primeiro_ano = models.BigIntegerField(blank=True, null=True)
    arrecadacao_total = models.BigIntegerField(blank=True, null=True)
    titulo = models.ForeignKey(Filme, on_delete=models.CASCADE)
    id_edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)

class Ocorre(models.Model):
    nome_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    id_edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['nome_evento', 'id_edicao']]

class EJuri(models.Model):
    nome_artistico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['nome_artistico', 'id_edicao']]

class Participa(models.Model):
    nome_artistico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Filme, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['nome_artistico', 'titulo']]

class Indicado(models.Model):
    nome_artistico = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id_edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Filme, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['nome_artistico', 'id_edicao', 'titulo']]

class Possui(models.Model):
    titulo = models.ForeignKey(Filme, on_delete=models.CASCADE)
    id_informacao = models.ForeignKey(Informacao, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['titulo', 'id_informacao']]

class Ator(models.Model):
    nome_artistico = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    td_filmes_a = models.IntegerField(blank=True, null=True)
    ano_a = models.IntegerField(blank=True, null=True)
    td_premios_a = models.IntegerField(blank=True, null=True)

class Diretor(models.Model):
    nome_artistico = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    td_filmes_d = models.IntegerField(blank=True, null=True)
    ano_d = models.IntegerField(blank=True, null=True)
    td_premios_d = models.IntegerField(blank=True, null=True)

class Roteirista(models.Model):
    nome_artistico = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    td_filmes_r = models.IntegerField(blank=True, null=True)
    ano_r = models.IntegerField(blank=True, null=True)
    td_premios_r = models.IntegerField(blank=True, null=True)

