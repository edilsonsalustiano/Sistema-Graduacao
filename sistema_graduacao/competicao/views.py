from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from competicao.models import Competicoes
from competicao.forms import CompeticoesForm
from .forms import InscricaoCompeticaoForm
from .models import Competicoes, InscricaoCompeticao

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


class AdicionarAlunoCompeticaoView(LoginRequiredMixin, CreateView):

    model = InscricaoCompeticao
    form_class = InscricaoCompeticaoForm
    template_name = "competicao/adicionar_aluno.html"

    def dispatch(self, request, *args, **kwargs):
        self.competicao = get_object_or_404(
            Competicoes,
            pk=self.kwargs["pk"]
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.competicao = self.competicao
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["competicao"] = self.competicao
        return context

    def get_success_url(self):
        return reverse(
            "detalhes_competicao",
            kwargs={"pk": self.competicao.pk}
        )

class RemoverInscricaoView(LoginRequiredMixin, DeleteView):

    model = InscricaoCompeticao
    template_name = "competicao/delete.html"

    def get_success_url(self):
        return reverse(
            "detalhes_competicao",
            kwargs={
                "pk": self.object.competicao.pk
            }
        )
