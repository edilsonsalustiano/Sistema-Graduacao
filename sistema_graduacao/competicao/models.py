from django.db import models
from alunos.models import Aluno

class Competicoes(models.Model):

    STATUS_CHOICES = [
        ("ABERTA", "Aberta"),
        ("ENCERRADA", "Encerrada"),
        ("FINALIZADA", "Finalizada"),
    ]
     
    nome = models.CharField(max_length=200)
    organizacao = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    local = models.CharField(max_length=200)
    data = models.DateField()
    observacao = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ABERTA",
    )

    def __str__(self):
        return f'{self.nome} - {self.data}'

class InscricaoCompeticao(models.Model):
    competicao = models.ForeignKey(
        Competicoes,
        on_delete=models.CASCADE,
        related_name="inscricoes"
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="inscricoes_competicao"
    )

    categoria = models.CharField(max_length=100)

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aluno.nome} - {self.competicao.nome}"