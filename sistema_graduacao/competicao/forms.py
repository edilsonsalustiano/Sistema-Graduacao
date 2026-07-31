from django import forms
from .models import Competicoes


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