from django.db import models


class Plano(models.Model):
    nome_plano = models.CharField(max_length=200)
    valor_plano = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome_plano} - R$: {self.valor_plano}"
