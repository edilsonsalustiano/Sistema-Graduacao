from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Modalidade


class ListModalidadeView(LoginRequiredMixin, ListView):
    model = Modalidade
    template_name = 'modalidades/lista.html'
    context_object_name = 'modalidades'


class CreateModalidadeView(LoginRequiredMixin, CreateView):
    model = Modalidade
    template_name = 'modalidades/form.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_modalidades')


class UpdateModalidadeView(LoginRequiredMixin, UpdateView):
    model = Modalidade
    template_name = 'modalidades/form.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_modalidades')


class DeleteModalidadeView(LoginRequiredMixin, DeleteView):
    model = Modalidade
    template_name = 'modalidades/delete.html'
    success_url = reverse_lazy('lista_modalidades')
