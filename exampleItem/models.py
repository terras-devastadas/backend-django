from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Comunidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Comunidade")
    descricao = models.TextField(verbose_name="Descrição da Comunidade")
    banner = models.ImageField(upload_to='banners/', null=True, blank=True, verbose_name="Banner da Comunidade")
    visibilidade_alunos = models.BooleanField(default=True, verbose_name="Visível para Alunos")
    visibilidade_professores = models.BooleanField(default=True, verbose_name="Visível para Professores")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome