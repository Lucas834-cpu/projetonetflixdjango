from email.policy import default
from random import choice

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISE", "Análise"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
)

# Criar os Filmes
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to = 'thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacaoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default= timezone.now)
    objects = models.Manager()

    def __str__(self):
        return self.titulo


# Criar os episodios

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name='episodios', on_delete=models.CASCADE)
    titulo =  models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


# Criar os usuários

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")