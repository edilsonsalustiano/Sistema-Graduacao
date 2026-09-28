from django.db import models


class Aula(models.Model):

    professor = models.CharField(max_length=200)
    turma = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.professor} - {self.turma}"


class Horario(models.Model):
    class DiaSemana(models.IntegerChoices):
        SEGUNDA = 0, "Segunda-feira"
        TERCA = 1, "Terça-feira"
        QUARTA = 2, "Quarta-feira"
        QUINTA = 3, "Quinta-feira"
        SEXTA = 4, "Sexta-feira"
        SABADO = 5, "Sábado"
        DOMINGO = 6, "Domingo"

    aula = models.ForeignKey(
        Aula,
        on_delete=models.CASCADE,
        related_name="horarios",
    )
    dia_semana = models.IntegerField(choices=DiaSemana.choices)
    hora = models.TimeField()

    class Meta:
        ordering = ["dia_semana", "hora"]

    def __str__(self):
        return f"{self.get_dia_semana_display()} às {self.hora:%H:%M}"