from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Modalidade


class ListModalidadeView(ListView):
    model = Modalidade
    template_name = 'modalidades/lista.html'
    context_object_name = 'modalidades'


class CreateModalidadeView(CreateView):
    model = Modalidade
    template_name = 'modalidades/form.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_modalidades')


class UpdateModalidadeView(UpdateView):
    model = Modalidade
    template_name = 'modalidades/form.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_modalidades')


class DeleteModalidadeView(DeleteView):
    model = Modalidade
    template_name = 'modalidades/delete.html'
    success_url = reverse_lazy('lista_modalidades')
