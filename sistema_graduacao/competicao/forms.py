from django import forms
from .models import Competicoes, InscricaoCompeticao


class CompeticoesForm(forms.ModelForm):
    class Meta:
        model = Competicoes
        fields = "__all__"

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "modalidade": forms.Select(attrs={"class": "form-select"}),
            "organizacao": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "data": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
            "observacao": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                }
            ),
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