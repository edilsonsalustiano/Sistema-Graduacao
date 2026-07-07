from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]

        if Aluno.objects.filter(cpf=cpf).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Já existe um aluno cadastrado com este CPF."
            )

        return cpf
