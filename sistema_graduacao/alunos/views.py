from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from alunos.forms import AlunoForm
from .models import Aluno



class ListaAlunosView(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = 'alunos/lista.html'
    context_object_name = 'alunos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_alunos'] = Aluno.objects.count()
        return context


class CreateAlunoView(LoginRequiredMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/alunoform.html'
    success_url = reverse_lazy('lista_alunos')


class UpdateAlunoView(LoginRequiredMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'alunos/form.html'
    success_url = reverse_lazy('lista_alunos')


class DeleteAlunoView(LoginRequiredMixin, DeleteView):
    model = Aluno
    template_name = 'alunos/delete.html'
    success_url = reverse_lazy('lista_alunos')
