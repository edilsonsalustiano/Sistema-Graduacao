from django.db import models

class Competicoes(models.Model):
     
    nome = models.CharField(max_length=200)
    organizacao = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    local = models.CharField(max_length=200)
    data = models.DateField()
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nome} - {self.data}'