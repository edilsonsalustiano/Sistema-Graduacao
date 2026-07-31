from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from competicao.models import Competicoes
from competicao.forms import CompeticoesForm


class ListaCompeticoesView(LoginRequiredMixin, ListView):
    model = Competicoes
    template_name = "competicao/lista.html"
    context_object_name = 'competicoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_competicoes"] = Competicoes.objects.count()
        return context

class CreateCompeticoesView(LoginRequiredMixin, CreateView):
    model = Competicoes
    form_class = CompeticoesForm
    template_name = "competicao/form.html"
    success_url = reverse_lazy("lista_competicoes")

class UpdateCompeticoesView(LoginRequiredMixin, UpdateView):
    model = Competicoes
    form_class = CompeticoesForm
    template_name = "competicao/form.html"
    success_url = reverse_lazy("lista_competicoes")

class DetailCompeticoesView(LoginRequiredMixin, DetailView):
    model = Competicoes
    template_name = "competicao/detalhe.html"
    context_object_name = "competicoes"

class DeleteCompeticoesView(LoginRequiredMixin, DeleteView):
    model = Competicoes
    template_name = "competicao/delete.html"
    success_url = reverse_lazy("lista_competicoes")
