from django import forms
from .models import Competicoes, InscricaoCompeticao


class CompeticoesForm(forms.ModelForm):
    class Meta:
        model = Competicoes
        fields = "__all__"

        widgets = {
            "data": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            )
        }

class InscricaoCompeticaoForm(forms.ModelForm):

    class Meta:
        model = InscricaoCompeticao
        fields = [
            "aluno",
            "categoria",
            "peso",
            "pago",
        ]