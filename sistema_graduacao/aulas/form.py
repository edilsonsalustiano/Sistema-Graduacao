from django import forms
from django.forms import inlineformset_factory
from alunos.models import Aluno
from .models import Aula, Horario


class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = "__all__"

        widgets = {
            "professor": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "turma": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "modalidade": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ["dia_semana", "hora"]

        widgets = {
            "dia_semana": forms.Select(attrs={"class": "form-select"}),
            "hora": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"},
                format="%H:%M",
            ),
        }


HorarioFormSet = inlineformset_factory(
    Aula,
    Horario,
    form=HorarioForm,
    extra=1,
    can_delete=True,
)


class AdicionarAlunoForm(forms.Form):
    aluno = forms.ModelChoiceField(
        queryset=Aluno.objects.none(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def __init__(self, *args, aula=None, **kwargs):
        super().__init__(*args, **kwargs)

        if aula and aula.modalidade:
            self.fields["aluno"].queryset = (
                Aluno.objects
                .filter(modalidades=aula.modalidade)
                .exclude(aulas=aula)
                .order_by("nome")
            )